API: /data_device
không cần truyền vào API cái j cả

// 20221028103410
// http://127.0.0.1:5000/data_device
[
  {
    "id_device": "3",
    "lat": null,
    "long": null,
    "last_active_at": null,
    "update_date_at": 1666931636.2312610149,
    "battery_percentage": null,
    "button_status": null,
    "lost_connect":  0
  }
]
device: thiết bi đeo của
{	'id_device': '1', 
	'lat': '123456',
	'long': '80', 
	'last_active_at': '123456,80', 
	'update_date_at': 1666915126.391565, 
	'battery_percentage': None,
	'status': '123456'
}
API: /data_gateway
// 20221028113323
// http://127.0.0.1:5000/data_gateway

{
  "id_gateway": "009",
  "lat": "123456",
  "lon": "123456",
  "degreeDirection": "90"
}

api bật chuông 
/on
api tắt chuông 
/off
api  thay đổi thời gian an toàn
/change_time_out
{
    "time_safe":"6"
}
6 là số phút
mặc định là 10
mỗi lần khơi động là reset là 10
sss