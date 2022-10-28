import serial
ser = serial.Serial('COM3', 9600, timeout=1)  # open serial port
while True:
    print(ser.name)         # check which port was really used
    line = ser.readline()   # write a string
    try:
        get_data(line)#
        print(device_dow.get_libraries())
        print(device_dow.get_gate_way())
        print(line)
    except:
        pass