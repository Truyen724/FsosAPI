import get_data
from flask import Flask
from pygame import mixer
import time
import json
import pandas as pd
import time
mixer.init()
app = Flask(__name__)
from get_data import Device_dow
device_dow = Device_dow()
device_dow.read_data()
import serial
def get_data(line):
    global device_dow
    line = str(line).replace("b","").replace(" ","").replace("'","")
    print(line)
    data = line.split(",")
    if(data[0]=="0"):
        device_dow.init_gate_way(data[1],data[2],data[3], data[4])
        # print(device_dow.get_gate_way())
    if(data[0]=="1"):
        device_dow.update_data(data[1],data[3],data[4],data[5],data[2])
        # print(device_dow.get_libraries())

def start():
    ser = serial.Serial('COM3', 9600, timeout=1)  # open serial port

    for i in range(5):
        print(ser.name)    
        print(ser.isOpen())     # check which port was really used
        line = ser.readline()   # write a string
        try:
            get_data(line)#
            # print(device_dow.get_libraries())
            print(device_dow.get_gate_way())
        except:
            pass
# start()



@app.route('/data_device')
def data_device():

    ser = serial.Serial('COM3', 9600, timeout=1)  # open serial port
    start_time = time.time()
    for i in range(5):
        print(ser.name)    
        print(ser.isOpen())     # check which port was really used
        line = ser.readline()   # write a string
        try:
            get_data(line)#
            # print(device_dow.get_libraries())
            print(device_dow.get_gate_way())
        except:
            pass

    # a, b = device_dow.get_libraries()
    a = device_dow.get_libraries()
    dataA = pd.DataFrame(a)
    # c = {}
    # try:
    #     if(device_dow.gateway != None):
    #         c = device_dow.get_gate_way()
    # except:
    #     pass
    
    # dataB = pd.Series(c)
    # out = {
    #     "lst_device": dataA.to_json(orient="records"),
    #     # "lst_strange_device":str(b),
    #     "gatewayinfo": dataB.to_json()
    # }
    # dataout = pd.Series(out)
    return dataA.to_json(orient="records")
@app.route('/data_gateway')
def data_gateway():
    c = {}
    try:
        if(device_dow.gateway != None):
            c = device_dow.get_gate_way()
    except:
        pass
    dataB = pd.Series(c)
    return  dataB.to_json()
is_on = False
@app.route('/on')
def on():
    global is_on
    is_on  = True
    mixer.music.load('file.mp3')

    while is_on == True:
        mixer.music.play()
        time.sleep(50)
    mixer.music.pause()
    is_on = False
    return
@app.route('/off')
def off():
    global is_on
    is_on = False
    mixer.music.pause()
    return 
if(__name__ == "__main__"):
    app.run(host = "0.0.0.0",debug=True)
# ser.close()             # close port