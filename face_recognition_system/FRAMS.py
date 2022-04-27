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




class Login_Window:
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

        get_str=Label(frame,text="Get Started",font=("Arial Black",20,"bold"),bg="BLACK",fg="white")
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

        #Subject=Label(frame,text="Subject:",font=("Arial Black",13,"bold"),bg="BLACK",fg="white")
        #Subject.place(x=60,y=289)

        #self.Subject=ttk.Entry(frame,textvariable=self.var_Subject,font=("Arial Black",13,"bold"))
        #self.Subject.place(x=20,y=320,width=308)

        #TeacherName=Label(frame,text="Teacher Name:",font=("Arial Black",13,"bold"),bg="BLACK",fg="white")
        #TeacherName.place(x=60,y=350)

        #self.txtTN=ttk.Entry(frame,textvariable=self.var_TeacherName,font=("Arial Black",13,"bold"))
        #self.txtTN.place(x=20,y=380,width=300)

        #Icon Images
        #img3=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\LoginIconAppl.png")
        #img3=img3.resize((25,25),Image.ANTIALIAS)
        #self.photoimage3=ImageTk.PhotoImage(img3)
        #img3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        #img3.place(x=640,y=330,width=25,height=25)

        #img2=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\lock-512.png")
        #img2=img2.resize((25,25),Image.ANTIALIAS)
        #self.photoimage2=ImageTk.PhotoImage(img2)
        #img2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        #img2.place(x=640,y=400,width=25,height=25)
        
        #Login Button
        lOGIN_btn=Button(frame,command=self.login,text="Login",width=15,height=1,font=("Arial Black",13,"bold"),bd=3,relief=RIDGE,bg="red",fg="white",activeforeground="white",activebackground="red")
        lOGIN_btn.place(x=110,y=410,width=120,height=35)

    def login(self):
        now=datetime.now()
        conn=mysql.connector.connect(host="localhost",user="root",passwd="sai@1234",database="face_recognizer")
        my_cursor=conn.cursor()
        query=("select * from register where username=%s and password=%s")
        value=(self.var_UserName.get(),self.var_Password.get())
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields Required")
        elif self.txtuser.get()=="Team FRAMS" and self.txtpass.get()=="ASRK":
            messagebox.showinfo("Success","welcome to FRAMS")
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition_System(self.new_window)
        elif(str(self.txtuser.get()) and str(self.txtpass.get())in row):
            messagebox.showinfo("Success","Welcome To FRAMS",parent=self.root)
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition_System(self.new_window)
            conn=mysql.connector.connect(host="localhost",user="root",passwd="sai@1234",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into login_det values(%s,%s,%s)",(
                                                                            self.var_UserName.get(),
                                                                            self.var_Password.get(),
                                                                            now
                                                                            ))
            conn.commit()
            conn.close()
        else:
            messagebox.showerror("Error","Wrong Credentials!!",parent=self.root)
                
            
                
                

    def fetch_data(self): 
        conn=mysql.connector.connect(host="localhost",user="root",passwd="sai@1234",database="face_recognizer")
        my_cursor=conn.cursor()  
        my_cursor.execute("select * from login_det")
        data=my_cursor.fetchall()
            


if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()