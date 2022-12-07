# import mysql.connector
from datetime import datetime
import re, uuid
import json
time_out  = 10
class thiet_bi_deo:
    def __init__(self, id = 1, boat_id = 1,out_of_safe_zone = 0, name = "unknow",is_active = 1,last_active_at = None , lat = None, lon = None, status = 0, battery_percentage = None, update_date_at = None,degreeDirection = None,is_update = 1,ble = 0, water = 0, type = None):
        self.id = id
        self.boat_id = boat_id
        self.name = name
        self.is_active = is_active
        self.last_active_at = last_active_at
        self.lat = lat
        self.lon = lon
        self.status = status
        self.battery_percentage = battery_percentage
        self.update_date_at = datetime.now().timestamp()
        self.degreeDirection = degreeDirection
        self.lost_connect = 0
        self.is_update = 1
        self.out_of_safe_zone = out_of_safe_zone
        self.ble = ble
        self.water = water
        self.type = type
# Kiểm tra thời gian
    def check_time_and_status(self):
        time_dif = datetime.now() - datetime.fromtimestamp(float(self.update_date_at))
        print(time_dif)
        if(time_dif.total_seconds()>time_out):
            self.lost_connect = 1
        else:
            self.lost_connect = 0
# Set thời gian lại cho máy
    def update_data(self, id,lat,lon,bat_perc, status, out_zone, ble, water, type):
        if id == self.id:
            if(lat!=""):
                self.last_active_at = lat+ ","+lon
            self.lat = lat
            self.lon = lon
            self.bat_perc =bat_perc
            self.update_date_at = datetime.now().timestamp()
            self.status = status
            self.is_update = "1"
            self.out_of_safe_zone = out_zone
            self.ble = ble
            self.water = water
            self.type = type
    def get_libraries(self):
        out = {
            "id_device":self.id,
            "lat":self.lat,
            "long":self.lon,
            "last_active_at":self.last_active_at,
            "update_date_at":self.update_date_at,
            "battery_percentage":self.battery_percentage,
            "button_status ":self.status,
            "lost_connect":  self.lost_connect,
            "is_update": self.is_update,
            "out_of_safe_zone": self.out_of_safe_zone,
            "ble":self.ble,
            "water":self.water,
            "type":self.type
        }
        return out
class Device_dow:
    def __init__(self):
        self.lst = []
        self.lst_strange = []
    def get_libraries(self):
        # lib =[]
        lib_strange = []
        for device in self.lst_strange:
            lib_strange.append(device.get_libraries())
            device.check_time_and_status()
        return lib_strange
    def init_gate_way(self, id, lat, lon,degreeDirection, type):
        self.gateway = thiet_bi_deo(id = int(id),lat = lat,lon = lon,degreeDirection = int(degreeDirection), type = int(type))
    def get_gate_way(self):
        lib = {
            "id_gateway":self.gateway.id,
            "lat":self.gateway.lat,
            "long":self.gateway.lon,
            "degree_direction":self.gateway.degreeDirection,
            "type" :self.gateway.type
        }
        return lib
    def update_data(self, id, lat, lon,bat_perc,status, out_zone, ble, water, type):
        print("Xin chào")
        if len(self.lst_strange) == 0:
            new = thiet_bi_deo(id = int(id),lat = lat,lon = lon,battery_percentage = int(bat_perc), status = int(status), out_of_safe_zone = int(out_zone), ble = int(ble),water = int(water),type = int(type))
            print("SSSSSS")
            print(new.get_libraries())
            self.lst_strange.append(new)
        else:
            x = 0
            for device in self.lst_strange:
                if(id == device.id):
                    x = 1
                    device.update_data(id, lat, lon, bat_perc,status, out_zone)
            if x == 0:
                new = thiet_bi_deo(id = int(id),lat = lat,lon = lon,battery_percentage = int(bat_perc), status = int(status))
                self.lst_strange.append(new)