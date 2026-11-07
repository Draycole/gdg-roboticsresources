int TRIG_PIN 9 
int ECHO_PIN 10  
//this sets up the pin numbers for our trig and echo pins.

long duration;
int distance;
//sets up the variables distance and duration, so we'll be able to calculate with them

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Serial.begin(9600);
  Serial.println("Ultrasonic Sensor Test Started");
}

void loop() {
  // Trigger the ultrasonic pulse
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Measure the echo return time
  duration = pulseIn(ECHO_PIN, HIGH);

  // Convert time to distance (cm)
  distance = duration * 0.034 / 2;

  // Print distance to Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  delay(500);
}
