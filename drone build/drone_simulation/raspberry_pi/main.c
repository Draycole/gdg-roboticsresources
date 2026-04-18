#include <stdio.h>
#include <math.h>
#include "pico/stdlib.h"
#include "hardware/i2c.h"
#include "mpu6050.h"

// ── pin config ───────────────────────────────────────────────────────────────
#define I2C_PORT    i2c0
#define I2C_SDA     4    // GP4
#define I2C_SCL     5    // GP5
#define I2C_FREQ    400000  // 400kHz fast mode

// ── complementary filter constant ────────────────────────────────────────────
// 0.98 = trust gyro 98%, correct with accel 2% each step
// Increase toward 1.0 for smoother but driftier output
// Decrease toward 0.9 for more accel correction but noisier
#define ALPHA 0.98f

#define LOOP_MS 10   // 100Hz

int main() {
    stdio_init_all();   // enables USB serial (shows up as COM port)
    sleep_ms(2000);     // give host time to open the port

    // ── I2C init ─────────────────────────────────────────────────────────────
    i2c_init(I2C_PORT, I2C_FREQ);
    gpio_set_function(I2C_SDA, GPIO_FUNC_I2C);
    gpio_set_function(I2C_SCL, GPIO_FUNC_I2C);
    gpio_pull_up(I2C_SDA);
    gpio_pull_up(I2C_SCL);

    // ── MPU6050 init ─────────────────────────────────────────────────────────
    printf("Initialising MPU6050...\n");
    if (!mpu6050_init(I2C_PORT)) {
        printf("ERROR: MPU6050 not found. Check wiring!\n");
        while (1) tight_loop_contents();
    }

    // ── calibration ──────────────────────────────────────────────────────────
    printf("CALIBRATING... Keep the Pico steady.\n");
    MPU6050_Offsets offsets;
    mpu6050_calibrate(I2C_PORT, &offsets, 200);  // 200 samples × 5ms = 1 second
    printf("READY\n");

    // ── complementary filter state ───────────────────────────────────────────
    float roll = 0.0f, pitch = 0.0f, yaw = 0.0f;
    uint32_t last_time = to_ms_since_boot(get_absolute_time());

    // ── main loop ────────────────────────────────────────────────────────────
    while (1) {
        MPU6050_Data d;
        if (!mpu6050_read(I2C_PORT, &d)) {
            printf("READ ERROR\n");
            sleep_ms(LOOP_MS);
            continue;
        }

        // Apply gyro calibration offsets
        d.gx -= offsets.gx;
        d.gy -= offsets.gy;
        d.gz -= offsets.gz;

        // Delta time in seconds
        uint32_t now = to_ms_since_boot(get_absolute_time());
        float dt = (now - last_time) / 1000.0f;
        last_time = now;

        // Accel-derived angles (degrees) — reliable when stationary
        float accel_roll  =  atan2f(d.ay, d.az) * 180.0f / (float)M_PI;
        float accel_pitch = -atan2f(d.ax, d.az) * 180.0f / (float)M_PI;

        // Complementary filter — fuse gyro integration + accel correction
        roll  = ALPHA * (roll  + d.gx * dt) + (1.0f - ALPHA) * accel_roll;
        pitch = ALPHA * (pitch + d.gy * dt) + (1.0f - ALPHA) * accel_pitch;
        yaw  += d.gz * dt;  // no mag, so yaw is gyro-only (drifts over time)

        // Same CSV format your Python expects: Roll,Pitch,Yaw
        printf("%.2f,%.2f,%.2f\n", roll, pitch, yaw);

        sleep_ms(LOOP_MS);
    }

    return 0;
}