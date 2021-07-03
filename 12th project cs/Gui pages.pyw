from tkinter import *
import threading
import sql_manager as ss

def temp(er,s):
            er.destroy()
            s.sperson()
def temp2(er,s):
    er.destroy()
    s.w.destroy()
def close_w(self):
    self.w.destroy()

class GUI:
    def __init__(self):
        self.w=Tk()
        p1 = PhotoImage(file = 'logo.png')
        self.w.iconphoto(True, p1)
        self.w.withdraw()

        self.welcome=Toplevel()
        self.welcome.title("WELCOME")
        self.welcome.configure(width=400,height=400)

        photo= PhotoImage(file = "logo.png")

        l=Label(self.welcome,image=photo)
        l.place(relheight=0.8,relwidth=1)

        lb=Label(self.welcome,text = "Welcome to CHATROOM \n -by JATIN YADAV",font="ALGERIAN 20 bold")
        lb.place(relheight=0.2,relwidth=1,rely=0.8)

        thread1=threading.Thread(target=self.y)
        thread1.start()

        self.login=Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=400)

        self.t=Label(self.login,text = "Login to continue",font="Arial 20 bold")
        self.t.place(relheight=0.15,relx=0.2,rely=0.001)

        self.uidlabel=Label(self.login,text="UID : ",font="Helvetica 12")
        self.uidlabel.place(relheight=0.2,relx=0.1,rely=0.1)

        self.uidentry=Entry(self.login,font="Helvetica 14")
        self.uidentry.place(relheight=0.1,relwidth=0.5,relx=0.4,rely=0.15)

        self.passwordlabel=Label(self.login,text="PASSWORD : ",font="Helvetica 12")
        self.passwordlabel.place(relheight=0.2,relx=0.1,rely=0.26)
        
        self.passwordentry=Entry(self.login,font="Helvetica 14")
        self.passwordentry.place(relheight=0.1,relwidth=0.5,relx=0.4,rely=0.3)

        self.next = Button(self.login,text = "LOGIN",font = "Helvetica 14 bold",bg="red",  \
                           command = lambda: self.Next(self.uidentry.get(),self.passwordentry.get()))
        self.next.place(relheight=0.2,relwidth=0.6,relx=0.25,rely=0.6)

        self.login.protocol("WM_DELETE_WINDOW",lambda : close_w(self))

        self.login.withdraw()
        
       
        self.w.mainloop()

    def y(self):
        def fo():
            self.welcome.destroy()
            self.login.deiconify()

        WAIT_TIME_SECONDS = 3

        ticker = threading.Event()
        if not ticker.wait(WAIT_TIME_SECONDS):
            fo()


    def Next(self,uid,password):
        self.login.destroy()
        self.uid=uid
        self.password=password
        c=ss.entrycheck(uid,password)
        if c:
            self.sperson()
        else:
            err2=Toplevel()
            err2.title("ERROR")
            
            err2.resizable(width=False,height=False)
            err2.configure(width=800,height=200)
            
            e=Label(err2,text = "ERROR \n YOUR DATA DOESN'T EXIST",font="Arial 30 bold")
            e.place(relwidth=1,relheight=0.8)

            ext2 = Button(err2,text ="EXIT",font = "Helvetica 14 bold",bg="red", \
                          command=lambda : temp2(err2,self))
            ext2.place(relheight=0.2,relwidth=1,rely=0.8)

            err2.protocol("WM_DELETE_WINDOW",lambda : close_w(self))

         
        
    def sperson(self):
        self.sp=Toplevel()
        self.sp.title("RECEIVER DETAILS")

        self.sp.resizable(width=False,height=False)
        self.sp.configure(width=400,height=400)

        self.st=Label(self.sp,text = "Enter receivers details",font="Arial 20 bold")
        self.st.place(relheight=0.15,relx=0.2,rely=0.001)

        self.uidlabel2=Label(self.sp,text="UID : ",font="Helvetica 12")
        self.uidlabel2.place(relheight=0.2,relx=0.1,rely=0.1)
        
        self.uidentry2=Entry(self.sp,font="Helvetica 14")
        self.uidentry2.place(relheight=0.1,relwidth=0.5,relx=0.4,rely=0.15)
        
        self.next2 = Button(self.sp,text = "NEXT",font = "Helvetica 14 bold",bg="red",  \
                            command = lambda: self.Next2(self.uidentry2.get()))
        self.next2.place(relheight=0.2,relwidth=0.6,relx=0.25,rely=0.6)

        self.sp.protocol("WM_DELETE_WINDOW",lambda : close_w(self))

    def Next2(self,uid):
        
        self.sp.destroy()
        self.uid2=uid
        c=ss.check2(uid)
        if c:
            self.layout()
           
        else:
            err2=Toplevel()
            err2.title("ERROR")

            err2.resizable(width=False,height=False)
            err2.configure(width=800,height=200)

            e=Label(err2,text = "ERROR \n THIS USER DOESN'T EXIST",font="Arial 30 bold")
            e.place(relwidth=1,relheight=0.8)

            ext2 = Button(err2,text ="BACK",font = "Helvetica 14 bold",bg="red", \
                          command=lambda : temp(err2,self))
            ext2.place(relheight=0.2,relwidth=1,rely=0.8)        

            err2.protocol("WM_DELETE_WINDOW",lambda : close_w(self))  


    def layout(self):
        self.sname=ss.fetch_name(self.uid)
        self.rname=ss.fetch_name(self.uid2)  

        self.w.deiconify()
        self.w.title("CHATROOM | JATIN YADAV")

        self.w.configure(width=800,height=750,bg="gray27")
        self.Headframe=Frame(self.w, width=800,height=37.5,bg="gray27")
        self.Headframe.place(relwidth=1,relx=0,rely=0)

        sender_label=Label(self.Headframe,text="SENDER : "+self.sname,width=150, \
                           font="arial 16 bold",height=37,bg="SteelBlue3")
        sender_label.place(relx=0.01,rely=0.01,relheight=0.9,relwidth=0.3)

        reciver_label=Label(self.Headframe,text="RECIVER : "+self.rname,width=150, \
                            font="arial 16 bold",height=37,bg="SteelBlue3")
        reciver_label.place(relx=0.65,rely=0.01,relheight=1,relwidth=0.3)

        self.historybutton=Button(self.w,text="CHAT HISTORY",font="arial 16 bold", \
                                  bg="lime green",command=lambda : self.history())
        self.historybutton.place(relheight=0.04,relwidth=0.4,relx=0.25,rely=0.06)

        self.textconsole=Text(self.w,width=30,height=5,bg="black",fg="white", \
                              font="Courier 14")
        self.textconsole.place(relwidth=0.95,relheight=0.7,rely=0.1)

        scrollbar=Scrollbar(self.textconsole)
        scrollbar.place(relheight=1,relx=0.97)
        scrollbar.config(command=self.textconsole.yview)

        self.bottomframe=Frame(self.w,width=800,height=140,bg="gray27")
        self.bottomframe.place(relwidth=1,rely=0.81)

        self.msgtxt=Text(self.bottomframe,width=30,height=5,bg="aquamarine",font="arial 14")
        self.msgtxt.place(relwidth=0.7,relheight=0.98,rely=0.01,relx=0.01)

        self.sendbutton=Button(self.bottomframe,text="SEND",font="arial 16 bold", \
                               bg="lime green",command=lambda : self.sendmsg(self.msgtxt.get("0.1","end-1c")))
        self.sendbutton.place(relheight=0.9,relwidth=0.2,relx=0.75,rely=0.01)

        self.textconsole.config(cursor = "arrow") 
        self.textconsole.config(state='disable')
        
        thread=threading.Thread(target=self.x)
        thread.start()
            
            
       
    def sndbutton(self,msg):
        snd=threading.Thread(target=self.sendmsg,args=(msg,))
        snd.start()

    def x(self):
        def foo():
            self.recmsg()
        
        WAIT_TIME_SECONDS = 1

        ticker = threading.Event()
        while not ticker.wait(WAIT_TIME_SECONDS):
            foo()

    def sendmsg(self,msg):
        self.textconsole.config(state='normal')
        self.textconsole.insert(END,self.sname+"->"+msg+"\n") 
        self.textconsole.config(state='disable')
        self.msgtxt.delete('1.0',END)

        ss.postmsg(msg)

    def recmsg(self):
        msglist=ss.getmsg()
        if len(msglist)!=0:
            self.textconsole.config(state='normal')
            for i in msglist:
                self.textconsole.insert(END,self.rname+"->"+i+"\n")
            self.textconsole.config(state='disable')
        else :
            pass

    def history(self):
        self.chathist=Toplevel()
        self.chathist.title("CHAT HISTORY")
        self.chathist.configure(width=400,height=400)
        messages_list=ss.getmessages()

        textconsole=Text(self.chathist,width=30,height=5,bg="black",fg="white")
        textconsole.place(relwidth=0.95,relheight=0.7,rely=0.1)

        for i in messages_list:
            textconsole.insert(END,ss.fetch_name(i[0])+"->"+i[1]+"\n")
        textconsole.config(state='disable')
        textconsole.config(cursor = "arrow")
        
        scrollbar=Scrollbar(textconsole)
        scrollbar.place(relheight=1,relx=0.97)
        scrollbar.config(command=textconsole.yview)
              

g=GUI()
