from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
from PIL import ImageTk,Image
con=sql.connect(host="localhost",user="root",passwd="nihal2692")
cur=con.cursor()
#DEFAULT SQL QUERY

cur.execute("create database if not exists naira")
cur.execute("use naira")
cur.execute("drop table if exists movies")
cur.execute("drop table if exists admin")
cur.execute("create table if not exists user(username varchar(50),city varchar(20),email varchar(30),password varchar(20))")
cur.execute("create table if not exists movies(movies varchar(50),hall varchar(20),date varchar(20),charges int)")
cur.execute("create table if not exists admin(admin varchar(20),password varchar(20))")
cur.execute("insert into movies values('GOLD','N1','07-01-2023',180),('AVATAR','N2','07-01-2023',180),('CHERNOBYL','N3','07-01-2023',180),('VARISU','N4','07-01-2023',180),('KGF-2','N5','07-01-2023',180)")
cur.execute("insert into admin values('sreeram','sreeram'),('nihal','nihal'),('s','s')")
con.commit()

def loginwin():
    global base
    base=Tk()
    base.geometry("1423x800")
    img=Image.open("LOGIN PAGE.png")
    myimg=ImageTk.PhotoImage(img)
    imglabel=Label(image=myimg)
    imglabel.place(x=0,y=0)

    text1=Label(base,text="Username:",font=("Arial",17),fg="black").place(x=900,y=290)
    box1=Entry(base,font=('Arial 15'))
    box1.place(x=1035,y=292)

    text2=Label(base,text="Password:",font=("Arial",17),fg="black").place(x=905,y=340)
    box2=Entry(base,font=('Arial 15'))
    box2.place(x=1035,y=342)

    button1=Button(base,text="Enter",font=("Arial",13),fg="black",command=lambda:login(box1.get(),box2.get())).place(x=990,y=410)

    button2=Button(base,text="Signup",font=("Arial",13),fg="blue",command=lambda:signupwin()).place(x=1100,y=410)
    button3=Button(base,text="Admin",font=("Arial",13),fg="red",command=lambda:adminpage()).place(x=1200,y=410)
    button5=Button(base,text="QUIT",font=("Arial",13),command=lambda:quitmain1()).place(x=1350,y=750)
    base.mainloop()

def adminpage():
    global base,base
    base.destroy()
    base=Tk()
    base.geometry("1423x800")
    img=Image.open("LOGIN PAGE.png")
    myimg=ImageTk.PhotoImage(img)
    imglabel=Label(image=myimg)
    imglabel.place(x=0,y=0)

    text1=Label(base,text="Username:",font=("Arial",17),fg="black").place(x=900,y=290)
    box1=Entry(base,font=('Arial 15'))
    box1.place(x=1035,y=292)

    text2=Label(base,text="Password:",font=("Arial",17),fg="black").place(x=905,y=340)
    box2=Entry(base,font=('Arial 15'))
    box2.place(x=1035,y=342)

    button1=Button(base,text="Enter",font=("Arial",13),fg="black",command=lambda:admin(box1.get(),box2.get())).place(x=990,y=410)
    button3=Button(base,text="User",font=("Arial",13),fg="blue",command=lambda:returnuser()).place(x=1100,y=410)
    button5=Button(base,text="QUIT",font=("Arial",13),command=lambda:quitmain1()).place(x=1350,y=750)
    base.mainloop()

def returnuser():
    global base,base
    base.destroy()
    loginwin()
    
def login(v1,v2):
    cur.execute("select username,password from user")
    l=cur.fetchall()
    c=0
    for i in l:
        if v1.lower() and v2.lower() in i:
            messagebox.showinfo("done","Login Completed")
            c=c+1
            base.destroy()
            bookingwin()
            break
    if c==0:
        messagebox.showerror("Login Failed!","Invalid User Infromation")
        signupwin()

