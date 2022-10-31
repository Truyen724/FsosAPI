from sympy import re
import get_data
from flask import Flask, request
from pygame import mixer
import time
import json
import pandas as pd
import time
mixer.init()
app = Flask(__name__)
from get_data import Device_dow
device_dow = Device_dow()
# device_dow.read_data()
import serial
def get_data(line):
    global device_dow
    line = str(line).replace("b","").replace(" ","").replace("'","")
    print(line)
    data = line.split(",")
    if(data[0]=="0"):
        device_dow.init_gate_way(data[1],data[2],data[3], data[4])
        print(data[1],data[2],data[3], data[4])
    if(data[0]=="1"):
        device_dow.update_data(data[1],data[3],data[4],data[5],data[2])
        # print(device_dow.get_libraries())
        # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    # print(data[0]=="1")
    # print(data[0]+"Data type")
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
start()



@app.route('/data_device')
def data_device():
    ser = serial.Serial('COM3', 9600, timeout=1)  # open serial port
    start_time = time.time()
    while (time.time() - start_time) < 2:
        print(ser.name)    
        print(ser.isOpen())     # check which port was really used
        line = ser.readline()   # write a string
        # try:
        get_data(line)#
        # print(device_dow.get_libraries())
        print(device_dow.get_gate_way())
    #     except:
    #         print("Loi")

    # a, b = device_dow.get_libraries()
    a = device_dow.get_libraries()
    dataA = pd.DataFrame(a)

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
    try:
        while is_on == True:
            mixer.music.play()
            time.sleep(50)
        
    except:
        out = json.dumps("0")
        return out
    mixer.music.pause()
    is_on = False
    out = json.dumps("1")
    return out
@app.route('/off')
def off():
    try:
        global is_on
        is_on = False
        mixer.music.pause()
    except:
        out = json.dumps("0")
        return out
    out = json.dumps("1")
    return out
@app.route('/change_time_out', methods=['POST'])
def change_time_out():
    framework = None
    request_data = json.loads(request.data)
    if 'time_safe' in request_data:
        framework = request_data['time_safe']
        get_data.time_out = int(framework)*60

    return str(get_data.time_out)
    
if(__name__ == "__main__"):
    app.run(host = "0.0.0.0",debug=True)
# ser.close()             # close port