from Extra import *

from rgbBlink import numberRGB
from numMotor import motorFunction
from functionality import sendDeicision



def menuFunction():
    options = [0x00,0x01,0x02,0x03,0x04,0x05]
    ans=True
    while ans:
      print ("1.Stimulate RGB\n2.Stimulate LED\n3.Stimulate Motor\n4.Exit/Quit")

      ans=int(input("What would you like to do?"))
      
      if ans==options[1]:  #1
        print("\nEntered RGB Simulation")
        numberRGB() 

      elif ans==options[2]:  #2
        print("\nEntered LED Simulation") 
        #LED NUMBER
        numberBlink.numberLed()
      elif ans==options[3]:  #3
        print("\nEntered Motor Simulation") 
        motorFunction()
      elif ans==options[4]:  #3
        print("\nEntered RGB Input Simulator") 
        sendDeicision()

      elif ans==options[5]:  #4
        print("\n Goodbye") 
        exit(options[0])    #0
      elif ans !="":
        print("\n Not Valid Choice Try again") 
  


        