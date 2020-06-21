const int stepPin = 6;
const int dirPin = 7;
//const int stepPin = 4;
//const int dirPin = 5;
const int enable = 3;

void setup() {
  // Sets the two pins as Outputs
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(enable, OUTPUT);
  digitalWrite(dirPin, LOW);
  digitalWrite(enable, LOW);
  Serial.begin(9600);
  Serial.println("Connection established...");
}
void loop() {
  digitalWrite(dirPin, HIGH); // Enables the motor to move in a particular direction
  // Makes 3200 pulses for making one full cycle rotation
  //if (Serial.available()) {
     // Enables the motor to move in a particular direction
    // String steps = Serial.readStringUntil('\n');
    String steps = "3200";
    Serial.println(steps.toInt());
    if (steps.toInt() > 0){
      digitalWrite(dirPin, HIGH);
      for (int i = 0; i < steps.toInt(); i++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(200);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(200);
      }
    }else{
      digitalWrite(dirPin, LOW);
      for (int i = 0; i < -steps.toInt(); i++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(200);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(200);
      }
    }
  //}
}
