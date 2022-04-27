from optparse import Values
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox

from matplotlib.pyplot import get
from main import Face_Recognition_System
import pyttsx3
import mysql.connector
from datetime import datetime
from FRAMS import Login_Window
from Admin import Admin_Window
from adminlogin import adlog_Window



class Prelogin_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Login")
        self.root.wm_iconbitmap("Purple E-sports Illustrative Gaming and Technology Logo.ico")
        
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

        get_str=Label(frame,text="Get Started",font=("Arial Black",20,"bold"),bg="BLACK",fg="white")
        get_str.place(x=85,y=100)
        
        #Login Button
        Admin_btn=Button(frame,command=self.adminlogin,text="Admin Login",width=15,height=1,font=("Arial Black",30,"bold"),bd=3,relief=RIDGE,bg="red",fg="white",activeforeground="white",activebackground="red")
        Admin_btn.place(x=0,y=270,width=340,height=70)

        lOGIN_btn=Button(frame,command=self.userlogin,text="User Login",width=15,height=1,font=("Arial Black",30,"bold"),bd=3,relief=RIDGE,bg="red",fg="white",activeforeground="white",activebackground="red")
        lOGIN_btn.place(x=0,y=380,width=340,height=70)

        

        
    def userlogin(self):
        self.new_window=Toplevel(self.root)
        self.app=Login_Window(self.new_window)
        #messagebox.showinfo("Success","Login To Continue")
        
    def adminlogin(self):
        self.new_window=Toplevel(self.root)
        self.app=adlog_Window(self.new_window)
        #messagebox.showinfo("Success","Login To Continue")

if __name__=="__main__":
    root=Tk()
    app=Prelogin_Window(root)
    root.mainloop()
    #root.destroy()