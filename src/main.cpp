#include <Arduino.h>
// MOTOR_INCLUDES
#include <Stepper.h>
// #include <StringSplitter.h>
#include <motor_module.h>
#include <led_module.h>
#include <rgb_module.h>
#include <input.h>
// #include <function.h>
// #error
char UserInput[10];

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  RBG_SETUP();
  LED_SETUP();
  MOTOR_SETUP();
  Input_SETUP();

}


void loop() {

  if (Serial.available() > 0) {
    int bytesRead = Serial.readBytesUntil('\n', UserInput, sizeof(UserInput));
    if (bytesRead > 0) {
      UserInput[bytesRead] = '\0';  // Null-terminate the string

      char decision = UserInput[0];
      String valuesStr = String(UserInput).substring(1);  // Remove the first character (decision)

      int openingBracketPos = valuesStr.indexOf('[');
      int closingBracketPos = valuesStr.indexOf(']');
      
      if (openingBracketPos != -1 && closingBracketPos != -1) {
        valuesStr = valuesStr.substring(openingBracketPos + 1, closingBracketPos);
        
        // Split the string into tokens based on commas
        char valuesCharArray[valuesStr.length() + 1];
        valuesStr.toCharArray(valuesCharArray, sizeof(valuesCharArray));
        
        uint8_t values[3];
        int numValues = 0;
        char *valueToken = strtok(valuesCharArray, ",");
        while (valueToken != NULL && numValues < 3) {
          values[numValues] = atoi(valueToken);
          valueToken = strtok(NULL, ",");
          numValues++;
        }

    if (numValues == 3) {
      uint8_t values[3];
      for (int i = 0; i < 3; i++) {
        values[i] = atoi(valueToken[i].c_str());
      }

    }

  }
      // UserInput[bytesRead] = '\0';  // Null-terminate the string

      // // Split the message into decision and value
      // char decision = UserInput[0];
      // uint8_t values = atoi(UserInput + 2);
      

    // UserInput = Serial.read();
    //switch cases
    switch (decision)
    {
    case '1':
      Led_On();
      break;
    case '2':
      Led_Off();
      break;
    case '3':
      SET_RGB_R();
      break;

    case '4':
      SET_RGB_G();
      break;
    
    case '5':
      SET_RGB_B();
      break;

    case '6':
      SET_RGB_OFF();
      break;

    case '7':
      Motor_On();
      break;
    
    case '8':
      Motor_Off();
      break;
    case '9':
      mainFunction();
      break;
    default:
          //unsupported decision
      break;

    }

    } 

  }
  
}















    // if(UserInput == 'o'){

    //   Led_On();

    // }
    // if(UserInput == 'x'){

    //   Led_Off();

    // }
    // if(UserInput == 'r'){

    //   SET_RGB_R();

    // }
    // if(UserInput == 'g'){

    //   SET_RGB_G();

    // }
    // if(UserInput == 'b'){

    //   SET_RGB_B();   

    // }
    // if(UserInput == 'n'){

    //   SET_RGB_OFF();

    // }
    // if(UserInput == 'a'){

    //   Motor_On();

    // }
    // if(UserInput == 'c'){

    //   Motor_Off();

    // }







