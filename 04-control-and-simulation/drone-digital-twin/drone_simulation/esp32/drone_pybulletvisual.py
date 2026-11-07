import pybullet as p
import pybullet_data
import serial
import time
import math

SERIAL_PORT = 'COM16'
BAUD_RATE = 115200

def run_digital_twin():
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -9.81)

    try:
        print("Loading URDF model...")
        drone_id = p.loadURDF("drone_colored.urdf", [0, 0, 1])
        print("Model loaded successfully!")
    except p.error:
        print("URDF not found! Creating a fallback 3D Box...")
        visual_id = p.createVisualShape(shapeType=p.GEOM_BOX, halfExtents=[0.3, 0.3, 0.1], rgbaColor=[0, 0.7, 1, 1])
        drone_id = p.createMultiBody(baseMass=1, baseVisualShapeIndex=visual_id, basePosition=[0, 0, 1])

    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)
        print(f"Connected to {SERIAL_PORT} successfully.")
    except Exception as e:
        print(f"SERIAL ERROR: {e}")
        return

    print("--- Waiting for data ---")
    
    try:
        while True:
            # ---- DEBUG: print everything raw ----
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                print(f"RAW: '{line}'")  # <-- shows exactly what ESP32 is sending
                
                parts = line.split(',')
                print(f"PARTS: {parts} (count: {len(parts)})")  # <-- shows the split
                
                if len(parts) == 3:
                    try:
                        roll  = math.radians(float(parts[0]))
                        pitch = math.radians(float(parts[1]))
                        yaw   = math.radians(float(parts[2]))
                        print(f"ANGLES: roll={math.degrees(roll):.1f} pitch={math.degrees(pitch):.1f} yaw={math.degrees(yaw):.1f}")
                        
                        orientation = p.getQuaternionFromEuler([roll, pitch, yaw])
                        p.resetBasePositionAndOrientation(drone_id, [0, 0, 1], orientation)
                    except ValueError as e:
                        print(f"VALUE ERROR: {e} on line: '{line}'")

            p.stepSimulation()
            time.sleep(1./240.)

    except KeyboardInterrupt:
        print("\nClosing...")
    finally:
        ser.close()
        p.disconnect()

if __name__ == "__main__":
    run_digital_twin()