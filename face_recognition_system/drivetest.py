from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth=GoogleAuth()
drive=GoogleDrive(gauth)

folder='12npAMcHjWImfKQR16T92VDF8sCAl8W2z'

#file1=drive.CreateFile({'parents' :[{'id' :folder}],'title' :'new.csv'})
#file1.FetchContent('./Attendance.csv')
#file1.Upload()

directory = 'C:/Users/Krunal/Downloads/face_recognition_system/face_recognition_system/attendance_report'
for f in os.listdir(directory):
	filename = os.path.join(directory, f)
	gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
	gfile.SetContentFile(filename)
	gfile.Upload()