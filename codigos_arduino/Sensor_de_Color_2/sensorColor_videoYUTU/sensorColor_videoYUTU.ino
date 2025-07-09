  
#define S0 2		// S0 a pin 2 MORADO
#define S1 3		// S1 a pin 3 VERDE
#define S2 4		// S2 a pin 4  NARANJA
#define S3 5		// S3 a pin 5  AMARILLO
#define salidaTCS 8	// salidaTCS a pin 8 AZUL
#define pin9 9 // Salida 


void setup() {
  pinMode(S0, OUTPUT);		// pin 2 como salida
  pinMode(S1, OUTPUT);		// pin 3 como salida
  pinMode(S2, OUTPUT);		// pin 4 como salida
  pinMode(S3, OUTPUT);		// pin 5 como salida
  pinMode(salidaTCS, INPUT);	// pin 8 como entrada
  pinMode(pin9,OUTPUT);
  digitalWrite(pin9,HIGH);
  
  digitalWrite(S0,HIGH);	// establece frecuencia de salida
  digitalWrite(S1,LOW);		// del modulo al 20 por ciento
  
  Serial.begin(9600);		// inicializa monitor serie a 9600 bps
}

void loop() {
  digitalWrite(S2,LOW);			// establece fotodiodos
  digitalWrite(S3,LOW);			// con filtro rojo
  int rojo = pulseIn(salidaTCS, LOW);	// obtiene duracion de pulso de salida del sensor
  delay(200);				// demora de 200 mseg
  
  digitalWrite(S2,HIGH);		// establece fotodiodos
  digitalWrite(S3,HIGH);		// con filtro verde
  int verde = pulseIn(salidaTCS, LOW);	// obtiene duracion de pulso de salida del sensor
  delay(200);				// demora de 200 mseg
  
  digitalWrite(S2,LOW);			// establece fotodiodos
  digitalWrite(S3,HIGH);		// con filtro azul
  int azul = pulseIn(salidaTCS, LOW);	// obtiene duracion de pulso de salida del sensor
  delay(200);				// demora de 200 mseg
  
  Serial.print("R:");			// muestra texto
  Serial.print(rojo);			// muestra valor de variable rojo

  Serial.print("\t");			// espacio de tabulacion

  Serial.print("V:");			// muestra texto
  Serial.print(verde);			// muestra valor de variable verde

  Serial.print("\t");			// espacio de tabulacion

  Serial.print("A:");			// muestra texto
  Serial.println(azul);			// muestra valor de variable azul
  					// y salto de linea
  if (verde < 300 && rojo > 300 && azul > 80){
    Serial.println("VERDE");
    digitalWrite(pin9, HIGH);
  }
  else if (verde < 90 && rojo < 60 && azul < 100){
    Serial.println("NARANJA");
    digitalWrite(pin9, LOW);
    delay(1000);
    digitalWrite(pin9,HIGH);
  }
}
  