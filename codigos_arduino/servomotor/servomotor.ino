#include <Servo.h>

Servo miServo;  // crea objeto servo

void setup() {
  miServo.attach(9); // conecta el servo al pin 9
}

void loop() {
  miServo.write(0);    // mueve a 0 grados
  delay(1000);         // espera 1 segundo

  miServo.write(180);  // mueve a 180 grados
  delay(1000);         // espera 1 segundo

  miServo.write(0);    // vuelve a 0 grados
  delay(1000);         // espera 1 segundo
}
