from ssl import Purpose
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from phonenumbers import is_alpha_number
import pyttsx3
from FRAMS import Login_Window
from prelogin import Prelogin_Window

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        self.root.wm_iconbitmap("Purple E-sports Illustrative Gaming and Technology Logo.ico")


        #text VAriables
        self.var_fname=StringVar()
        self.var_Lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        self.var_UserName=StringVar()
        self.var_Password=StringVar()
        self.var_Subject=StringVar()
        self.var_TeacherName=StringVar()
    


        img=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\hackers2.jpg")
        img=img.resize((1517,765),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=5,y=50,width=1517,height=765)

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\clock.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=50,y=140,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=140,width=800,height=550)
        
        get_str=Label(frame,text="REGISTER HERE",font=("Arial Black",20,"bold"),fg="darkgreen",bg="white")
        get_str.place(x=20,y=20)

        fname=Label(frame,text="First Name:",font=("Arial Black",15,"bold"),bg="White")
        fname.place(x=50,y=60)

        self.txtfname=ttk.Entry(frame,textvariable=self.var_fname,font=("Arial Black",15,"bold"))
        self.txtfname.place(x=50,y=90,width=300)

        Lname=Label(frame,text="Last Name:",font=("Arial Black",15,"bold"),bg="White")
        Lname.place(x=450,y=60)
        
        #Purp=Label(frame,text="Purpose:",font=("Arial Black",15,"bold"),bg="White")
        #Purp.place(x=450,y=140)
        #depSQ1_combo=ttk.Combobox(frame,font=("Arial Black",15,"bold"),state="readonly",width=21)
        #depSQ1_combo["values"]=("Select","School/College","Organization","Corporate","Others")
        #depSQ1_combo.current(0)
        #depSQ1_combo.place(x=450,y=170)

        self.txtLname=ttk.Entry(frame,textvariable=self.var_Lname,font=("Arial Black",15,"bold"))
        self.txtLname.place(x=450,y=90,width=300)

        contact=Label(frame,text="Mobile No.:",font=("Arial Black",15,"bold"),bg="White")
        contact.place(x=50,y=140)

        self.txtcontact=ttk.Entry(frame,textvariable=self.var_contact,font=("Arial Black",15,"bold"))
        self.txtcontact.place(x=50,y=170,width=300)

        email=Label(frame,text="Email:",font=("Arial Black",15,"bold"),bg="White")
        email.place(x=450,y=140)

        self.txtemail=ttk.Entry(frame,textvariable=self.var_TeacherName,font=("Arial Black",15,"bold"))
        self.txtemail.place(x=450,y=170,width=300)

        SQ=Label(frame,text="Select Security Question:",font=("Arial Black",15,"bold"),bg="White")
        SQ.place(x=50,y=220)

        depSQ_combo=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Arial Black",15,"bold"),state="readonly",width=21)
        depSQ_combo["values"]=("Select","Birth Place","Favourite City","Pet Name","Favourite Car","Favourite Actor","Favourite Actress")
        depSQ_combo.current(0)
        depSQ_combo.place(x=50,y=250)

        SQA=Label(frame,text="Security Answer:",font=("Arial Black",15,"bold"),bg="White")
        SQA.place(x=450,y=220)

        self.txtSQA=ttk.Entry(frame,textvariable=self.var_securityA,font=("Arial Black",15,"bold"))
        self.txtSQA.place(x=450,y=250,width=300)

        SQA1=Label(frame,text="Username:",font=("Arial Black",15,"bold"),bg="White")
        SQA1.place(x=50,y=300)

        self.txtSQA1=ttk.Entry(frame,textvariable=self.var_UserName,font=("Arial Black",15,"bold"))
        self.txtSQA1.place(x=50,y=330,width=300)

        SQA3=Label(frame,text="Must be alphanumeric:",font=("Arial Black",7,"bold"),bg="White")
        SQA3.place(x=50,y=290)

        SQA2=Label(frame,text="Subject:",font=("Arial Black",15,"bold"),bg="White")
        SQA2.place(x=450,y=300)

        self.txtSQA2=ttk.Entry(frame,textvariable=self.var_Subject,font=("Arial Black",15,"bold"))
        self.txtSQA2.place(x=450,y=330,width=300)

        Password=Label(frame,text="Password:",font=("Arial Black",15,"bold"),bg="White")
        Password.place(x=50,y=370)

        self.txtPassword=ttk.Entry(frame,textvariable=self.var_pass,font=("Arial Black",15,"bold"),show="*")
        self.txtPassword.place(x=50,y=400,width=300)

        Password1=Label(frame,text="1.Must Contain Atleast 1 Uppercase,Lowercase,Number and Special Character!",font=("Arial Black",7,"bold"),bg="White")
        Password1.place(x=50,y=440)

        Password2=Label(frame,text="2.Minimum Length must be 6",font=("Arial Black",7,"bold"),bg="White")
        Password2.place(x=50,y=455)

        Cpass=Label(frame,text="Confirm Password:",font=("Arial Black",15,"bold"),bg="White")
        Cpass.place(x=450,y=370)

        self.txtCpass=ttk.Entry(frame,textvariable=self.var_confpass,font=("Arial Black",15,"bold"),show="*")
        self.txtCpass.place(x=450,y=400,width=300)


        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Condition",font=("Arial Black",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=470)

        #buttons'
        img5=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\register-now-button1.jpg")
        img5=img5.resize((200,55),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        save_btn=Button(frame,image=self.photoimg5,command=self.register_data,borderwidth=0,cursor="hand2")
        save_btn.place(x=50,y=500,width=200)

        img6=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\loginpng.png")
        img6=img6.resize((200,45),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        save1_btn=Button(frame,image=self.photoimg6,command=self.Login,borderwidth=0,cursor="hand2")
        save1_btn.place(x=525,y=500,width=200)
        
        
    
    #Function Declaration

    def register_data(self):
        a=self.var_UserName.get().isalnum()
        b=self.var_Password.get().isalnum()
        if self.var_fname.get()=="" or self.var_contact.get=="" or self.var_email.get=="" or self.var_securityA.get=="" or self.var_Lname.get=="" or self.var_UserName.get()=="" or self.var_securityQ.get()=="Select" or self.var_confpass=="" or self.var_Subject=="":
            messagebox.showerror("Error","All fields are required")
        elif len(self.var_pass.get())<5:
            messagebox.showerror("Error","Password should be of Mininum 6 characters")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please click on agree terms and conditions")
        #elif a==False:
        #    messagebox.showerror("Error","Username Must Contain Characters,Numbers and Special Characters")
        #elif b==False:
        #    messagebox.showerror("Error","Password Must Contain Characters,Numbers and Special Characters")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",passwd="sai@1234",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where username=%s")
            value=(self.var_UserName.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist")
            if row==None:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                       self.var_Lname.get(),
                                                                                       self.var_contact.get(),
                                                                                       self.var_securityQ.get(),
                                                                                       self.var_securityA.get(),
                                                                                       self.var_pass.get(),
                                                                                       self.var_UserName.get(),
                                                                                       self.var_Subject.get(),
                                                                                       self.var_TeacherName.get()
                                                                                       ))
                messagebox.showinfo("success","Registered Successfully") 
            conn.commit()
            
             
            
            
    def Login(self):
        self.new_window=Toplevel(self.root)
        self.app=Prelogin_Window(self.new_window)
    






if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()