from sympy import re
import get_data
from flask import Flask, request
from pygame import mixer
import time
import json
import pandas as pd
import time
from sys import platform

mixer.init()
linkFile = "file.mp3"
app = Flask(__name__)
from get_data import Device_dow
device_dow = Device_dow()
# device_dow.read_data()
port = "COM3"
if platform == "linux" or platform == "linux2":
    linkFile = "/home/truyen/FsosAPI/file.mp3"
    port = "tty/USB0"
    print(linkFile)
    print(port)
    print(platform)

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

ser = serial.Serial(port, 9600, timeout=1) 

def start():
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


# @app.route('/on_light')
def den_on():
    try:
        import RPi.GPIO as GPIO#
        import time

        PORT_GPIO = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PORT_GPIO, GPIO.OUT)       
        GPIO.output(PORT_GPIO,GPIO.HIGH)
        GPIO.output(PORT_GPIO,GPIO.LOW)
        print("Den on")
    except:
        print("Loi")
    out = json.dumps("da bat")
    return out
# @app.route('/off_light')
def den_off():
    try:
        import RPi.GPIO as GPIO#
        import time

        PORT_GPIO = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PORT_GPIO, GPIO.OUT)        
        # GPIO.output(PORT_GPIO,GPIO.HIGH)
        GPIO.output(PORT_GPIO,GPIO.LOW)
        print("Den off")
    except:
        print("Loi")
        pass 
    out = json.dumps("da tat")
    return out    
@app.route('/')
@app.route('/data_device')
def data_device():
     # open serial port
    start_time = time.time()
    # while (time.time() - start_time) < 1:
    for i in range(10):
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
    # String a = "1,001,1,123456,123456,80,z/n";  
@app.route('/open_saving', methods=['POST'])
def open_saving():
    request_data = json.loads(request.data)
    id_ = request_data["id"]
    status_ = request_data["button_status"]
    lat = request_data["lat"]
    long = request_data["long"]
    line = "1,{id_},{status_},{lat},{lon},{line}80,z/n\n".format(id_=id_, status_=status_, lat=lat, long=long)
            # {
            #   "id":id, 
            #   "button_status":button_status
            #   "lat":lat,
            #   "long":long
            # }
    try:
        ser.write(line.encode())
    except:
        pass
    return line
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
    den_on()
    global is_on
    is_on  = True
    mixer.music.load('file.mp3')
    try:
        # global is_on
        while is_on == True:
            mixer.music.play()
            time.sleep(10)
    except:
        out = json.dumps("0")
        return out
    mixer.music.pause()
    is_on = False
    # out = json.dumps("1")
    # return out
@app.route('/off')
def off():
    den_off()
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

@app.route('/change_distance', methods=['POST'])
def change_distance():
    request_data = json.loads(request.data)
    if 'distance' in request_data:
        distance = request_data['distance']
        start_time = time.time()
        for i in range(10):
            print(ser.name)    
            print(ser.isOpen())     # check which port was really used
            print(distance)
            ser.write((distance+"\n").encode())
        return distance


if(__name__ == "__main__"):
    app.run(host = "0.0.0.0",debug=False)
    ser.close()             # close port