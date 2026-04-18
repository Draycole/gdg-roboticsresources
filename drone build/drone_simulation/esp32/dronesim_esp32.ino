#include "Wire.h"
#include <MPU6050_light.h>

MPU6050 mpu(Wire);
unsigned long timer = 0;

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22); 
  
  byte status = mpu.begin();
  if(status != 0) {
    while(1) { 
      Serial.println(F("Error: MPU6050 not found. Check wiring!"));
      delay(1000); 
    }
  }
  
  Serial.println(F("CALIBRATING... Keep the ESP32 steady on a flat surface."));
  delay(2000);
  mpu.calcOffsets(); 
  Serial.println(F("READY: Stream starting..."));
}

void loop() {
  mpu.update();

  // 100Hz is perfect for real-time physics
  if((millis() - timer) > 500) { 
    // Format: Roll,Pitch,Yaw
    Serial.print(mpu.getAngleX()); 
    Serial.print(",");
    Serial.print(mpu.getAngleY());
    Serial.print(",");
    Serial.println(mpu.getAngleZ());
    timer = millis();
  }
}