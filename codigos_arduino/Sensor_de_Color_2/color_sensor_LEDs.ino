// define pins
const int S0 = 2;
const int S1 = 3;
const int S2 = 4;
const int S3 = 5;
const int signal = 6;
// note - sensor LED pin is hardwired to 5V. You can use
// an I/O pin to turn the white LEDs on and off instead, but a single
// I/O pin cannot provide enough current for all four LEDs at full brightness.

// LED pins
const int redLED = 10;
const int greenLED = 9;
const int blueLED = 8;

// define variables for pulses
unsigned long red;
unsigned long blue;
unsigned long green;
unsigned long clear;

void setup() { // put your setup code here, to run once:
  // set pin modes
  pinMode(S0,OUTPUT);
  pinMode(S1,OUTPUT);
  pinMode(S2,OUTPUT);
  pinMode(S3,OUTPUT);
  pinMode(signal,INPUT);
  pinMode(redLED,OUTPUT);
  pinMode(greenLED,OUTPUT);
  pinMode(blueLED,OUTPUT);

  /* set frequency scaling - 
     S0 S1 | Output frequency scaling
     L  L  | power down
     L  H  | 2%
     H  L  | 20%
     H  H  | 100%
  */
  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);

  // initialize serial communication
  Serial.begin(9600);
}

void loop() { // put your main code here, to run repeatedly:
  /* cycle through each filter type and use the pulseIn command to measure pulse length.
  Frequency *increases* with more light, so the pulse length will *decrease*.
  /  S2 S3 | Photodiode Type
     L  L  | Red
     L  H  | Blue
     H  L  | Clear (no filter)
     H  H  | Green
  */
  
  // clear
  digitalWrite(S2,HIGH);
  digitalWrite(S3,LOW);
  clear = pulseIn(signal,HIGH);
  
  // red
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);
  red = pulseIn(signal,HIGH);

  // green
  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  green = pulseIn(signal,HIGH);

  // blue
  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  blue = pulseIn(signal,HIGH);

  /* map the red, green, and blue values to a more intuitive 0-255 range where
     0 means less light and 255 means more. This part will require calibration
     depending on your colored surfaces and ambient light levels.
  */
  red = map(red,80,30,0,255);
  green = map(green,80,30,0,255);
  blue = map(blue,80,30,0,255);
  
// Threshold to determine if the sensor detects a color
const int detectionThreshold = 100;  // Adjust this based on your sensor's readings

// Check if any significant color is detected
if (red <= green && red <= blue && red < detectionThreshold) {  // Red is the lowest and below threshold
    digitalWrite(redLED, HIGH);
    digitalWrite(greenLED, LOW);
    digitalWrite(blueLED, LOW);
} else if (green <= red && green <= blue && green < detectionThreshold) {  // Green is the lowest and below threshold
    digitalWrite(redLED, LOW);
    digitalWrite(greenLED, HIGH);
    digitalWrite(blueLED, LOW);
} else if (blue <= red && blue <= green && blue < detectionThreshold) {  // Blue is the lowest and below threshold
    digitalWrite(redLED, LOW);
    digitalWrite(greenLED, LOW);
    digitalWrite(blueLED, HIGH);
} else {  // No significant color detected
    digitalWrite(redLED, LOW);
    digitalWrite(greenLED, LOW);
    digitalWrite(blueLED, LOW);
}



  // print readings
  
  Serial.print("Red: ");
  Serial.print(red);
  Serial.print(" | Green: ");
  Serial.print(green);
  Serial.print(" | Blue: ");
  Serial.println(blue);
  

}
