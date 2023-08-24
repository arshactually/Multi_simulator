#include <Arduino.h>
// MOTOR_INCLUDES
#include <Stepper.h>

// MOTOR_DEFINES
#define motor_clock "Motor is rotating AntiClockwise"    //Motor is rotating Clockwise
#define motor_off "Motor is rotating Clockwise"

// MOTOR__DRIVER_PINS
int myMotorPins[] = {0x04,0x05,0x06,0x07};

#define IN1 myMotorPins[0] //4
#define IN2 myMotorPins[1] //5
#define IN3 myMotorPins[2] //6
#define IN4 myMotorPins[3] //7



const int stepsPerRevolution = 0x800; //2048;  // change this to fit the number of steps per revolution

Stepper myStepper(stepsPerRevolution, IN1, IN3, IN2, IN4);

void MOTOR_SETUP(){
        // MOTOR_SETUP
       // set the speed at 5 rpm
       myStepper.setSpeed(0x14);  //20

}

void Motor_On(){
      myStepper.step(stepsPerRevolution);
      Serial.print(motor_clock); Serial.print("\n");
      // delay(1000);


}


void Motor_Off(){
     myStepper.step(-stepsPerRevolution);
      Serial.print(motor_off); Serial.print("\n");
      // delay(1000);


}