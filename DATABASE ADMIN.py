from tkinter import *
from tkinter import messagebox
import sqlite3
import sys
import sqlite3
import datetime


conn = sqlite3.connect("database1.db")
c = conn.cursor()

root = Tk()
root.title("DBMS")
root.geometry("1350x650+0+0")

#----------------------------------------FUNCTIONS----------------------------------------------------------------------------
def iExit():
    qExit = messagebox.askyesno("DBMS","Do You Want To Exit Program")
    if qExit > 0:
        root.destroy()
        return

def create_table():
    for i in f2.winfo_children():
        i.destroy()
    def official_table_create():
        Tname = tname.get()
        obj = open("database.txt","a")
        obj.write(Tname)
        obj.write("     ")
        now  = str(datetime.datetime.now())
        obj.write(now)
        obj.write("\n")
        obj.close()
        c.execute("CREATE TABLE IF NOT EXISTS {} ( NAME VARCHAR(10) , PHONE NUMBER(10) , AGE NUMBER(2) , WORK VARCHAR(20) )".format(Tname))
        labelstatus = Label(f1b , font=("arial",8,"bold"),text="{} Table Created!!!!".format(Tname)).pack(side=TOP)
    
    labelTname = Label(f2 ,text="Table Name:",font=("arial",10,"bold")).grid(row=1,column=0)
    entryTname = Entry(f2 ,textvariable=tname ,font=("arial",13,"bold"), width = 20).grid(row=1,column=3)
    buttonx = Button(f2 , text = "Create" ,font=("arial",13,"bold"),padx=8,pady=8 ,bd = 5,command =official_table_create).grid(row=7,column=3)

def data_entry():
    
    for i in f2.winfo_children():
        i.destroy()

    def data_fill():
        name_tab = tname1.get()

        for i in f2.winfo_children():
            i.destroy()
        
        def row_fill():
            c.execute("INSERT INTO {} (NAME , PHONE , AGE , WORK ) VALUES (? , ? ,? ,?)".format(name_tab),( name.get(),phone.get(),age.get(),work.get() ))
            conn.commit()
            labelROW = Label(f1b , font=("arial",8,"bold"),text="Row Has Been Created In {} Table".format(name_tab)).pack(side=TOP)
                
        labelname = Label(f2 ,text="Name :",font=("arial",10,"bold")).grid(row=1,column=0)
        entryname = Entry(f2 ,textvariable=name ,font=("arial",13,"bold"), width = 20).grid(row=1,column=3)
            
        labelphone = Label(f2 ,text="Phone :",font=("arial",10,"bold")).grid(row=3,column=0)
        entryphone = Entry(f2 ,textvariable=phone ,font=("arial",13,"bold"), width = 20).grid(row=3,column=3)
            
        labelage = Label(f2 ,text="Age :",font=("arial",10,"bold")).grid(row=5,column=0)
        entryage = Entry(f2 ,textvariable=age ,font=("arial",13,"bold"), width = 20).grid(row=5,column=3)
            
        labelwork = Label(f2 ,text="Work :",font=("arial",10,"bold")).grid(row=7,column=0)
        entrywork = Entry(f2 ,textvariable=work ,font=("arial",13,"bold"), width = 20).grid(row=7,column=3)
            
        buttonfill = Button(f2 , text = "Enter row",font=("arial",13,"bold"),padx=8,pady=8 ,bd = 5,command =row_fill).grid(row=10,column=3)
        
    
    labelTname1 = Label(f2 ,text="Table Name:",font=("arial",10,"bold")).grid(row=1,column=0)
    entryTname1 = Entry(f2 ,textvariable=tname1 ,font=("arial",13,"bold"), width = 20).grid(row=1,column=3)
    
    buttony = Button(f2 , text = "Enter" ,font=("arial",13,"bold"),padx=8,pady=8 ,bd = 5,command =data_fill).grid(row=10,column=3)



def print_data():
    for i in f2.winfo_children():
        i.destroy()

    def official_print_data():
        for i in f2.winfo_children():
            i.destroy()
        name_t = tname3.get()
        c.execute("SELECT * FROM {}".format(name_t))
        data = c.fetchall()
        for k in data:
            labelPrint = Label(f2 ,text=k,font=("arial",15,"bold")).pack(side=TOP)


    labelTname2 = Label(f2 ,text="Table Name:",font=("arial",10,"bold")).grid(row=1,column=0)
    entryTname2 = Entry(f2 ,textvariable=tname3 ,font=("arial",13,"bold"), width = 20).grid(row=1,column=3)
    
    buttonZ = Button(f2 , text = "Print Data" ,font=("arial",13,"bold"),padx=8,pady=8 ,bd = 5,command = official_print_data).grid(row=10,column=3)


    
