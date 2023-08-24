import tkinter as tk 
from functionality import turnOnLed
from functionality import turnOffLed



#arduino = serial.Serial('COM6', baudrate=115200, timeout=1)

def creatingTinkerWindow():
       #  Creating tkinter window 
       root = tk.Tk()
       root.title('Blink GUI')
       btn_On=tk.Button(root, text="Turn On", command=turnOnLed)

       
       btn_On.grid(row=5, column=11)
       btn_Off=tk.Button(root, text="Turn Off", command=turnOffLed)
       btn_Off.grid(row=5, column=12)
       root.geometry("350x350")
       root.mainloop()