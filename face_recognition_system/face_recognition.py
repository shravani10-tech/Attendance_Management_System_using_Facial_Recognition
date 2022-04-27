from os import close
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector.fabric import connect
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import pyttsx3
import sys
import csv
import json
import requests
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd

class Face_Recognition:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
        self.root.wm_iconbitmap("Purple E-sports Illustrative Gaming and Technology Logo.ico")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("Algerian",35,"bold"),bg="Light grey",fg="Black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        self.var_sr_no=IntVar()
        self.var_Subject=StringVar()
        self.var_Class=StringVar()
        self.var_Division=StringVar()
        #img1
        img_bottom=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\facedet.png")
        img_bottom=img_bottom.resize((650,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl1=Label(self.root,image=self.photoimg_bottom)
        f_lbl1.place(x=0,y=55,width=650,height=700)

        #img2
        img_top=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_top=img_top.resize((950,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=650,y=55,width=950,height=700)
        
        #Button
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,font=("Arial Black",15,"bold"),bg="DARKGREEN",fg="white",cursor="hand2")
        b1_1.place(x=365,y=620,width=200,height=40)
        
        SQA2=Label(f_lbl1,text="Subject:",font=("Arial Black",12,"bold"),bg="red",width=18)
        SQA2.place(x=0,y=550)

        self.txtSQA2=ttk.Combobox(f_lbl1,textvariable=self.var_Subject,font=("Arial Black",12,"bold"),state="readonly",width=15)
        self.txtSQA2["values"]=("Select","Mathematics","English","Hindi","Social Sciences","Science")
        self.txtSQA2.current(0)
        self.txtSQA2.place(x=200,y=550,width=200)

        Search_label1=Label(f_lbl1,text="Division:",font=("Arial Black",12,"bold"),bg="red",fg="Black")
        Search_label1.place(x=0,y=500,width=200)

        self.Search_combo1=ttk.Combobox(f_lbl1,textvariable=self.var_Division,font=("Arial Black",12,"bold"),state="readonly",width=15)
        self.Search_combo1["values"]=("Select","A","B","C","D")
        self.Search_combo1.current(0)
        self.Search_combo1.place(x=200,y=500,width=200)

        Search_label2=Label(f_lbl1,text="Class:",font=("Arial Black",12,"bold"),bg="red",fg="Black")
        Search_label2.place(x=0,y=450,width=200)

        self.Search_combo2=ttk.Combobox(f_lbl1,textvariable=self.var_Class,font=("Arial Black",12,"bold"),state="readonly",width=15)
        self.Search_combo2["values"]=("Select","1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th")
        self.Search_combo2.current(0)
        self.Search_combo2.place(x=200,y=450,width=200)
        
        b1_2=Button(f_lbl1,text="Save Data",command=self.save_data,font=("Arial Black",15,"bold"),bg="DARKGREEN",fg="white",cursor="hand2")
        b1_2.place(x=0,y=640,width=325,height=40)

        b1_3=Button(f_lbl1,text="Upload CSV",command=self.UpDrive,font=("Arial Black",15,"bold"),bg="DARKGREEN",fg="white",cursor="hand2")
        b1_3.place(x=325,y=640,width=325,height=40)

        b1_4=Button(f_lbl1,text="Delete CSV",command=self.delete_file,font=("Arial Black",15,"bold"),bg="DARKGREEN",fg="white",cursor="hand2")
        b1_4.place(x=325,y=600,width=325,height=40)

        b1_5=Button(f_lbl1,text="Annual Report",command=self.Annual_report,font=("Arial Black",15,"bold"),bg="DARKGREEN",fg="white",cursor="hand2")
        b1_5.place(x=0,y=600,width=325,height=40)
        
    #Attendance
    def mark_attendance(self,i,i1,i2,i3):
        now=datetime.now().strftime("%Y-%m-%d")
        conn=mysql.connector.connect(host="localhost",user="root",passwd="sai@1234",database="face_recognizer")
        my_cursor=conn.cursor()
        query=("select * from att_records where Subject=%s and Class=%s and Division=%s")
        value=(self.var_Subject.get(),self.var_Class.get(),self.var_Division.get(),)
        my_cursor.execute(query,value)
        myresult=my_cursor.fetchall()
        conn.commit()
        file_name_path="attendance_report/"+now+"_"+str(self.var_Class.get())+"_"+str(self.var_Division.get())+"_"+str(self.var_Subject.get())+".csv"
           
        
        with open(file_name_path,"r+",newline="\n") as f3:
            #writer=csv.writer(f)
            myDataList=f3.readlines()
            name_list=[]
            f3.write(str(self.var_Subject.get())+"  "+now+"  "+str(self.var_Class.get())+"  "+str(self.var_Division.get()))
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (i1 not in name_list) and (i2 not in name_list) and (i3 not in name_list)):
                now1=datetime.now()
                d1=now1.strftime("%Y/%m/%d")
                dtString=now1.strftime("%H:%M:%S")
                #writer.writerow(f"\n{i3},{i1},{i},{i2},{dtString},{d1},present")
                f3.writelines(f"\n{i3},{i1},{i},{i2},{dtString},{d1},present\n")

        '''try:
            headers = {"Authorization": "Bearer ya29.A0ARrdaM-9cUxnJEg63kXrcSml77ndO0X2XTmPTdWP7cNUIttHuuzzJGAeFnRPHRDER420dL9Tqa3pBVVFfT0cCow1YnQ67KtNVO4k3A1sGUFFNHxzifXGTntvDcpbDmqvzHHLv1AjaPeykjxgrPD_JRKtjzdQ"}
            para = {
                "name": "new.csv",
                "parents":["12npAMcHjWImfKQR16T92VDF8sCAl8W2z"]
                }
            files = {
                'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
                'file': open("./attendance_report/user"+str(self.var_Subject.get())+".csv", "rb")
            }
            r = requests.post(
                "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
                headers=headers,
                files=files
            )
            #print(r.text)
        except Exception:
            messagebox.showerror("Error","Connection Failed...",parent=self.root)'''
        
        '''with open(r"At.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (i1 not in name_list) and (i2 not in name_list) and (i3 not in name_list)):
                #now=datetime.now()
                d1=datetime.now().date()
                dtString=datetime.now().time()
                f.writelines(f"\n{i3},{i1},{i},{i2},{dtString},{d1},present")'''
        '''conn=mysql.connector.connect(host="localhost",user="root",passwd="sai@1234",database="face_recognizer")

        cursor = conn.cursor()
        csv_data = csv.reader(open('At.csv'))
        header = next(csv_data)

        for row in csv_data:
            print(row)
            cursor.execute(
                "INSERT INTO attendance (Student_ID,Roll,Name,Dep,time,date,attendance) VALUES (%s, %s, %s, %s,%s,%s,%s)", row)
        '''
        
        file_name_path1="attendance_realtime/"+now+"_"+str(self.var_Class.get())+"_"+str(self.var_Division.get())+"_"+str(self.var_Subject.get())+".csv"
        #f2=open(file_name_path1,'a+')
        with open(file_name_path1,"r+",newline="\n") as f:
            #writer=csv.writer(f)
            myDataList=f.readlines()
            name_list=[]
            f.write(str(self.var_Subject.get())+"  "+now+"  "+str(self.var_Class.get())+"  "+str(self.var_Division.get()))
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (i1 not in name_list) and (i2 not in name_list) and (i3 not in name_list)):
                now1=datetime.now()
                d1=now1.strftime("%Y/%m/%d")
                dtString=now1.strftime("%H:%M:%S")
                #writer.writerow(f"\n{i3},{i1},{i},{i2},{dtString},{d1},present")
                f.writelines(f"\n{i3},{i1},{i},{i2},{dtString},{d1},present\n")

    
    #FACE RECOGNITION

    def face_recog(self):
        if(self.txtSQA2==None):
            messagebox.showerror("Error","Enter Subject",parent=self.root)
        def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",passwd="sai@1234",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("Select Name from student where Student_ID="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("Select Roll from student where Student_ID="+str(id))
                i1=my_cursor.fetchone()
                i1="+".join(i1)

                my_cursor.execute("Select Dep from student where Student_ID="+str(id))
                i2=my_cursor.fetchone()
                i2="+".join(i2)

                my_cursor.execute("Select Student_ID from student where Student_ID="+str(id))
                i3=my_cursor.fetchone()
                i3="+".join(i3)

                if confidence>77:
                    cv2.putText(img,f"Student ID:{i3}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{i1}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{i2}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,i1,i2,i3)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            if cv2.waitKey(1) & 0xff==ord('q'):
                break
    
        video_cap.release()
        cv2.destroyAllWindows()
    def save_data(self):  
        conn=mysql.connector.connect(host="localhost",user="root",passwd="sai@1234",database="face_recognizer")
        my_cursor=conn.cursor()
        
        if(self.txtSQA2.get()=="Select"  or self.Search_combo2.get=="Select" or self.Search_combo1.get()=="Select"):
            messagebox.showerror("Error","Every Field IS Compulsory",parent=self.root)
        else: 
            now=datetime.now()
            messagebox.showinfo("Success","Successfully Saved",parent=self.root)
            conn=mysql.connector.connect(host="localhost",user="root",passwd="sai@1234",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into att_records values(%s,%s,%s,%s)",(
                                                                        self.var_sr_no.get(),
                                                                        self.var_Subject.get(),
                                                                        self.var_Class.get(),
                                                                        self.var_Division.get()
                                                                    ))

            conn.commit()
        

        #conn.close()
        
        
    def Export_To_Database():
        conn=mysql.connector.connect(host="localhost",user="root",passwd="sai@1234",database="face_recognizer")

        cursor = conn.cursor()
        csv_data = csv.reader(open('At.csv'))
        header = next(csv_data)

        for row in csv_data:
            print(row)
            cursor.execute(
                "INSERT INTO attendance (Student_ID,Roll,Name,Dep,time,date,attendance) VALUES (%s, %s, %s, %s,%s,%s,%s)", row)

        conn.commit()
        cursor.close()

    def UpDrive(self):
        now=datetime.now().strftime("%Y-%m-%d")
        try:
            gauth=GoogleAuth()
            drive=GoogleDrive(gauth)

            folder='1DavmIJvol9CFeWK-VeFGfitkwnkH2hCM'

            #file1=drive.CreateFile({'parents' :[{'id' :folder}],'title' :'new.csv'})
            #file1.FetchContent('./Attendance.csv')
            #file1.Upload()

            directory = 'C:/Users/Krunal/Downloads/face_recognition_system/face_recognition_system/attendance_realtime'
            for f in os.listdir(directory):
                filename = os.path.join(directory, f)
                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
                gfile.SetContentFile(filename)
                gfile.Upload()
        
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    def Annual_report(self):
        now=datetime.now().strftime("%Y-%m-%d")
        try:
            gauth=GoogleAuth()
            drive=GoogleDrive(gauth)

            folder='1XSMnDJTasAQiZ9CfZKyD0E4OJZLO_8u1'

            #file1=drive.CreateFile({'parents' :[{'id' :folder}],'title' :'new.csv'})
            #file1.FetchContent('./Attendance.csv')
            #file1.Upload()

            directory = 'C:/Users/Krunal/Downloads/face_recognition_system/face_recognition_system/attendance_report'
            for f in os.listdir(directory):
                filename = os.path.join(directory, f)
                gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
                gfile.SetContentFile(filename)
                gfile.Upload()
        
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    def delete_file(self):

        now=datetime.now().strftime("%Y-%m-%d")
        file_name_path1="attendance_realtime/"+now+"_"+str(self.var_Class.get())+"_"+str(self.var_Division.get())+"_"+str(self.var_Subject.get())+".csv"
        messagebox.showinfo("Success","Deleted "+now+"_"+str(self.var_Class.get())+"_"+str(self.var_Division.get())+"_"+str(self.var_Subject.get())+".csv")
        os.remove(file_name_path1)

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()