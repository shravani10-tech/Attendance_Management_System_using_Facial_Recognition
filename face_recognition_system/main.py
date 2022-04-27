from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from help import Help
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter
from datetime import datetime
from time import strftime
from chatbot import ChatBot
import pyttsx3




class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
        self.root.wm_iconbitmap("Purple E-sports Illustrative Gaming and Technology Logo.ico")

        

        #IMG1
        img=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\pg3.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #IMG2
        img1=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\pg3.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #IMG3
        img2=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\pg1.png")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg image
        img3=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\1.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="Teacher Name:DEMO",font=("Algerian",25,"bold"),bg="dark grey",fg="Black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=("Algerian",13,"bold"),bg="dark grey",fg="black")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #detect Face
        img5=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\face-id.png")
        img5=img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",font=("Arial Black",15,"bold"),bg="green",fg="white",cursor="hand2",command=self.face_data)
        b1_1.place(x=200,y=300,width=220,height=40)

        #Attendance
        img6=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\immigration.png")
        img6=img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=650,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",font=("Arial Black",15,"bold"),bg="green",fg="white",cursor="hand2",command=self.attendance_data)
        b1_1.place(x=650,y=300,width=220,height=40)

        #CHATBOT
        img7=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\chatbot.png")
        img7=img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.chatbot)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="FRAMIE",command=self.chatbot,font=("Arial Black",15,"bold"),bg="green",fg="white",cursor="hand2")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #Developer
        img10=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\coding.png")
        img10=img10.resize((180,180),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=420,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("Arial Black",15,"bold"),bg="green",fg="white")
        b1_1.place(x=420,y=580,width=220,height=40)

        #Exit
        img11=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\power.png")
        img11=img11.resize((150,150),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=880,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",font=("Arial Black",15,"bold"),bg="green",fg="white",cursor="hand2",command=self.iExit)
        b1_1.place(x=880,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    #Function Buttons

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    #def Help_data(self):
        #self.new_window=Toplevel(self.root)
        #self.app=Help(self.new_window)
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
    def chatbot(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)
    



if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()