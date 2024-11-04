#include <Servo.h>

Servo myServo;

void setup() {
  myServo.attach(9); // Attach the servo on pin 9
}

void loop() {
  myServo.write(0);   // Move to 0 degrees
  delay(1000);        // Wait for a second
  myServo.write(90);  // Move to 90 degrees
  delay(1000);        // Wait for a second
  myServo.write(180); // Move to 180 degrees
  delay(1000);        // Wait for a second
}
