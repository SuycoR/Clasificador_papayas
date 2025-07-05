int S0 = 51;
int S1 = 52;
int S2 = 49;
int S3 = 50;
int outPin = 48;

unsigned int redPW = 0;
unsigned int greenPW = 0;
unsigned int bluePW = 0;

void setup() {
  Serial.begin(9600);

  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(outPin, INPUT);

  // Configurar frecuencia de salida al 100%
  digitalWrite(S0, HIGH);
  digitalWrite(S1, HIGH);

  Serial.println("***Electrotec - TCS3200***");
}

void loop() {
  // Leer rojo
  digitalWrite(S2, LOW);
  digitalWrite(S3, LOW);
  delay(50);
  redPW = pulseIn(outPin, LOW);

  // Leer verde
  digitalWrite(S2, HIGH);
  digitalWrite(S3, HIGH);
  delay(50);
  greenPW = pulseIn(outPin, LOW);

  // Leer azul
  digitalWrite(S2, LOW);
  digitalWrite(S3, HIGH);
  delay(50);
  bluePW = pulseIn(outPin, LOW);

  // Mostrar valores
  Serial.print("Red PW: ");
  Serial.print(redPW);
  Serial.print(" | Green PW: ");
  Serial.print(greenPW);
  Serial.print(" | Blue PW: ");
  Serial.println(bluePW);

  // Detectar color aproximado
  if (redPW < greenPW && redPW < bluePW) {
    Serial.println("Color detectado: ROJO");
  } 
  else if (greenPW < redPW && greenPW < bluePW) {
    Serial.println("Color detectado: VERDE");
  } 
  else if (bluePW < redPW && bluePW < greenPW) {
    Serial.println("Color detectado: AZUL");
  } 
  else {
    Serial.println("Color detectado: DESCONOCIDO");
  }

  Serial.println("------------------------");
  delay(500);
}
