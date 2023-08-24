import serial 
import threading
from values_input import takeRGBValues

# This is sending a decison of doing something
# if it is value this, execute the function this for eg. Motor on
On_VALUE = b'1' 
OFF_VALUE =b'2'
RED_VALUE = b'3' 
GREEN_VALUE =b'4'
BLUE_VALUE = b'5' 
RGB_OFF_VALUE =b'6'
MOTOR_ON_VALUE =b'7'
MOTOR_OFF_VALUE =b'8'

decision =b'9'

decision_turnoff =b'10'

# My task is somehow to send a decison i.e analog.write(decision)
# but also the values analog.write(value)
# Main Task how to do it? Sending decision and value together.




# R_VALUE =b'9'
# G_VALUE =b'10'
# B_VALUE =b'11'


# Open the serial connection
arduino = serial.Serial('COM6', baudrate=115200, timeout=1) 



def turnOnLed():
        arduino.write(On_VALUE)
        arduino_data = arduino.readline()
        recieved_data= arduino_data.decode().strip()
        print("Recieved: " , recieved_data)



def turnOffLed():
        arduino.write(OFF_VALUE)
        arduino_data = arduino.readline()
        recieved_data= arduino_data.decode().strip()
        print("Recieved: " , recieved_data)


def SET_LED_R():
        arduino.write(RED_VALUE)
        arduino_data = arduino.readline()
        recieved_data= arduino_data.decode().strip()
        print("Recieved: " , recieved_data)

def SET_LED_G():
        arduino.write(GREEN_VALUE)
        arduino_data = arduino.readline()
        recieved_data= arduino_data.decode().strip()
        print("Recieved: " , recieved_data)

def SET_LED_B():
        arduino.write(BLUE_VALUE)
        arduino_data = arduino.readline()
        recieved_data= arduino_data.decode().strip()
        print("Recieved: " , recieved_data)

def SET_LED_OFF():
        arduino.write(OFF_VALUE)
        arduino_data = arduino.readline()
        recieved_data= arduino_data.decode().strip()
        print("Recieved: " , recieved_data)


def turnOnMotor():
        arduino.write(MOTOR_ON_VALUE)
        arduino_data = arduino.readline()
        recieved_data= arduino_data.decode().strip()
        print("Recieved: " , recieved_data)



def turnOffMotor():
        arduino.write(MOTOR_OFF_VALUE)
        arduino_data = arduino.readline()
        recieved_data= arduino_data.decode().strip()
        print("Recieved: " , recieved_data)

def sendDeicision():
        # Calling the function to take input values
        channels = takeRGBValues()
        data_to_send = bytes(channels)
        turn_off_channels = bytes([0, 0, 0])

#Concatinating values of decison and values of channels 
        message = f'{decision.decode()}:{data_to_send[0]}:{data_to_send[1]}:{data_to_send[2]}'
        # message = f'{decision.decode()}:{",".join(map(str, data_to_send))}'
        message = f'{decision.decode()}:{data_to_send}'
        turn_off_message= f'{decision_turnoff.decode()}:{",".join(map(str, turn_off_channels))}'
        # Flag to control the loop
        exit_signal = False

        def user_input_thread():
                global exit_signal
                input("Press Enter to turn off the LED: ")
                exit_signal = True

        # Start the user input thread
        input_thread = threading.Thread(target=user_input_thread)
        input_thread.start()

        try:
             while not exit_signal:
                #Analog write of the concatinated value of decision and channels
                arduino.write(message)

                # arduino_confirmation = arduino.readline().decode().strip()
                # print("Arduino Confirmation:", arduino_confirmation)
        except KeyboardInterrupt:
                pass
        finally:
    
                # arduino.write(bytes([0, 0, 0]))
                arduino.write(turn_off_message)
                input_thread.join()  # Wait for the user input thread to finish

        # Close the serial connection
        arduino.close()



# Approach Two 
# also not working 

# def serialWriteR():
#         arduino.write(R_VALUE)
#         arduino_data = arduino.readline()
#         recieved_data= arduino_data.decode().strip()



# def serialWriteG():
#         arduino.write(G_VALUE)
#         arduino_data = arduino.readline()
#         recieved_data= arduino_data.decode().strip()


# def serialWriteB():
#         arduino.write(B_VALUE)
#         arduino_data = arduino.readline()
#         recieved_data= arduino_data.decode().strip()




# #Approach three 
# # def function():
#         arduino.write(decision)
#         arduino.write(data_to_send)
     