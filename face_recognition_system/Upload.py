import json
import requests
headers = {"Authorization": "Bearer ya29.A0ARrdaM9cN_nypd_Cg66yGqG6ihHUU9K0yaP6vsJzIGU1aqTOGiDC6C8G7STUnNYqaTF2Dd2dFYb1J6bjrPG9EoBX9D9M_Yv5u8RgooqR-Qo51OylTp9uIg3ZAT48fPQLdIP0X-KkWPEh_fnt33kfnqO23GdE"}
para = {
    "name": "new.csv",
    "parents":["12npAMcHjWImfKQR16T92VDF8sCAl8W2z"]
    }
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./attendance_report/userEP3.csv", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)