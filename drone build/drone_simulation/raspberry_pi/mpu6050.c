#include "mpu6050.h"
#include "pico/stdlib.h"
#include <string.h>

// ── low-level helpers ────────────────────────────────────────────────────────

static bool reg_write(i2c_inst_t *i2c, uint8_t reg, uint8_t val) {
    uint8_t buf[2] = {reg, val};
    int ret = i2c_write_blocking(i2c, MPU6050_ADDR, buf, 2, false);
    return ret == 2;
}

static bool reg_read(i2c_inst_t *i2c, uint8_t reg, uint8_t *dst, size_t len) {
    // Send register pointer, then read
    int ret = i2c_write_blocking(i2c, MPU6050_ADDR, &reg, 1, true); // true = repeated start
    if (ret != 1) return false;
    ret = i2c_read_blocking(i2c, MPU6050_ADDR, dst, len, false);
    return ret == (int)len;
}

// ── public API ───────────────────────────────────────────────────────────────

bool mpu6050_init(i2c_inst_t *i2c) {
    // WHO_AM_I sanity check
    uint8_t who = 0;
    if (!reg_read(i2c, WHO_AM_I, &who, 1) || who != 0x68) {
        return false;   // wrong device or not connected
    }

    reg_write(i2c, PWR_MGMT_1,  0x00);  // wake up, use internal oscillator
    reg_write(i2c, SMPLRT_DIV,  0x07);  // sample rate = 1kHz / (1+7) = 125 Hz
    reg_write(i2c, CONFIG_REG,  0x06);  // DLPF ~5Hz — smooth but not laggy
    reg_write(i2c, GYRO_CONFIG, 0x00);  // ±250 °/s
    reg_write(i2c, ACCEL_CONFIG,0x00);  // ±2g

    sleep_ms(100);  // let it settle
    return true;
}

bool mpu6050_read(i2c_inst_t *i2c, MPU6050_Data *out) {
    uint8_t raw[14];  // ACCEL(6) + TEMP(2) + GYRO(6)
    if (!reg_read(i2c, ACCEL_XOUT_H, raw, 14)) return false;

    // Each value is big-endian 16-bit signed
    int16_t ax_raw = (int16_t)(raw[0]  << 8 | raw[1]);
    int16_t ay_raw = (int16_t)(raw[2]  << 8 | raw[3]);
    int16_t az_raw = (int16_t)(raw[4]  << 8 | raw[5]);
    // raw[6..7] is temperature — skip it
    int16_t gx_raw = (int16_t)(raw[8]  << 8 | raw[9]);
    int16_t gy_raw = (int16_t)(raw[10] << 8 | raw[11]);
    int16_t gz_raw = (int16_t)(raw[12] << 8 | raw[13]);

    out->ax = ax_raw / ACCEL_SENSITIVITY;
    out->ay = ay_raw / ACCEL_SENSITIVITY;
    out->az = az_raw / ACCEL_SENSITIVITY;
    out->gx = gx_raw / GYRO_SENSITIVITY;
    out->gy = gy_raw / GYRO_SENSITIVITY;
    out->gz = gz_raw / GYRO_SENSITIVITY;

    return true;
}

void mpu6050_calibrate(i2c_inst_t *i2c, MPU6050_Offsets *offsets, int samples) {
    double gx_sum = 0, gy_sum = 0, gz_sum = 0;
    MPU6050_Data d;

    for (int i = 0; i < samples; i++) {
        if (mpu6050_read(i2c, &d)) {
            gx_sum += d.gx;
            gy_sum += d.gy;
            gz_sum += d.gz;
        }
        sleep_ms(5);
    }

    offsets->gx = (float)(gx_sum / samples);
    offsets->gy = (float)(gy_sum / samples);
    offsets->gz = (float)(gz_sum / samples);
}