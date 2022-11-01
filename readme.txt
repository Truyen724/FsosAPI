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

api bật chuông, bật đèn
/on
api tắt chuông, tắt đèn
/off

api đổi khoảng cách
/change_distance
{
    "distance":"6"
}
api mở rộng tìm kiếm
/open_saving', methods=['POST']
{
    "id":"6",
    "button_status":"1",
    "lat":"12223,33",
    "long":"12223,33"
}
Khi có báo động thì POST thông tin này vào
