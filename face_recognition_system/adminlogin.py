from optparse import Values
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox

from matplotlib.pyplot import get
from Admin import Admin_Window
from main import Face_Recognition_System
import pyttsx3
import mysql.connector
from datetime import datetime




class adlog_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Login")
        self.root.wm_iconbitmap("Purple E-sports Illustrative Gaming and Technology Logo.ico")
        self.var_UserName=StringVar()
        self.var_Password=StringVar()
        self.var_Subject=StringVar()
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\di.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\295128.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        img1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        img1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="ADMIN LOGIN",font=("Arial Black",20,"bold"),bg="BLACK",fg="white")
        get_str.place(x=85,y=100)

        #label

        username=Label(frame,text="Username:",font=("Arial Black",13,"bold"),bg="BLACK",fg="white")
        username.place(x=60,y=155)

        self.txtuser=ttk.Entry(frame,textvariable=self.var_UserName,font=("Arial Black",13,"bold"))
        self.txtuser.place(x=20,y=190,width=300)

        password=Label(frame,text="Password:",font=("Arial Black",13,"bold"),bg="BLACK",fg="white")
        password.place(x=60,y=225)

        self.txtpass=ttk.Entry(frame,textvariable=self.var_Password,font=("Arial Black",13,"bold"))
        self.txtpass.place(x=20,y=260,width=300)
        self.txtpass.config(show='*')

        
        #Login Button
        lOGIN_btn=Button(frame,command=self.login,text="Login",width=15,height=1,font=("Arial Black",13,"bold"),bd=3,relief=RIDGE,bg="red",fg="white",activeforeground="white",activebackground="red")
        lOGIN_btn.place(x=110,y=410,width=120,height=35)

        lOGIN_btn=Button(frame,command=self.login,text="Login",width=15,height=1,font=("Arial Black",13,"bold"),bd=3,relief=RIDGE,bg="red",fg="white",activeforeground="white",activebackground="red")
        lOGIN_btn.place(x=110,y=410,width=120,height=35)

        
    


    def login(self):
        now=datetime.now()
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields Required")
        elif self.txtuser.get()=="ADMIN" and self.txtpass.get()=="ADMIN":
            self.new_window=Toplevel(self.root)
            self.app=Admin_Window(self.new_window)
           

if __name__=="__main__":
    root=Tk()
    app=adlog_Window(root)
    root.mainloop()
