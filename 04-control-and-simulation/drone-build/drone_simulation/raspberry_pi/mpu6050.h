#ifndef MPU6050_H
#define MPU6050_H

#include "hardware/i2c.h"
#include <stdbool.h>

#define MPU6050_ADDR     0x68
#define PWR_MGMT_1       0x6B
#define SMPLRT_DIV       0x19
#define CONFIG_REG       0x1A
#define GYRO_CONFIG      0x1B
#define ACCEL_CONFIG     0x1C
#define ACCEL_XOUT_H     0x3B
#define WHO_AM_I         0x75

// Sensitivity scalars (datasheet §6.1, §6.2)
// Accel ±2g  → 16384 LSB/g
// Gyro  ±250°/s → 131 LSB/°/s
#define ACCEL_SENSITIVITY 16384.0f
#define GYRO_SENSITIVITY  131.0f

typedef struct {
    float ax, ay, az;   // g
    float gx, gy, gz;   // degrees/s
} MPU6050_Data;

typedef struct {
    float gx, gy, gz;   // gyro offsets (degrees/s)
} MPU6050_Offsets;

bool    mpu6050_init(i2c_inst_t *i2c);
bool    mpu6050_read(i2c_inst_t *i2c, MPU6050_Data *out);
void    mpu6050_calibrate(i2c_inst_t *i2c, MPU6050_Offsets *offsets, int samples);

#endif
