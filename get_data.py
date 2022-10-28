import mysql.connector
from datetime import datetime
import re, uuid
import json

# joins elements of getnode() after each 2 digits.
# using regex expression
# print ("Mac Address:  ", end="")
# mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
# print(x)
time_out  = 10*60
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Ntt@2432001",
  database="fsos"
)
class thiet_bi_deo:
    def __init__(self, id = 1, boat_id = 1, name = "unknow",is_active = 1,last_active_at = "", lat = "", lon = "", status = 0, battery_percentage = "", update_date_at = "",degreeDirection = "" ):
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

# Kiểm tra thời gian
    # def check_time_and_status(self):
    #     time_dif = datetime.now() - datetime.fromtimestamp(self.last_active_at)
    #     if(time_dif>time_out):
    #         return True
    #     elif(self.status!=0):
    #         return True
    #     else:
    #         return False

# Set thời gian lại cho máy
    def update_data(self, id,lat,lon,bat_perc, status):
        if id == self.id:
            if(lat!=""):
                self.last_active_at = lat+ ","+lon
            self.lat = lat
            self.lon = lon
            self.bat_perc =bat_perc
            self.update_date_at = datetime.now().timestamp()
            self.status = status
    def get_libraries(self):
        out = {
            "id_device":self.id,
            "lat":self.lat,
            "long":self.lon,
            "last_active_at":self.last_active_at,
            "update_date_at":self.update_date_at,
            "battery_percentage":self.battery_percentage,
            "button_status ":self.status
        }
        return out
class Device_dow:
    def __init__(self):
        self.lst = []
        self.lst_strange = []
        
    def read_data(self):
        try:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM fsos.device left join fsos.device_realtime_data ON  device.id = device_realtime_data.id;")
            myresult = mycursor.fetchall()
            for result in myresult:
                x = thiet_bi_deo(id = result[0],boat_id = result[1], name=result[2],is_active = result[3],last_active_at = result[4],lat = result[6], lon = result[7],status=result[8],battery_percentage = result[9], update_date_at = result[10],degreeDirection = "")
                self.lst.append(x)
        except:
            pass
    # def update_data(self, id, lat, lon,bat_perc,status):
    #     for device in self.lst:
    #         device.update_data(id, lat, lon, bat_perc,status)
    #     for device in self.lst_strange:
    #         device.update_data(id, lat, lon, bat_perc,status)
    def get_libraries(self):
        lib =[]
        lib_strange = []
        for device in self.lst:
            lib.append(device.get_libraries())
        for device in self.lst_strange:
            lib_strange.append(device.get_libraries())
        # out = str(lib),str(lib_strange)
        # return lib,lib_strange
        return lib
    def init_gate_way(self, id, lat, lon,degreeDirection):
        self.gateway = thiet_bi_deo(id = id,lat = lat,lon = lon,degreeDirection = degreeDirection)
    def get_gate_way(self):
        lib = {
            "id_gateway":self.gateway.id,
            "lat":self.gateway.lat,
            "long":self.gateway.lon,
            "degree_direction":self.gateway.degreeDirection
            # "id_gateway_":mac
        }
        return lib
    def update_data(self, id, lat, lon,bat_perc,status):
        x = 0
        for device in self.lst:
            if(id == device.id):
                x = 1
                device.update_data(id, lat, lon, bat_perc,status)
        if x == 0:
            # y = 0
            # for device_strange in self.lst_strange:
            #     if(device_strange.id == id):
            #         y = 1
            #         device_strange.update_data(id, lat, lon, bat_perc,status)
            # if(y == 0):
            new = thiet_bi_deo(id = id,lat = lat,lon = lon,bat_perc = bat_perc, status = status)
            self.lst_strange.append(new)
            self.lst.append(new)

        