def delete_table():
    for i in f2.winfo_children():
        i.destroy()

    def official_delete():
        name_d = tname4.get()
        c.execute("DROP TABLE {}".format(name_d))
        labelDEL = Label(f1b , font=("arial",8,"bold"),text="{} table has been deleted".format(name_d)).pack(side=TOP)
        



    labelTname3 = Label(f2 ,text="Table Name:",font=("arial",10,"bold")).grid(row=1,column=0)
    entryTname3 = Entry(f2 ,textvariable=tname4 ,font=("arial",13,"bold"), width = 20).grid(row=1,column=3)
    
    buttonA = Button(f2 , text = "Delete Table" ,font=("arial",13,"bold"),padx=8,pady=8 ,bd = 5,command = official_delete).grid(row=10,column=3)

    
    
        
def access_db():
    for i in f2.winfo_children():
        i.destroy()

    def login_base():
        username = UNAME.get()
        password = int(UPASS.get())

        if((username == "admin" and password == 4087) or (username == "ADMIN" and password == 4087)):
            for i in f2.winfo_children():
                i.destroy()
            obj = open("database.txt","r")
            data = obj.readlines()
            for k in data:
                labelFILE = Label(f2 ,text=k,font=("arial",15,"bold")).pack(side=TOP)
            obj.close()
        
        else:
            labelERROR = Label(f1b , font=("arial",8,"bold"),text="INVALID CREDENTIALS").pack(side=TOP)
            
            

    labelUNAME  = Label(f2 ,text="UserName:",font=("arial",10,"bold")).grid(row=1,column=0)
    entryUNAME = Entry(f2 ,textvariable=UNAME ,font=("arial",13,"bold"), width = 20).grid(row=1,column=3)
    
    labelPASS  = Label(f2 ,text="Password (INT):",font=("arial",10,"bold")).grid(row=3,column=0)
    entryPASS = Entry(f2 ,textvariable=UPASS,show="*" ,font=("arial",13,"bold"), width = 20).grid(row=3,column=3)

    buttonlogin = Button(f2 , text = "Login" ,font=("arial",13,"bold"),padx=8,pady=8 ,bd = 5,command = login_base).grid(row=10,column=3)



    






#-----------------------------------------------------------------------------------------------------------------------------

#---------------------------------------VARIABLES------------------------------------------------------------------------------
tname = StringVar()
row = StringVar()
tname1 = StringVar()
name = StringVar()
phone = StringVar()
age = StringVar()
work = StringVar()
tname3 = StringVar()
tname4 = StringVar()
UNAME = StringVar()
UPASS = StringVar()






#-----------------------------------------------------------------------------------------------------------------------------------

frame1 = Frame(root , width=1350 , height=50 , bd=8 , relief="raise")
frame1.pack(side=TOP)
f1 = Frame(root , width=600, height=600 , bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root , width=900, height=700 , bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a = Frame(f1 , width = 600,height = 200,bd=20 , relief="raise")
f1a.pack(side=TOP)
f1b = Frame(root , width = 600 ,height = 200)
f1b.pack(side=BOTTOM)
labelf1b = Label(f1b , font=("Algerian",12,"bold"),text=":::::::STATUS ::::::::").pack(side=TOP)


labelinfo = Label(frame1 , font=("arial",60,"bold"),text="                Database Management                 ")
labelinfo.grid(row=0,column=0)

button1 = Button(f1a ,padx=16,pady=16, text = "1. CREATE TABLE",font=("arial",13,"bold"),bd=10,command= create_table).grid(row=0,column=0)

button2 = Button(f1a ,padx=16,pady=16, text = "2. ENTER DATA IN TABLE",font=("arial",13,"bold"),bd=10,command= data_entry).grid(row=1,column=0)

button3 = Button(f1a ,padx=16,pady=16, text = "3. DISPLAY DATA",font=("arial",13,"bold"),bd=10,command= print_data).grid(row=2,column=0)

button4 = Button(f1a ,padx=16,pady=16, text = "4. DELETE TABLE",font=("arial",13,"bold"),bd=10,command = delete_table).grid(row=3,column=0)

button5 = Button(f1a ,padx=16,pady=16, text = "5. ACCESS DATABASE",font=("arial",13,"bold"),bd=10 , command = access_db).grid(row=4,column=0)

button1 = Button(f1a ,padx=16,pady=16, text = "6. EXIT PROGRAM",font=("arial",13,"bold"),bd=10,command=iExit).grid(row=5,column=0)























root.mainloop()
