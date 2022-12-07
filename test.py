

import serial
port = "COM3"
import time
ser = serial.Serial(port, 9600, timeout=1000)  # open serial port
while True:
    print(("x"+"\z"+"\n").encode())
    ser.write()
    time.sleep(0.2)
# import time
# def xxx():
#     global ser
#     while True:
#         try:
#             print(ser.name)    
#             print(ser.isOpen())     # check which port was really used
#             line = ser.readline()
#             distance = ""
#             print(line)
#             time.sleep(0.2)
#         except:
#             print("accccccccccccccccccccccccccccccc")
#             time.sleep(0.2)
#             try:
#                 ser = serial.Serial(port, 9600, timeout=1000)
#             except:
#                 return False
#             pass
# while True:
#     xxx()