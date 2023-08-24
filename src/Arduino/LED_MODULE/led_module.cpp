#include <Arduino.h>

#define led_turned_on "Led is turned On"
#define led_turned_off "Led is turned off"

#define ledPin    10  // 10
// int ledPin = 10;


void LED_SETUP() {
  pinMode(ledPin, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}


void Led_On() {
    
    digitalWrite(ledPin, HIGH);
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.print(led_turned_on);


}

void Led_Off() {
    
      digitalWrite(ledPin, LOW);
      digitalWrite(LED_BUILTIN, LOW);
      Serial.print(led_turned_off);  Serial.print("\n");

}