def admin(v1,v2):
    cur.execute("select admin,password from admin")
    l=cur.fetchall()
    c=0
    for i in l:
        if v1.lower() and v2.lower() in i:
            messagebox.showinfo("done","Admin Login Completed")
            c=c+1
            base.destroy()
            adminwin()
            break
    if c==0:
        messagebox.showerror("Admin Login Failed!","Invalid Admin Infromation")

def signupwin():
    global base
    global base
    base.destroy()
    base=Tk()
    base.geometry("1423x800")
    img=Image.open("LOGIN PAGE.png")
    myimg=ImageTk.PhotoImage(img)
    imglabel=Label(image=myimg)
    imglabel.place(x=0,y=0)
    text1=Label(base,text="Username:",font=("Arial",17)).place(x=894,y=290)
    box1=Entry(base,font=('Arial 15'))
    box1.place(x=1035,y=292)
    text2=Label(base,text="Password:",font=("Arial",17)).place(x=900,y=330)
    box2=Entry(base,font=('Arial 15'))
    box2.place(x=1035,y=332)
    text3=Label(base,text="Email:",font=("Arial",17)).place(x=946,y=370)
    box3=Entry(base,font=('Arial 15'))
    box3.place(x=1035,y=372)
    text3=Label(base,text="City:",font=("Arial",17)).place(x=962,y=410)
    box4=Entry(base,font=('Arial 15'))
    box4.place(x=1035,y=412)

    button1=Button(base,text="Enter",font=("Arial",13),fg="black",command=lambda:signup(box1.get().lower(),box2.get().lower(),box3.get().lower(),box4.get().lower())).place(x=1060,y=454)
    base.mainloop()
    
def delete(m):
    print(m)
    cur.execute("select movies from movies")
    s=cur.fetchall()
    v=s[m]
    for i in v:
        c=i
    print(c)
    cur.execute("delete from movies where movies='{}'".format(c))
    con.commit()

def insert():
    global box1,box2,box3,box4,name,date,hall,p,price
    text=Label(base,text="INSERT MOVIE DETAILS",font=("Arial",20),bg="black",fg="white").place(x=550,y=400)
    text1=Label(base,text="Enter Movie Name:",font=("Arial",15),bg="black",fg="white").place(x=200,y=475)
    box1=Entry(base,font=("Arial,14"))
    box1.place(x=425,y=475)
    text2=Label(base,text="Enter Screen Name:",font=("Arial",15),bg="black",fg="white").place(x=200,y=525)
    box2=Entry(base,font=("Arial,14"))
    box2.place(x=425,y=525)
    text3=Label(base,text="Enter Date:",font=("Arial",15),bg="black",fg="white").place(x=200,y=575)
    box3=Entry(base,font=("Arial,14"))
    box3.place(x=425,y=575)
    text4=Label(base,text="Enter Ticket Price:",font=("Arial",15),bg="black",fg="white").place(x=200,y=625)
    box4=Entry(base,font=("Arial,14"))
    box4.place(x=425,y=625)


    button1=Button(base,text="Enter",font=("Arial",15),fg="white",bg="black",command=lambda:insertsuc()).place(x=450,y=675)
def insertsuc():
    name=box1.get()
    hall=box2.get()
    date=box3.get()
    price=box4.get()
    cur.execute("insert into movies values('{}','{}','{}','{}')".format(name,hall,date,price))
    con.commit()
    cur.execute("select movies from movies")
    c=cur.fetchall()
    print(c)
    text1=Label(base,text="Insertion Successful. Reload page to see result",font=("Arial",20),bg="black",fg="white").place(x=750,y=500)


def reload():
    global base
    base.destroy()
    adminwin()

