from functionality import turnOnMotor
from functionality import turnOffMotor
# from mainMenu import menuFunction
# from function_RGB import turnOnLed
# from function_RGB import turnOffLed



def motorFunction():
    while True:
     num = int(input("Enter '1' to turn 'on' the Motor and '2' to turn Motor 'off': "))
     if(num==0x01): #1
       turnOnMotor()
     
     elif(num==0x02): #2
       turnOffMotor()
       
     elif(num==0x00): #0
         exit(0x00)

# menuFunction()