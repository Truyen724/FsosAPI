import serial
port = "COM3"
ser = serial.Serial(port, 9600, timeout=1)  # open serial port
import time
for i in range(5):
    print(ser.name)    
    print(ser.isOpen())     # check which port was really used
    distance = "xxxxxxxxxxxxxxxxxxxxxxxx"
    print((distance+"\n").encode())
    