def adminwin():
    global base
    base=Tk()
    base.geometry("1423x800")
    img=Image.open("ADMIN PAGE.png")
    myimg=ImageTk.PhotoImage(img)
    imglabel=Label(image=myimg)
    imglabel.place(x=0,y=0)

    cur.execute("select movies from movies")
    p=cur.fetchall()
    n=0

    try:
        text3=Label(base,text=p[n],font=("Arial",25),fg="white",bg="black").place(x=150,y=220)
        button1=Button(base,text="Delete",font=("Arial",14),fg="green",bg="black",command=lambda:delete(0)).place(x=150,y=320)

        text4=Label(base,text=p[n+1],font=("Arial",25),fg="white",bg="black").place(x=350,y=220)
        button2=Button(base,text="Delete",font=("Arial",14),fg="green",bg="black",command=lambda:delete(1)).place(x=350,y=320)

        text5=Label(base,text=p[n+2],font=("Arial",25),fg="white",bg="black").place(x=550,y=220)
        button2=Button(base,text="Delete",font=("Arial",14),fg="green",bg="black",command=lambda:delete(2)).place(x=550,y=320)

        text5=Label(base,text=p[n+3],font=("Arial",25),fg="white",bg="black").place(x=800,y=220)
        button2=Button(base,text="Delete",font=("Arial",14),fg="green",bg="black",command=lambda:delete(3)).place(x=800,y=320)

        text5=Label(base,text=p[n+4],font=("Arial",25),fg="white",bg="black").place(x=1050,y=220)
        button3=Button(base,text="Delete",font=("Arial",14),fg="green",bg="black",command=lambda:delete(4)).place(x=1050,y=320)
    except:
        pass

    button7=Button(base,text="INSERT",font=("Arial",15),fg="green",bg="black",command=lambda:insert()).place(x=1300,y=220)
    button4=Button(base,text="LOGOUT",font=("Arial",13),fg="red",bg="black",command=lambda:logout1()).place(x=1250,y=750)
    button5=Button(base,text="QUIT",font=("Arial",13),command=lambda:quitmain1()).place(x=1350,y=750)
    button6=Button(base,text="RELOAD",font=("Arial",13),command=lambda:reload()).place(x=1290,y=700)

    base.mainloop()


def signup(v1,v4,v3,v2):
    cur.execute("insert into user values('{}','{}','{}','{}')".format(v1,v2,v3,v4))
    con.commit()
    messagebox.showinfo("done","signup Completed")
    base.destroy()
    loginwin()
    
def charges1(co):
    global charge,time
    time="10:00 am"
    a=v
    b=""
    for i in a:
        if i.isdigit():
            b=b+i
        elif i.isalpha():
            b=b+i
        elif i.isspace():
            b=b+i
    cur.execute("select charges from movies where movies='{}'".format(b))
    x=cur.fetchall()
    y=0
    for i in x:
        for c in i:
            y=c
            charge=y*co
    text14=Label(frame1,text="Amount to pay is:",font=("Arial",18),fg="white",bg="black").place(x=700,y=590)

    text15=Label(frame1,text=charge,font=("Arial",18),fg="white",bg="black").place(x=900,y=590)

    button1=Button(frame1,text="Pay",font=("Arial",13),fg="green",command=lambda:payed()).place(x=750,y=630)

    button2=Button(frame1,text="Cancel",font=("Arial",13),fg="red",command=lambda:cancelpay()).place(x=800,y=630)

def charges2(co):
    global charge,time
    time="2:00 pm"
    a=v
    b=""
    for i in a:
        if i.isdigit():
            b=b+i
        elif i.isalpha():
            b=b+i
        elif i.isspace():
            b=b+i
    cur.execute("select charges from movies where movies='{}'".format(b))
    x=cur.fetchall()
    y=0
    for i in x:
        for c in i:
            y=c
            charge=y*co
    text14=Label(frame1,text="Amount to pay is:",font=("Arial",18),fg="white",bg="black").place(x=700,y=590)

    text15=Label(frame1,text=charge,font=("Arial",18),fg="white",bg="black").place(x=900,y=590)

    button1=Button(frame1,text="Pay",font=("Arial",13),fg="green",command=lambda:payed()).place(x=750,y=630)

    button2=Button(frame1,text="Cancel",font=("Arial",13),fg="red",command=lambda:cancelpay()).place(x=800,y=630)
