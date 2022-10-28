import serial
ser = serial.Serial('COM4', 9600, timeout=1)  # open serial port
while True:
    print(ser.name)         # check which port was really used
    line = ser.readline()   # write a string
    print(line) #
ser.close()             # close port