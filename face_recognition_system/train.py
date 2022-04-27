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
import pyttsx3

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
        self.root.wm_iconbitmap("Purple E-sports Illustrative Gaming and Technology Logo.ico")

        

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("Algerian",35,"bold"),bg="light grey",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\facialrecognition.png")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)
          
        #Button  
        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,font=("Arial Black",30,"bold"),bg="RED",fg="white",cursor="hand2")
        b1_1.place(x=0,y=380,width=1530,height=60)

        #img_bottom=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\college_images\opencv_face_reco_more_data.jpg")
        #img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        #self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        #f_lbl=Label(self.root,image=self.photoimg_bottom)
        #f_lbl.place(x=0,y=440,width=1530,height=325)
    
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')#Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #Train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets Completed!!")

            
        

        



if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()