def charges3(co):
    global charge,time
    time="6:00 pm"
    a=v
    b=""
    for i in a:
        if i.isdigit():
            b=b+i
        elif i.isalpha():
            b=b+i
        elif i.isspace():
            b=b+i
    cur.execute("select charges from movies where movies='{}'".format(b))
    x=cur.fetchall()
    y=0
    for i in x:
        for c in i:
            y=c
            charge=y*co
    text14=Label(frame1,text="Amount to pay is:",font=("Arial",18),fg="white",bg="black").place(x=700,y=590)

    text15=Label(frame1,text=charge,font=("Arial",18),fg="white",bg="black").place(x=900,y=590)

    button1=Button(frame1,text="Pay",font=("Arial",13),fg="green",command=lambda:payed()).place(x=750,y=630)

    button2=Button(frame1,text="Cancel",font=("Arial",13),fg="red",command=lambda:cancelpay()).place(x=800,y=630)
    
def charges4(co):
    global charge,time
    time="10:00 pm"
    a=v
    b=""
    for i in a:
        if i.isdigit():
            b=b+i
        elif i.isalpha():
            b=b+i
        elif i.isspace():
            b=b+i
    cur.execute("select charges from movies where movies='{}'".format(b))
    x=cur.fetchall()
    y=0
    for i in x:
        for c in i:
            y=c
            charge=y*co
    text14=Label(frame1,text="Amount to pay is:",font=("Arial",18),fg="white",bg="black").place(x=700,y=590)

    text15=Label(frame1,text=charge,font=("Arial",18),fg="white",bg="black").place(x=900,y=590)

    button1=Button(frame1,text="Pay",font=("Arial",13),fg="green",command=lambda:payed()).place(x=750,y=630)

    button2=Button(frame1,text="Cancel",font=("Arial",13),fg="red",command=lambda:cancelpay()).place(x=800,y=630)
    
def cancelpay():
    global base
    base.destroy()
    bookingwin()

def seatname1():
    global cse,sc
    sc=1
    if cse==0:
        text8=Label(frame1,text="Enter Recipient Name:",font=("Arial",14),fg="white",bg="black").place(x=250,y=542)
        box=Entry(frame1)
        box.place(x=450,y=548)
        button6=Button(frame1,text="Confirm",command=lambda:confirmcom()).place(x=470,y=580)
        cse=cse+1
        
def seatname2():
    global cse,sc
    sc=2
    if cse==0:
        text8=Label(frame1,text="Enter Recipient Name:",font=("Arial",14),fg="white",bg="black").place(x=250,y=542)
        box=Entry(frame1)
        box.place(x=450,y=548)
        text9=Label(frame1,text="Enter Recipient Name:",font=("Arial",14),fg="white",bg="black").place(x=250,y=572)
        box=Entry(frame1)
        box.place(x=450,y=575)
        button6=Button(frame1,text="Confirm",command=lambda:confirmcom()).place(x=470,y=610)
        cse=cse+2

def seatname3():
    global cse,sc
    sc=3
    if cse==0:
        text8=Label(frame1,text="Enter Recipient Name:",font=("Arial",14),fg="white",bg="black").place(x=250,y=542)
        box=Entry(frame1)
        box.place(x=450,y=548)
        text9=Label(frame1,text="Enter Recipient Name:",font=("Arial",14),fg="white",bg="black").place(x=250,y=572)
        box=Entry(frame1)
        box.place(x=450,y=578)
        text10=Label(frame1,text="Enter Recipient Name:",font=("Arial",14),fg="white",bg="black").place(x=250,y=602)
        box=Entry(frame1)
        box.place(x=450,y=608)
        button6=Button(frame1,text="Confirm",command=lambda:confirmcom()).place(x=470,y=640)
        cse=cse+3

