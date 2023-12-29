String inputString = "";
bool stringComplete = false;
int letra;

void setup() {
  Serial.begin(115200);
  inputString.reserve(200);
  
  pinMode(2, OUTPUT);
  //serialEvent();
  
  digitalWrite(2, HIGH);
  delay(2000);
  digitalWrite(2, LOW);
  delay(2000);
  
}

void loop() {

    if(Serial.available() > 0)
    {
      letra = (char)Serial.read();
      if(letra)
      {
        printf("letra");
        digitalWrite(2, HIGH);
        delay(500);
        digitalWrite(2. LOW);
      }
    }

    // Clear the string and reset the flag
    inputString = "";
    stringComplete = false;
  
}

void serialEvent() {
  while (Serial.available()) {
      inputString = Serial.readString();
      stringComplete = true;
  }
}
