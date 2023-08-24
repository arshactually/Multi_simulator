# from function_RGB import SET_LED_R
# from function_RGB import SET_LED_G
# from function_RGB import SET_LED_B
# from function_RGB import SET_LED_OFF

from functionality import SET_LED_R
from functionality import SET_LED_G
from functionality import SET_LED_B
from functionality import SET_LED_OFF
# from mainMenu import menuFunction



# from functionality import turnOnLed
# from functionality import turnOffLed

def numberRGB():
    while True:
     num = int(input(
       "Enter '5' to turn the LED 'Red'\nEnter '6' to turn the LED 'Green'\nEnter '7' to turn the LED 'Blue'\nEnter '8' to turn LED 'off'\nInput:  "))
     
     if(num== 0x05):  #5
       SET_LED_R()
     
     elif(num==0x06): #6
       SET_LED_G()
      #  SET_LED_B()
    
     elif(num==0x07): #7
       SET_LED_B()
    #    SET_LED_G()

     elif(num==0x08): #8
       SET_LED_OFF()

     elif(num==0x00): #0
       exit(0x00)
# menuFunction()