def seatname4():
    global cse,sc
    sc=4
    if cse==0:
        text8=Label(frame1,text="Enter Recipient Name:",font=("Arial",14),fg="white",bg="black").place(x=250,y=542)
        box=Entry(frame1)
        box.place(x=450,y=548)
        text9=Label(frame1,text="Enter Recipient Name:",font=("Arial",14),fg="white",bg="black").place(x=250,y=572)
        box=Entry(frame1)
        box.place(x=450,y=578)
        text10=Label(frame1,text="Enter Recipient Name:",font=("Arial",14),fg="white",bg="black").place(x=250,y=602)
        box=Entry(frame1)
        box.place(x=450,y=608)
        text11=Label(frame1,text="Enter Recipient Name:",font=("Arial",14),fg="white",bg="black").place(x=250,y=632)
        box=Entry(frame1)
        box.place(x=450,y=638)
        button6=Button(frame1,text="Confirm",command=lambda:confirmcom()).place(x=470,y=670)
        cse=cse+4

def seatname5():
    global cse,sc
    sc=5
    if cse==0:
        text8=Label(frame1,text="Enter Recipient Name:",font=("Arial",14),fg="white",bg="black").place(x=250,y=542)
        box=Entry(frame1)
        box.place(x=450,y=548)
        text9=Label(frame1,text="Enter Recipient Name:",font=("Arial",14),fg="white",bg="black").place(x=250,y=572)
        box=Entry(frame1)
        box.place(x=450,y=578)
        text10=Label(frame1,text="Enter Recipient Name:",font=("Arial",14),fg="white",bg="black").place(x=250,y=602)
        box=Entry(frame1)
        box.place(x=450,y=608)
        text11=Label(frame1,text="Enter Recipient Name:",font=("Arial",14),fg="white",bg="black").place(x=250,y=632)
        box=Entry(frame1)
        box.place(x=450,y=638)
        text12=Label(frame1,text="Enter Recipient Name:",font=("Arial",14),fg="white",bg="black").place(x=250,y=662)
        box=Entry(frame1)
        box.place(x=450,y=668)

        button6=Button(frame1,text="Confirm",command=lambda:confirmcom()).place(x=470,y=700)
        cse=cse+5
def confirmcom():
    text13=Label(frame1,text="AvailableShow's:",font=("Arial",18),fg="white",bg="black").place(x=700,y=500)
    button7=Button(frame1,text="10:00am",font=("Arial,6"),fg="green",command=lambda:charges1(cse)).place(x=900,y=495)
    button8=Button(frame1,text="2:00pm",font=("Arial,6"),fg="green",command=lambda:charges2(cse)).place(x=1020,y=495)
    button9=Button(frame1,text="6:00pm",font=("Arial,6"),fg="green",command=lambda:charges3(cse)).place(x=1120,y=495)
    button10=Button(frame1,text="10:00pm",font=("Arial,6"),fg="green",command=lambda:charges4(cse)).place(x=1220,y=495)
    
def bookingwin():
    global base,count,p
    base=Tk()
    base.geometry("1423x800")
    img=Image.open("HOME PAGE.png")
    myimg=ImageTk.PhotoImage(img)
    imglabel=Label(image=myimg)
    imglabel.place(x=0,y=0)
    cur.execute("select movies from movies")
    p=cur.fetchall()
    count=0
    n=0

    try:
        text3=Label(base,text=p[n],font=("Arial",25),fg="white",bg="black").place(x=150,y=220)
        button1=Button(base,text="BookNow",font=("Arial",14),fg="green",bg="black",command=lambda:movie(0)).place(x=150,y=320)

        text4=Label(base,text=p[n+1],font=("Arial",25),fg="white",bg="black").place(x=350,y=220)
        button2=Button(base,text="BookNow",font=("Arial",14),fg="green",bg="black",command=lambda:movie(1)).place(x=350,y=320)

        text5=Label(base,text=p[n+2],font=("Arial",25),fg="white",bg="black").place(x=550,y=220)
        button2=Button(base,text="BookNow",font=("Arial",14),fg="green",bg="black",command=lambda:movie(2)).place(x=550,y=320)

        text5=Label(base,text=p[n+3],font=("Arial",25),fg="white",bg="black").place(x=800,y=220)
        button2=Button(base,text="BookNow",font=("Arial",14),fg="green",bg="black",command=lambda:movie(3)).place(x=800,y=320)

        text5=Label(base,text=p[n+4],font=("Arial",25),fg="white",bg="black").place(x=1050,y=220)
        button3=Button(base,text="BookNow",font=("Arial",14),fg="green",bg="black",command=lambda:movie(4)).place(x=1050,y=320)
    except:
        pass

    button4=Button(base,text="LOGOUT",font=("Arial",13),fg="red",bg="black",command=lambda:logout1()).place(x=1250,y=750)

    button5=Button(base,text="QUIT",font=("Arial",13),command=lambda:quitmain1()).place(x=1350,y=750)
    base.mainloop()
    
