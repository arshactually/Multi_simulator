#include <Arduino.h>

// RGB_DEFINES
#define Red_turned_on "RGB is turned Red"
#define Green_turned_on "RGB is turned Green"
#define Blue_turned_on "RGB is turned Blue"
#define RGB_turned_off "RGB is turned off"


// RGB_PINS
int myPins[] = {0x0F,0x10,0x11};

int channels[] = {0x00, 0xF7,0x78};


#define PIN_RED    myPins[0]         //15 // GPIO23
#define PIN_GREEN  myPins[1]         //16 // GPIO22
#define PIN_BLUE   myPins[2]         //17 // GPIO21

void RBG_SETUP(){
    
  // RGB_SETUP
  pinMode(PIN_RED,   OUTPUT);
  pinMode(PIN_GREEN, OUTPUT);
  pinMode(PIN_BLUE,  OUTPUT);

}


void SET_RGB_R(){
        analogWrite(PIN_RED,  channels[1] ); // =0xF7 -- 247
        analogWrite(PIN_GREEN, channels[0]); // =0x00 -- 0
        analogWrite(PIN_BLUE,  channels[0]); // =0x00 -- 0
        Serial.print(Red_turned_on); Serial.print("\n");

}



void SET_RGB_G(){
        analogWrite(PIN_RED,   channels[0]); // =0x00 -- 0
        analogWrite(PIN_GREEN, channels[1]); // =0xF7 -- 247
        analogWrite(PIN_BLUE,  channels[0]); // =0x00 -- 0
        Serial.print(Green_turned_on); Serial.print("\n");


}


void SET_RGB_B(){
        analogWrite(PIN_RED,   channels[0]); // =0x00 -- 0
        analogWrite(PIN_GREEN, channels[2]); // =0x78 -- 120
        analogWrite(PIN_BLUE,  channels[1]); // =0xF7 -- 247
        Serial.print(Blue_turned_on); Serial.print("\n");

}

void SET_RGB_OFF(){
        analogWrite(PIN_RED,   channels[0]); // =0x00 -- 0
        analogWrite(PIN_GREEN, channels[0]); // =0x00 -- 0
        analogWrite(PIN_BLUE,  channels[0]); // =0x00 -- 0
        Serial.print(RGB_turned_off); Serial.print("\n");

}