from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import pyttsx3


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_function)
        self.root.wm_iconbitmap("Purple E-sports Illustrative Gaming and Technology Logo.ico")

        


        main_frame=Frame(self.root,bd=4,bg="black",width=610)
        main_frame.pack()

        img_chat=Image.open(r"C:\Users\Krunal\Downloads\face_recognition_system\face_recognition_system\college_images\chat.jpg")
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoImg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor="nw",width=870,compound=LEFT,image=self.photoImg,text="FRAMIE",font=("Algerian",25,"bold"),fg="Black",bg="white")
        Title_label.pack(side=TOP)
        
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=("arial black",14,"bold"),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bd=4,bg="light grey",width=730)
        btn_frame.pack()

        label=Label(btn_frame,text="Type Something",font=("arial black",14,"bold"),fg="green",bg="light grey")
        label.grid(row=0,column=0,padx=5,sticky=W)
        
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=30,font=("arial black",14,"bold"))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send=>",command=self.send,font=("arial black",15,"bold"),width=8,bg="green")
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.cleadata=Button(btn_frame,command=self.clear,text="Clear Data",font=("arial black",15,"bold"),width=9,bg="red",fg="white")
        self.cleadata.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label1=Label(btn_frame,text=self.msg,font=("arial black",14,"bold"),fg="red",bg="white")
        self.label1.grid(row=1,column=1,padx=5,sticky=W)


    #function declaration
    def enter_function(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg="Please Enter Some Input"
            self.label1.config(text=self.msg,fg='red')
        else:
            self.msg=""
            self.label1.config(text=self.msg,fg='red')

        if(self.entry.get()=='hello' or self.entry.get()=='Hello' or self.entry.get()=='HELLO' or self.entry.get()=='hii' or self.entry.get()=='Hii'):
            self.text.insert(END,'\n\n'+'Bot: Hi')
        
        elif(self.entry.get()=='hi' or self.entry.get()=='Hi' or self.entry.get()=='HI'):
            self.text.insert(END,'\n\n'+'Bot: Hello')

        elif(self.entry.get()=='How Are You' or self.entry.get()=='Wassup' or self.entry.get()=='How you are doing?'):
            self.text.insert(END,'\n\n'+'Bot: I am Good and You?')
        
        #elif(self.entry.get()=='How Are You' or self.entry.get()=='how are you' or self.entry.get()=='How Are u' or self.entry.get()=='how are u' or self.entry.get()=='How are you' or self.entry.get()=='How are you?' or self.entry.get()=='How Are You?' or self.entry.get()=='how are you?' or  self.entry.get()=='how are u?' or self.entry.get()=='how are U?' or self.entry.get()=='How are u?'):
            #self.text.insert(END,'\n\n'+'Bot: I am Good and You?')

        elif(self.entry.get()=='Fanatic' or self.entry.get()=='Good' or self.entry.get()=='Perfect' or self.entry.get()=='fanatic' or self.entry.get()=='good' or self.entry.get()=='perfect'):
            self.text.insert(END,'\n\n'+'Bot: Nice To Hear That')

        elif(self.entry.get()=='You are created by?' or self.entry.get()=='Who is your Creater' or self.entry.get()=='You are invention of?'):
            self.text.insert(END,'\n\n'+'Bot: Team FRAMS Did it using Python')
        
        elif(self.entry.get()=='Can you speak any other language'):
            self.text.insert(END,'\n\n'+'Bot: I am still Learning...')
        
        elif(self.entry.get()=='What is machine Learning?' or self.entry.get()=='what is machine learning?' or self.entry.get()=='What is Machine Learning?' or self.entry.get()=='What Is Machine Learning?' or self.entry.get()=='WHAT IS MACHINE LEARNING?'):
            self.text.insert(END,'\n\n'+'Bot: Machine learning is a branch of artificial intelligence (AI) \n and computer science which focuses on the use of data \n and algorithms to imitate the way that humans learn, \n gradually improving its accuracy.')
        
        elif(self.entry.get()=='How does face recognition work?'):
            self.text.insert(END,'\n\n'+'Bot: Facial recognition is a way of recognizing \n a human face through technology. \n A facial recognition system uses biometrics to \n map facial features from a photograph or video. \n It compares the information with a database of known faces to \n find a match.')
        
        elif(self.entry.get()=='How many countries use facial recogition?'):
            self.text.insert(END,'\n\n'+'Bot: There are 109 countries today that \n are either using or have approved \n the use of facial recognition technology for \n surveillance purposes.')
        
        elif(self.entry.get()=='What is python programming?'):
            self.text.insert(END,'\n\n'+'Bot: Python is an interpreted, object-oriented, \n high-level programming language with dynamic semantics. Its high-level \n built in data structures, combined with dynamic typing and \n dynamic binding, make it very attractive for Rapid \n Application Development, as well as for use as a \n scripting or glue language to connect existing components together. ')
        
        elif(self.entry.get()=='What is chatbot?'):
            self.text.insert(END,'\n\n'+'Bot: At the most basic level, a chatbot is a computer program \n that simulates and processes human conversation \n (either written or spoken), allowing humans to interact with digital \n devices as if they were communicating with a real person')
        
        elif(self.entry.get()=='Bye'):
            self.text.insert(END,'\n\n'+'Bot: Have A Good Day :)')
        elif(self.entry.get()=='Get me in touch' or self.entry.get()=='Contact developers' or self.entry.get()=='Help'):
            self.text.insert(END,'\n\n'+'teamframs@vit.edu.in')

        else:
            self.text.insert(END,'\n\n'+"Bot: Sorry I didn't get it")
        


if __name__=="__main__":
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()