def logout1():
    global base
    base.destroy()
    loginwin()
 
def quitmain1():
    global base
    base.destroy()
    

def movie(u):
    global count,frame1,cse,v,p
    cse=0
    print(p)
    v=p[u]
    if count==0:
        frame1=LabelFrame(base,padx=900,pady=900).place()

        text6=Label(frame1,text=p[u],font=("Arial",30),fg="white",bg="black").place(x=600,y=400)
        text7=Label(frame1,text="Number of Tickets:",font=("Arial",16),fg="white",bg="black").place(x=250,y=502)

        button1=Button(frame1,text="1",command=lambda:seatname1()).place(x=430,y=503)

        button2=Button(frame1,text="2",command=lambda:seatname2()).place(x=450,y=503)

        button3=Button(frame1,text="3",command=lambda:seatname3()).place(x=470,y=503)

        button4=Button(frame1,text="4",command=lambda:seatname4()).place(x=490,y=503)

        button5=Button(frame1,text="5",command=lambda:seatname5()).place(x=510,y=503)
        count=count+1

def gotohome():
    global base
    base.destroy()
    bookingwin()

def logout2():
    global base
    base.destroy()
    loginwin()
 
def quitmain2():
    global base
    base.destroy()

def payed():
    global base,base
    base.destroy()
    base=Tk()
    base.geometry("1423x800")
    img=Image.open("CONFIRM.png")
    myimg=ImageTk.PhotoImage(img)
    imglabel=Label(image=myimg)
    imglabel.place(x=0,y=0)
    for i in v:
        u=i
        cur.execute("select*from movies where movies='{}'".format(u))
        x=cur.fetchall()
    for i in x:
        y=i
    text8=Label(text="Movie:",font=("Arial",20),fg="white",bg="black").place(x=50,y=200)

    text9=Label(text=v,font=("Arial",20),fg="white",bg="black").place(x=180,y=200)
    text10=Label(text="Screen:",font=("Arial",20),fg="white",bg="black").place(x=50,y=250)

    text11=Label(text=y[1],font=("Arial",20),fg="white",bg="black").place(x=180,y=250)
    text12=Label(text="Date:",font=("Arial",20),fg="white",bg="black").place(x=50,y=300)

    text13=Label(text=y[2],font=("Arial",20),fg="white",bg="black").place(x=180,y=300)
    text14=Label(text="Ticket:",font=("Arial",20),fg="white",bg="black").place(x=50,y=350)

    text15=Label(text=sc,font=("Arial",20),fg="white",bg="black").place(x=180,y=350)
    text16=Label(text="Time:",font=("Arial",20),fg="white",bg="black").place(x=50,y=400)

    text17=Label(text=time,font=("Arial",20),fg="white",bg="black").place(x=180,y=400)
    text18=Label(text="Ticket has been sent to your email",font=("Arial",20),fg="green",bg="black").place(x=50,y=450)

    button1=Button(text="Confirm",font=("Arial",13),fg="white",bg="black",command=lambda:gotohome()).place(x=140,y=500)
    button4=Button(base,text="LOGOUT",font=("Arial",13),fg="red",bg="black",command=lambda:logout2()).place(x=850,y=750)
    button5=Button(base,text="QUIT",font=("Arial",13),command=lambda:quitmain2()).place(x=1350,y=750)
    base.mainloop()
loginwin()
con.close()
