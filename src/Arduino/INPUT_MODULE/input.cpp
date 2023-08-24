#include <Arduino.h>

// RGB_DEFINES
#define Display_color "The RGB is displaying the required color"

// RGB_PINS
int myPins[] = {0x0F, 0x10, 0x11};

#define PIN_RED    myPins[0]         //15 // GPIO23
#define PIN_GREEN  myPins[1]         //16 // GPIO22
#define PIN_BLUE   myPins[2]         //17 // GPIO21

void Input_SETUP() {
    pinMode(PIN_RED,   OUTPUT);
    pinMode(PIN_GREEN, OUTPUT);
    pinMode(PIN_BLUE,  OUTPUT);
}

void write_function(uint8_t value1, uint8_t value2, uint8_t value3) {
    analogWrite(PIN_RED,   value1);
    analogWrite(PIN_GREEN, value2);
    analogWrite(PIN_BLUE,  value3);
    Serial.println(Display_color);

}

void mainFunction(uint8_t values[3]){
    while (true)
    {
        if (Serial.available()) { 

            uint8_t values[3];
            Serial.readBytes(values, 3); 



       write_function(values[0], values[1], values[2]);

            // Send confirmation back to Python with changed values
            Serial.print("Values changed to: ");
            Serial.print(values[0]);
            Serial.print(", ");
            Serial.print(values[1]);
            Serial.print(", ");
            Serial.println(values[2]);
    }
    
    }
    
}

