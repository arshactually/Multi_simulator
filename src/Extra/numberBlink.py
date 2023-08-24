from functionality import turnOnLed
from functionality import turnOffLed
# from mainMenu import menuFunction
# from function_RGB import turnOnLed
# from function_RGB import turnOffLed



def numberLed():
    while True:
     num = int(input("Enter '1' to turn 'on' the LED and '2' to turn LED 'off': "))
     if(num==0x01):  #1
       turnOnLed()
     
     elif(num==0x02): #2
       turnOffLed()
       
     elif(num==0x00): #3
       
       exit(0x00)

# menuFunction()






# def numberLed():
#     while True:
#      num = int(input("Enter '5' to turn 'on' the LED and '6' to turn LED 'off': "))
#      if(num==5):
#        turnOnLed()
     
#      elif(num==6):
#        turnOffLed()