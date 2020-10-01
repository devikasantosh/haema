from tkinter import*
import tkinter as tk
import mysql.connector
#import time
m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
c=m.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
c.execute("USE HAEMA")
c.execute("CREATE TABLE IF NOT EXISTS REQUESTS(Category VARCHAR(10), Hospital_ID VARCHAR(3), Hospital_Name VARCHAR(20), Blood_Group VARCHAR(10),No_of_bags INTEGER(2), Date VARCHAR(12))")
c.execute("CREATE TABLE IF NOT EXISTS DONORS(Donor_ID VARCHAR(3), Donor_Name VARCHAR(20), Age INTEGER(2), Blood_Group VARCHAR(10), Date VARCHAR(12))")

#===============================================================================================================================
#===============================================================================================================================
#===============================================================================================================================



root=Tk()
root.title("Haema")
root.state('zoomed')
canvas = Canvas(root, width = 1438, height = 830, bg='black') 
canvas.pack(expand=YES,fill=BOTH)
img=PhotoImage(file="haema2.png")
Label(image=img, width=0, height=0,border=0).place(x=250,y=100)
#img_icon=PhotoImage(file="haema.png").subsample(3,3)


#===============================================================================================================================
#===============================================================================================================================
#========================================================REQUEST================================================================
#===============================================================================================================================
#===============================================================================================================================    
def request():
    
    global category
    global hosp_id
    global hosp_name
    global bloodgrp
    global noofbags
    global datenow
    global cat
    global h_id
    global h_name
    global no
    global b
    global date
    global root1
    root1 = Toplevel(root)
    root1.geometry('500x500')
    root1.title("Request Form")
    root1.configure(background='black')
    cat=StringVar()
    h_id=StringVar()
    h_name=StringVar()
    b=StringVar()
    no = IntVar()
    date= StringVar()


    def request_database():
    #m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        category=cat.get()
        hosp_id=h_id.get()
        hosp_name=h_name.get()
        bloodgrp=b.get()
        noofbags=no.get()
        datenow=date.get()

        c.execute("INSERT INTO REQUESTS VALUES ('%s','%s','%s','%s','%s','%s')"%(category,hosp_id,hosp_name,bloodgrp,noofbags,datenow))
        m.commit()
        #request.destroy()
        global r      
        r=Toplevel(root1)
        r.geometry('275x135')
        r.title("SUCCESS")
        r.configure(background='IndianRed')
            
        r1=Label(r, text="REQUEST SUBMITTED.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
        r1.place(x=0,y=50)
        '''entry_2.delete(0,END)
        entry_3.delete(0,END)
        #droplist.delete()
        spin.delete(0,END)
        entry_6.delete(0,END)'''
        

    #================================================================================
    label_0 = Label(root1, text="REQUEST FORM",width=20,font=("bold", 20),bg="IndianRed",fg="white")
    label_0.place(x=90,y=50)
    #=====================================================================================
    label_1 = Label(root1, text="Category",width=20,font=("bold", 10),bg="black",fg="white")
    label_1.place(x=80,y=130)
    Radiobutton(root1, text="Emergency", variable=cat, value="Emergency").place(x=240,y=130)
    Radiobutton(root1, text="Routine", variable=cat, value="Routine").place(x=330,y=130)
    #=====================================================================================
    label_2 = Label(root1, text="Hospital ID",width=20,font=("bold", 10),bg="black",fg="white")
    label_2.place(x=80,y=180)
    entry_2 = Entry(root1,textvar=h_id)
    entry_2.place(x=240,y=180)
    #=======================================================================================
    label_3 = Label(root1, text="Hospital Name",width=20,font=("bold", 10),bg="black",fg="white")
    label_3.place(x=80,y=230)
    entry_3 = Entry(root1,textvar=h_name)
    entry_3.place(x=240,y=230)
    #=========================================================================================
    label_4 = Label(root1, text="Blood Group",width=20,font=("bold", 10),bg="black",fg="white")
    label_4.place(x=80,y=280)
    list1 = ['A-','A+','B-','B+','O-','O+','AB-','AB+','Bombay'];
    droplist=OptionMenu(root1,b,*list1)
    droplist.config(width=15)
    b.set('SELECT') 
    droplist.place(x=240,y=280)
    #=============================================================================================
    label_5 = Label(root1, text="No. of Bags",width=20,font=("bold", 10),bg="black",fg="white")
    label_5.place(x=80,y=330)
    spin = Spinbox(root1, from_=1, to=10, textvar=no)
    #spin.pack()
    spin.place(x=240,y=330)

    #=========================================================================================
    label_6 = Label(root1, text="Required Date (YYYY-MM-DD)",width=25,font=("bold", 10),bg="black",fg="white")
    label_6.place(x=15,y=380)
    entry_6 = Entry(root1, textvar=date)
    entry_6.place(x=240,y=380)
    #==================================================================================================
    Button(root1, text='Submit',width=20,bg='IndianRed',fg='white',command=request_database).place(x=170,y=440)
    root1.mainloop()
    
#===============================================================================================================================
#===============================================================================================================================
#========================================================MANAGE=================================================================
#===============================================================================================================================
#===============================================================================================================================

def manage():
    global manage
    root2=Toplevel(root)
    root2.title("Haema Management")
    canvas = Canvas(root2, width = 1900, height = 900, bg='black') 
    canvas.pack(expand=YES,fill=BOTH)
    #img=PhotoImage(file="haema2.png")
    img=PhotoImage(file="haema.png").subsample(3,3)
    #r=Toplevel(root2)
    Label(root2,image=img, width=0, height=0,border=0).place(x=50,y=40)
    root2.state('zoomed')
    label_mgmt= Label(root2, text="MANAGEMENT",width=35,font=("Times New Roman", 40),bg="IndianRed4",fg="white")
    label_mgmt.place(x=400,y=60)


    m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
    c=m.cursor()
    c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
    c.execute("USE HAEMA")

    def show_an():
        global show_an
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        global r1    
        r1=Toplevel(root2)
        r1.geometry('290x150-600+375')
        r1.title("A- DONOR")
        r1.configure(background='IndianRed')
        c.execute("select donor_id,donor_name from donors where blood_group='A-' order by date;")
        if c.fetchone() is None:
            do=Label(r1, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (a,b)=c.fetchone()
            m.close()
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            c1.execute("select hospital_name from requests where blood_group='A-' order by date;")
            (z,)=c1.fetchone()
            d=("BLOOD AVAILABLE:\n\nDONOR ID:",a,"\nDONOR NAME:",b,"\n\nDONATE TO HOSPITAL:",z)
            m1.close()
            do=Label(r1, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=20)
    def show_ap():
        global show_ap
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        global r2
        r2=Toplevel(root2)
        r2.geometry('290x150-600+375')
        r2.title("A+ DONOR")
        r2.configure(background='IndianRed')
        c.execute("select donor_id,donor_name from donors where blood_group='A+' order by date;")
        if c.fetchone() is None:
            do=Label(r2, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (a,b)=c.fetchone()
            m.close()
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            c1.execute("select hospital_name from requests where blood_group='A+' order by date;")
            (z,)=c1.fetchone()
            d=("BLOOD AVAILABLE:\n\nDONOR ID:",a,"\nDONOR NAME:",b,"\n\nDONATE TO HOSPITAL:",z)
            m1.close()
            do=Label(r2, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=20)
    def show_bn():
        global show_bn
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        global r3
        r3=Toplevel(root2)
        r3.geometry('290x150-600+375')
        r3.title("B- DONOR")
        r3.configure(background='IndianRed')
        c.execute("select donor_id,donor_name from donors where blood_group='B-' order by date;")
        if c.fetchone() is None:
            do=Label(r3, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (a,b)=c.fetchone()
            m.close()
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            c1.execute("select hospital_name from requests where blood_group='B-' order by date;")
            (z,)=c1.fetchone()
            d=("BLOOD AVAILABLE:\n\nDONOR ID:",a,"\nDONOR NAME:",b,"\n\nDONATE TO HOSPITAL:",z)
            m1.close()
            do=Label(r3, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=20)
    def show_bp():
        global show_bp
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        global r4
        r4=Toplevel(root2)
        r4.geometry('290x150-600+375')
        r4.title("B+ DONOR")
        r4.configure(background='IndianRed')
        c.execute("select donor_id,donor_name from donors where blood_group='B+' order by date;")
        if c.fetchone() is None:
            do=Label(r4, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (a,b)=c.fetchone()
            m.close()
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            c1.execute("select hospital_name from requests where blood_group='B+' order by date;")
            (z,)=c1.fetchone()
            d=("BLOOD AVAILABLE:\n\nDONOR ID:",a,"\nDONOR NAME:",b,"\n\nDONATE TO HOSPITAL:",z)
            m1.close()
            do=Label(r4, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=20)
    def show_on():
        global show_on
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        global r5
        r5=Toplevel(root2)
        r5.geometry('290x150-600+375')
        r5.title("O- DONOR")
        r5.configure(background='IndianRed')
        c.execute("select donor_id,donor_name from donors where blood_group='O-' order by date;")
        if c.fetchone() is None:
            do=Label(r5, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (a,b)=c.fetchone()
            m.close()
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            c1.execute("select hospital_name from requests where blood_group='O-' order by date;")
            (z,)=c1.fetchone()
            d=("BLOOD AVAILABLE:\n\nDONOR ID:",a,"\nDONOR NAME:",b,"\n\nDONATE TO HOSPITAL:",z)
            m1.close()
            do=Label(r5, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=20)
    def show_op():
        global show_op
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        global r6
        r6=Toplevel(root2)
        r6.geometry('290x150-600+375')
        r6.title("O+ DONOR")
        r6.configure(background='IndianRed')
        c.execute("select donor_id,donor_name from donors where blood_group='O+' order by date;")
        if c.fetchone() is None:
            do=Label(r6, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (a,b)=c.fetchone()
            m.close()
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            c1.execute("select hospital_name from requests where blood_group='O+' order by date;")
            (z,)=c1.fetchone()
            d=("BLOOD AVAILABLE:\n\nDONOR ID:",a,"\nDONOR NAME:",b,"\n\nDONATE TO HOSPITAL:",z)
            m1.close()
            do=Label(r6, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=20)
    def show_abn():
        global show_abn
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        global r7
        r7=Toplevel(root2)
        r7.geometry('290x150-600+375')
        r7.title("AB- DONOR")
        r7.configure(background='IndianRed')
        c.execute("select donor_id,donor_name from donors where blood_group='AB-' order by date;")
        if c.fetchone() is None:
            do=Label(r7, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (a,b)=c.fetchone()
            m.close()
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            c1.execute("select hospital_name from requests where blood_group='AB-' order by date;")
            (z,)=c1.fetchone()
            d=("BLOOD AVAILABLE:\n\nDONOR ID:",a,"\nDONOR NAME:",b,"\n\nDONATE TO HOSPITAL:",z)
            m1.close()
            do=Label(r7, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=20)
    def show_abp():
        global show_abp
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        global r8
        r8=Toplevel(root2)
        r8.geometry('290x150-600+375')
        r8.title("AB+ DONOR")
        r8.configure(background='IndianRed')
        c.execute("select donor_id,donor_name from donors where blood_group='AB+' order by date;")
        if c.fetchone() is None:
            do=Label(r8, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (a,b)=c.fetchone()
            m.close()
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            c1.execute("select hospital_name from requests where blood_group='AB+' order by date;")
            (z,)=c1.fetchone()
            d=("BLOOD AVAILABLE:\n\nDONOR ID:",a,"\nDONOR NAME:",b,"\n\nDONATE TO HOSPITAL:",z)
            m1.close()
            do=Label(r8, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=20)
    def show_bo():
        global show_bo
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        global r9
        r9=Toplevel(root2)
        r9.geometry('290x150-600+375')
        r9.title("BOMBAY DONOR")
        r9.configure(background='IndianRed')
        c.execute("select donor_id,donor_name from donors where blood_group='Bombay' order by date;")
        if c.fetchone() is None:
            do=Label(r9, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (a,b)=c.fetchone()
            m.close()
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            c1.execute("select hospital_name from requests where blood_group='Bombay' order by date;")
            (z,)=c1.fetchone()
            d=("BLOOD AVAILABLE:\n\nDONOR ID:",a,"\nDONOR NAME:",b,"\n\nDONATE TO HOSPITAL:",z)
            m1.close()
            do=Label(r9, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=20)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    

    def donate_an():
        global donate_an
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        c.execute("select donor_id,donor_name from donors where blood_group='A-' order by date;")
        #(del1,del2)=c.fetchone()
        #m.commit()
        #m.close()
        #print(del1)

        global r11    
        r11=Toplevel(root2)
        r11.geometry('300x135-500+375')
        r11.title("A- BLOOD")
        r11.configure(background='IndianRed')
        if c.fetchone() is None:
            do=Label(r11, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (del1,del2)=c.fetchone()        
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            st="delete from donors where donor_id = {}".format(del1)
            c1.execute(st)
            m1.commit()
            c1.execute("select hospital_id,no_of_bags from requests where blood_group='A-' order by category,date;")
            (z,a,)=c1.fetchone()
            print(a)
            b=a-1
            print(b)
            m1.close()
            
            m2=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c2=m2.cursor()
            c2.execute("USE HAEMA") 
            #c2.execute("update requests set no_of_bags='%s' where blood_group='A-' and no_of_bags='%s'")%(b,a)
            #c2.commit()
            y1 = "update requests set no_of_bags=%s where blood_group='A-' and hospital_id=%s"
            y2 = (b,z)
            c2.execute(y1, y2)
            m2.commit()
            
            m3=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c3=m3.cursor()
            c3.execute("USE HAEMA")
            c3.execute("select hospital_name from requests where blood_group='A-' order by date;")
            (z,)=c3.fetchone()
            d=("BLOOD DONATED TO",z,"\n\nDONOR ID:",del1,"\nDONOR NAME:",del2)
            do=Label(r11, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=10,y=20)
            m3.close()
      
    def donate_ap():
        global donate_ap
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        c.execute("select donor_id,donor_name from donors where blood_group='A+' order by date;")
        #(del1,del2)=c.fetchone()
        #m.commit()
        #m.close()
        #print(del1)

        global r12    
        r12=Toplevel(root2)
        r12.geometry('300x135-500+375')
        r12.title("A+ BLOOD")
        r12.configure(background='IndianRed')
           
        if c.fetchone() is None:
            do=Label(r12, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (del1,del2)=c.fetchone()        
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            st="delete from donors where donor_id = {}".format(del1)
            c1.execute(st)
            m1.commit()
            c1.execute("select hospital_id, no_of_bags from requests where blood_group='A+' order by category,date;")
            (z,a,)=c1.fetchone()
            print(a)
            b=a-1
            print(b)
            m1.close()
            
            m2=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c2=m2.cursor()
            c2.execute("USE HAEMA") 
            #c2.execute("update requests set no_of_bags='%s' where blood_group='A-' and no_of_bags='%s'")%(b,a)
            #c2.commit()
            y1 = "update requests set no_of_bags=%s where blood_group='A+' and hospital_id=%s"
            y2 = (b,z)
            c2.execute(y1, y2)
            m2.commit()

            m3=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c3=m3.cursor()
            c3.execute("USE HAEMA")
            c3.execute("select hospital_name from requests where blood_group='A+' order by date;")
            (z,)=c3.fetchone()
            d=("BLOOD DONATED TO",z,"\n\nDONOR ID:",del1,"\nDONOR NAME:",del2)
            do=Label(r12, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=10,y=20)
            m3.close()

    def donate_bn():
        global donate_bn
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        c.execute("select donor_id,donor_name from donors where blood_group='B-' order by date;")
        #(del1,del2)=c.fetchone()
        #m.commit()
        #m.close()
        #print(del1)

        global r13    
        r13=Toplevel(root2)
        r13.geometry('300x135-550+375')
        r13.title("B- BLOOD")
        r13.configure(background='IndianRed')
      
        if c.fetchone() is None:
            do=Label(r13, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (del1,del2)=c.fetchone()        
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            st="delete from donors where donor_id = {}".format(del1)
            c1.execute(st)
            m1.commit()
            c1.execute("select hospital_id, no_of_bags from requests where blood_group='B-' order by category,date;")
            (z,a,)=c1.fetchone()
            print(a)
            b=a-1
            print(b)
            m1.close()
            
            m2=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c2=m2.cursor()
            c2.execute("USE HAEMA") 
            #c2.execute("update requests set no_of_bags='%s' where blood_group='A-' and no_of_bags='%s'")%(b,a)
            #c2.commit()
            y1 = "update requests set no_of_bags=%s where blood_group='B-'  and hospital_id=%s"
            y2 = (b,z)
            c2.execute(y1, y2)
            m2.commit()

            m3=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c3=m3.cursor()
            c3.execute("USE HAEMA")
            c3.execute("select hospital_name from requests where blood_group='B-' order by date;")
            (z,)=c3.fetchone()
            d=("BLOOD DONATED TO",z,"\n\nDONOR ID:",del1,"\nDONOR NAME:",del2)
            do=Label(r13, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=10,y=20)
            m3.close()
        
    def donate_bp():
        global donate_bp
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        c.execute("select donor_id,donor_name from donors where blood_group='B+' order by date;")
        #(del1,del2)=c.fetchone()
        #m.commit()
        #m.close()
        #print(del1)
       
        global r14   
        r14=Toplevel(root2)
        r14.geometry('300x135-550+375')
        r14.title("B+ BLOOD")
        r14.configure(background='IndianRed')
      
        if c.fetchone() is None:
            do=Label(r14, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (del1,del2)=c.fetchone()        
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            st="delete from donors where donor_id = {}".format(del1)
            c1.execute(st)
            m1.commit()
            c1.execute("select hospital_id, no_of_bags from requests where blood_group='B+' order by category,date;")
            (z,a,)=c1.fetchone()
            print(a)
            b=a-1
            print(b)
            m1.close()
            
            m2=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c2=m2.cursor()
            c2.execute("USE HAEMA") 
            #c2.execute("update requests set no_of_bags='%s' where blood_group='A-' and no_of_bags='%s'")%(b,a)
            #c2.commit()
            y1 = "update requests set no_of_bags=%s where blood_group='B+' and hospital_id=%s"
            y2 = (b,z)
            c2.execute(y1, y2)
            m2.commit()

            m3=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c3=m3.cursor()
            c3.execute("USE HAEMA")
            c3.execute("select hospital_name from requests where blood_group='B+' order by date;")
            (z,)=c3.fetchone()
            d=("BLOOD DONATED TO",z,"\n\nDONOR ID:",del1,"\nDONOR NAME:",del2)
            do=Label(r14, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=10,y=20)
            m3.close()
        
    def donate_on():
        global donate_on
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        c.execute("select donor_id,donor_name from donors where blood_group='O-' order by date;")
        #(del1,del2)=c.fetchone()
        #m.commit()
        #m.close()
        #print(del1)

        global r15    
        r15=Toplevel(root2)
        r15.geometry('300x135-550+375')
        r15.title("O- BLOOD")
        r15.configure(background='IndianRed')
      
        if c.fetchone() is None:
            do=Label(r15, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (del1,del2)=c.fetchone()        
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            st="delete from donors where donor_id = {}".format(del1)
            c1.execute(st)
            m1.commit()
            c1.execute("select hospital_id, no_of_bags from requests where blood_group='O-' order by category,date;")
            (z,a,)=c1.fetchone()
            print(a)
            b=a-1
            print(b)
            m1.close()
            
            m2=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c2=m2.cursor()
            c2.execute("USE HAEMA") 
            #c2.execute("update requests set no_of_bags='%s' where blood_group='A-' and no_of_bags='%s'")%(b,a)
            #c2.commit()
            y1 = "update requests set no_of_bags=%s where blood_group='O-' and hospital_id=%s"
            y2 = (b,z)
            c2.execute(y1, y2)
            m2.commit()

            m3=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c3=m3.cursor()
            c3.execute("USE HAEMA")
            c3.execute("select hospital_name from requests where blood_group='O-' order by date;")
            (z,)=c3.fetchone()
            d=("BLOOD DONATED TO",z,"\n\nDONOR ID:",del1,"\nDONOR NAME:",del2)
            do=Label(r15, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=10,y=20)
            m3.close()


    def donate_op():
        global donate_op
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        c.execute("select donor_id,donor_name from donors where blood_group='O+' order by date;")
        #(del1,del2)=c.fetchone()
        #m.commit()
        #m.close()
        #print(del1) 
        
        global r16   
        r16=Toplevel(root2)
        r16.geometry('300x135-550+375')
        r16.title("O+ BLOOD")
        r16.configure(background='IndianRed')
     
        if c.fetchone() is None:
            do=Label(r16, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (del1,del2)=c.fetchone()        
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            st="delete from donors where donor_id = {}".format(del1)
            c1.execute(st)
            m1.commit()
            c1.execute("select hospital_id, no_of_bags from requests where blood_group='O+' order by category,date;")
            (z,a,)=c1.fetchone()
            print(a)
            b=a-1
            print(b)
            m1.close()
            
            m2=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c2=m2.cursor()
            c2.execute("USE HAEMA") 
            #c2.execute("update requests set no_of_bags='%s' where blood_group='A-' and no_of_bags='%s'")%(b,a)
            #c2.commit()
            y1 = "update requests set no_of_bags=%s where blood_group='O+' and hospital_id=%s"
            y2 = (b,z)
            c2.execute(y1, y2)
            m2.commit()

            m3=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c3=m3.cursor()
            c3.execute("USE HAEMA")
            c3.execute("select hospital_name from requests where blood_group='O+' order by date;")
            (z,)=c3.fetchone()
            d=("BLOOD DONATED TO",z,"\n\nDONOR ID:",del1,"\nDONOR NAME:",del2)
            do=Label(r16, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=10,y=20)
            m3.close()

    def donate_abn():
        global donate_abn
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        c.execute("select donor_id,donor_name from donors where blood_group='AB-' order by date;")
        #(del1,del2)=c.fetchone()
        #m.commit()
        #m.close()
        #print(del1)

        global r17    
        r17=Toplevel(root2)
        r17.geometry('300x135-550+375')
        r17.title("AB- BLOOD")
        r17.configure(background='IndianRed')
      
        if c.fetchone() is None:
            do=Label(r17, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (del1,del2)=c.fetchone()        
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            st="delete from donors where donor_id = {}".format(del1)
            c1.execute(st)
            m1.commit()
            c1.execute("select hospital_id, no_of_bags from requests where blood_group='AB-' order by category,date;")
            (z,a,)=c1.fetchone()
            print(a)
            b=a-1
            print(b)
            m1.close()
            
            m2=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c2=m2.cursor()
            c2.execute("USE HAEMA") 
            #c2.execute("update requests set no_of_bags='%s' where blood_group='A-' and no_of_bags='%s'")%(b,a)
            #c2.commit()
            y1 = "update requests set no_of_bags=%s where blood_group='AB-' and hospital_id=%s"
            y2 = (b,z)
            c2.execute(y1, y2)
            m2.commit()

            m3=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c3=m3.cursor()
            c3.execute("USE HAEMA")
            c3.execute("select hospital_name from requests where blood_group='AB-' order by date;")
            (z,)=c3.fetchone()
            d=("BLOOD DONATED TO",z,"\n\nDONOR ID:",del1,"\nDONOR NAME:",del2)
            do=Label(r17, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=10,y=20)
            m3.close()

    def donate_abp():
        global donate_abp
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        c.execute("select donor_id,donor_name from donors where blood_group='AB+' order by date;")
        #(del1,del2)=c.fetchone()
        #m.commit()
        #m.close()
        #print(del1)
        
        global r18
        r18=Toplevel(root2)
        r18.geometry('300x135-550+375')
        r18.title("AB+ BLOOD")
        r18.configure(background='IndianRed')
     
        if c.fetchone() is None:
            do=Label(r18, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (del1,del2)=c.fetchone()        
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            st="delete from donors where donor_id = {}".format(del1)
            c1.execute(st)
            m1.commit()
            c1.execute("select hospital_id, no_of_bags from requests where blood_group='AB+' order by category,date;")
            (z,a,)=c1.fetchone()
            print(a)
            b=a-1
            print(b)
            m1.close()
            
            m2=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c2=m2.cursor()
            c2.execute("USE HAEMA") 
            #c2.execute("update requests set no_of_bags='%s' where blood_group='A-' and no_of_bags='%s'")%(b,a)
            #c2.commit()
            y1 = "update requests set no_of_bags=%s where blood_group='AB+' and hospital_id=%s"
            y2 = (b,z)
            c2.execute(y1, y2)
            m2.commit()

            m3=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c3=m3.cursor()
            c3.execute("USE HAEMA")
            c3.execute("select hospital_name from requests where blood_group='AB+' order by date;")
            (z,)=c3.fetchone()
            d=("BLOOD DONATED TO",z,"\n\nDONOR ID:",del1,"\nDONOR NAME:",del2)
            do=Label(r18, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=10,y=20)
            m3.close()        
       
    def donate_bo():
        global donate_bo
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
        c=m.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        c.execute("select donor_id,donor_name from donors where blood_group='Bombay' order by date;")
        #(del1,del2)=c.fetchone()
        #m.commit()
        #m.close()
        #print(del1)
      
        global r19
        r19=Toplevel(root2)
        r19.geometry('300x135-550+375')
        r19.title("BOMBAY BLOOD")
        r19.configure(background='IndianRed')
   
        if c.fetchone() is None:
            do=Label(r19, text="BLOOD UNAVAILABLE.\nTRY LATER.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=0,y=50)
        else:
            (del1,del2)=c.fetchone()        
            m1=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c1=m1.cursor()
            c1.execute("USE HAEMA")
            st="delete from donors where donor_id = {}".format(del1)
            c1.execute(st)
            m1.commit()
            c1.execute("select hospital_id, no_of_bags from requests where blood_group='Bombay' order by category,date;")
            (z,a,)=c1.fetchone()
            print(a)
            b=a-1
            print(b)
            m1.close()
            
            m2=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c2=m2.cursor()
            c2.execute("USE HAEMA") 
            #c2.execute("update requests set no_of_bags='%s' where blood_group='A-' and no_of_bags='%s'")%(b,a)
            #c2.commit()
            y1 = "update requests set no_of_bags=%s where blood_group='Bombay' and hospital_id=%s"
            y2 = (b,z)
            c2.execute(y1, y2)
            m2.commit()

            m3=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')
            c3=m3.cursor()
            c3.execute("USE HAEMA")
            c3.execute("select hospital_name from requests where blood_group='Bombay' order by date;")
            (z,)=c3.fetchone()
            d=("BLOOD DONATED TO",z,"\n\nDONOR ID:",del1,"\nDONOR NAME:",del2)
            do=Label(r19, text=" ".join(d), bg="IndianRed",fg='white',width=32,font=("bold", 12))
            do.place(x=10,y=20)
            m3.close()        

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MANAGEMENT BUTTONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    

    def mgmt_view():
        label_0a = Label(root2, text="REQUESTS",width=20,font=("bold", 20),bg="IndianRed4",fg="white")
        label_0a.place(x=60,y=190)
        
        label_0b = Label(root2, text="Select blood group to view oldest donor ID.",font=(15),bg="IndianRed3",fg="white")
        label_0b.place(x=70,y=240)
        
        label_1a = Label(root2, text="Blood Group",font=("bold", 15),bg="IndianRed3",fg="white")
        label_1a.place(x=50,y=300)

        label_1b = Label(root2, text="No. of bags",font=("bold", 15),bg="IndianRed",fg="white")
        label_1b.place(x=270,y=300)

        Button(root2, text='A-',width=10,bg='IndianRed',fg='white',command=show_an).place(x=60,y=340)
        c.execute("select sum(no_of_bags) from requests where blood_group='A-';")
        an=c.fetchone()
        #print(an)
        label_2b = Label(root2, text=an,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_2b.place(x=280,y=340)

        Button(root2, text='A+',width=10,bg='IndianRed',fg='white',command=show_ap).place(x=60,y=370)
        c.execute("select sum(no_of_bags) from requests where blood_group='A+';")
        ap=c.fetchone()
        #print(ap)
        label_3b = Label(root2, text=ap,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_3b.place(x=280,y=370)

        Button(root2, text='B-',width=10,bg='IndianRed',fg='white',command=show_bn).place(x=60,y=400)
        c.execute("select sum(no_of_bags) from requests where blood_group='B-';")
        bn=c.fetchone()
        #print(bn)
        label_4b = Label(root2, text=bn,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_4b.place(x=280,y=400)

        Button(root2, text='B+',width=10,bg='IndianRed',fg='white',command=show_bp).place(x=60,y=430)
        c.execute("select sum(no_of_bags) from requests where blood_group='B+';")
        bp=c.fetchone()
        #print(bp)
        label_5b = Label(root2, text=bp,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_5b.place(x=280,y=430)

        Button(root2, text='O-',width=10,bg='IndianRed',fg='white',command=show_on).place(x=60,y=460)
        c.execute("select sum(no_of_bags) from requests where blood_group='O-';")
        on=c.fetchone()
        #print(on)
        label_6b = Label(root2, text=on,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_6b.place(x=280,y=460)

        Button(root2, text='O+',width=10,bg='IndianRed',fg='white',command=show_op).place(x=60,y=490)
        c.execute("select sum(no_of_bags) from requests where blood_group='O+';")
        op=c.fetchone()
        #print(op)
        label_7b = Label(root2, text=op,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_7b.place(x=280,y=490)

        Button(root2, text='AB-',width=10,bg='IndianRed',fg='white',command=show_abn).place(x=60,y=520)
        c.execute("select sum(no_of_bags) from requests where blood_group='AB-';")
        abn=c.fetchone()
        #print(abn)
        label_8b = Label(root2, text=abn,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_8b.place(x=280,y=520)

        Button(root2, text='AB+',width=10,bg='IndianRed',fg='white',command=show_abp).place(x=60,y=550)
        c.execute("select sum(no_of_bags) from requests where blood_group='AB+';")
        abp=c.fetchone()
        #print(abp)
        label_9b = Label(root2, text=abp,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_9b.place(x=280,y=550)

        Button(root2, text='BOMBAY',width=10,bg='IndianRed',fg='white',command=show_bo).place(x=60,y=580)
        c.execute("select sum(no_of_bags) from requests where blood_group='Bombay';")
        bo=c.fetchone()
        #print(bo)
        label_10b = Label(root2, text=bo,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_10b.place(x=280,y=580)
    ################################################################################################################

        label_0c = Label(root2, text="DONORS",width=20,font=("bold", 20),bg="IndianRed4",fg="white")
        label_0c.place(x=1060,y=190)
        label_0d = Label(root2, text="Select blood group to donate 1 blood bag.",font=(15),bg="IndianRed3",fg="white")
        label_0d.place(x=1070,y=240)

        label_1c = Label(root2, text="Blood Group",font=("bold", 15),bg="IndianRed3",fg="white")
        label_1c.place(x=1050,y=300)

        label_1d = Label(root2, text="No. of bags",font=("bold", 15),bg="IndianRed3",fg="white")
        label_1d.place(x=1270,y=300)

        Button(root2, text='A-',width=10,bg='IndianRed',fg='white',command=donate_an).place(x=1060,y=340)
        c.execute("select count(blood_group) from donors where blood_group='A-';")
        an=c.fetchone()
        #print(an)
        label_2d = Label(root2, text=an,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_2d.place(x=1280,y=340)

        Button(root2, text='A+',width=10,bg='IndianRed',fg='white',command=donate_ap).place(x=1060,y=370)
        c.execute("select count(blood_group) from donors where blood_group='A+';")
        ap=c.fetchone()
        #print(ap)
        label_3d = Label(root2, text=ap,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_3d.place(x=1280,y=370)

        Button(root2, text='B-',width=10,bg='IndianRed',fg='white',command=donate_bn).place(x=1060,y=400)
        c.execute("select count(blood_group) from donors where blood_group='B-';")
        bn=c.fetchone()
        #print(bn)
        label_4d = Label(root2, text=bn,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_4d.place(x=1280,y=400)

        Button(root2, text='B+',width=10,bg='IndianRed',fg='white',command=donate_bp).place(x=1060,y=430)
        c.execute("select count(blood_group) from donors where blood_group='B+';")
        bp=c.fetchone()
        #print(bp)
        label_5d = Label(root2, text=bp,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_5d.place(x=1280,y=430)

        Button(root2, text='O-',width=10,bg='IndianRed',fg='white',command=donate_on).place(x=1060,y=460)
        c.execute("select count(blood_group) from donors where blood_group='O-';")
        on=c.fetchone()
        #print(on)
        label_6d = Label(root2, text=on,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_6d.place(x=1280,y=460)

        Button(root2, text='O+',width=10,bg='IndianRed',fg='white',command=donate_op).place(x=1060,y=490)
        c.execute("select count(blood_group) from donors where blood_group='O+';")
        op=c.fetchone()
        #print(op)
        label_7d = Label(root2, text=op,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_7d.place(x=1280,y=490)

        Button(root2, text='AB-',width=10,bg='IndianRed',fg='white',command=donate_abn).place(x=1060,y=520)
        c.execute("select count(blood_group) from donors where blood_group='AB-';")
        abn=c.fetchone()
        #print(abn)
        label_8d = Label(root2, text=abn,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_8d.place(x=1280,y=520)

        Button(root2, text='AB+',width=10,bg='IndianRed',fg='white',command=donate_abp).place(x=1060,y=550)
        c.execute("select count(blood_group) from donors where blood_group='AB+';")
        abp=c.fetchone()
        #print(abp)
        label_9d = Label(root2, text=abp,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_9d.place(x=1280,y=550)

        Button(root2, text='BOMBAY',width=10,bg='IndianRed',fg='white',command=donate_bo).place(x=1060,y=580)
        c.execute("select count(blood_group) from donors where blood_group='Bombay';")
        bo=c.fetchone()
        #print(bo)
        label_10d = Label(root2, text=bo,width=10,font=("bold", 10),bg="IndianRed",fg="white")
        label_10d.place(x=1280,y=580)


        root2.mainloop()
    mgmt_view()
    
    #manage()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~LOGIN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def login():

    l1=['admin1','admin2']
    l2=['123haema','123haema']
    lg=Toplevel(root)
    lg.geometry('500x250')
    lg.title("Login Screen")
    lg.configure(background='black')
    global login
    global username
    global password
    global un_login
    global pwd_login
    global un
    global pwd
    
    username = StringVar()
    password = StringVar()
    un=username.get()
    pwd=password.get()
 
    heading=Label(lg, text="ENTER DETAILS", bg="IndianRed",width=32,font=("bold", 20))
    heading.place(x=0,y=50)
    
    unlabel = Label(lg, text="Username: ",bg="black",fg="white")
    unlabel.place(x=160,y=120)
    
    un_login = Entry(lg, textvariable=username)
    un_login.place(x=240,y=120)
   
    pwdlabel = Label(lg, text="Password: ",bg="black",fg="white")
    pwdlabel.place(x=160,y=160)
    
    pwd_login = Entry(lg, textvariable=password, show='*')
    pwd_login.place(x=240,y=160)
    
    
    def verify():
        global verify
        l1=['admin']
        l2=['123haema']
        print(un)
        i=0
        if username.get() in l1:
            if password.get() in l2:
                rt1 = Toplevel(lg)
                rt1.geometry('300x200')
                rt1.title("LOGIN VERIFIED")
                rt1.configure(background='IndianRed')
                v1=Label(rt1, text="LOGIN VERIFIED!", bg="IndianRed",fg='white',width=22,font=("bold", 18))
                v1.place(x=0,y=50)
                v2=Label(rt1, text="Click to continue.", bg="IndianRed",fg='white',width=34,font=("bold", 12))
                v2.place(x=0,y=90)
                Button(rt1, text='CONTINUE',width=20,bg='white',fg='IndianRed',command=manage).place(x=75,y=120)

                '''elif password.get()!=l2[count]:
                    count=count+1
                    print(count)'''
            
            else:
                rt2 = Toplevel(lg)
                rt2.geometry('275x125')
                rt2.title("ERROR")
                rt2.configure(background='IndianRed')
                m=Label(rt2, text="INCORRECT PASSWORD!", bg="IndianRed",fg='white',width=32,font=("bold", 12))
                m.place(x=0,y=50)

        else:
            rt3 = Toplevel(lg)
            rt3.geometry('275x125')
            rt3.title("ERROR")
            rt3.configure(background='IndianRed')
            m=Label(rt3, text="INCORRECT USERNAME!", bg="IndianRed",fg='white',width=32,font=("bold", 12))
            m.place(x=0,y=50)
            
    Button(lg, text="LOGIN", width=10, height=1, bg="IndianRed",command=verify).place(x=205,y=210)
   

#===============================================================================================================================
#===============================================================================================================================
#========================================================DONATE=================================================================
#===============================================================================================================================
#===============================================================================================================================

def donate():

    global donate
    root3 = Toplevel(root)
    root3.geometry('500x500')
    root3.title("Donation Form")
    root3.configure(background='black')
    d_id=StringVar()
    d_name=StringVar()
    d_age= IntVar()
    d_grp=StringVar()
    #d_no= IntVar()
    d_date= StringVar()
    
    def donate_database():
        donor_id=d_id.get()
        donor_name=d_name.get()
        age=d_age.get()
        bloodgrp=d_grp.get()
        datenow=d_date.get()
        m=mysql.connector.connect(host="localhost",user="root",passwd="necpuc",auth_plugin='mysql_native_password')        
    #    with m:
        c=m.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS HAEMA")
        c.execute("USE HAEMA")
        c.execute("CREATE TABLE IF NOT EXISTS DONORS(Donor_ID VARCHAR(3), Donor_Name VARCHAR(20), Age INTEGER(2), Blood_Group VARCHAR(10), Date VARCHAR(12))")
        c.execute("INSERT INTO DONORS VALUES (%s,%s,%s,%s,%s)",(donor_id,donor_name,age,bloodgrp,datenow))
        m.commit()
        global d
        d=Toplevel(root3)
        d.geometry('275x135')
        d.title("SUCCESS")
        d.configure(background='IndianRed')
                    
        d1=Label(d, text="DONATION SUCCESSFUL.", bg="IndianRed",fg='white',width=32,font=("bold", 12))
        d1.place(x=0,y=50)
    #=====================================================================================   
    label_0 = Label(root3, text="DONATION FORM",width=20,font=("bold", 20),bg="IndianRed",fg="white")
    label_0.place(x=90,y=50)
    #=====================================================================================
    label_2 = Label(root3, text="Donor ID",width=20,font=("bold", 10),bg="black",fg="white")
    label_2.place(x=80,y=130)
    entry_2 = Entry(root3,textvar = d_id)
    entry_2.place(x=240,y=130)
    #=======================================================================================
    label_3 = Label(root3, text="Donor Name",width=20,font=("bold", 10),bg="black",fg="white")
    label_3.place(x=80,y=180)
    entry_3 = Entry(root3,textvar=d_name)
    entry_3.place(x=240,y=180)
    #=========================================================================================
    label_4 = Label(root3, text="Blood Group",width=20,font=("bold", 10),bg="black",fg="white")
    label_4.place(x=80,y=230)
    list1 = ['A-','A+','B-','B+','O-','O+','AB-','AB+','Bombay'];
    droplist=OptionMenu(root3,d_grp, *list1)
    droplist.config(width=15)
    d_grp.set('SELECT') 
    droplist.place(x=240,y=230)
    #=============================================================================================
    label_5 = Label(root3, text="Age",width=20,font=("bold", 10),bg="black",fg="white")
    label_5.place(x=80,y=280)
    spin = Spinbox(root3, from_=18, to=60, textvar=d_age)
    #spin.pack()
    spin.place(x=240,y=280)
    #=========================================================================================
    label_6 = Label(root3, text="Date of Donation (YYYY-MM-DD)",width=25,font=("bold", 10),bg="black",fg="white")
    label_6.place(x=12,y=330)
    entry_6 = Entry(root3, textvar=d_date)
    entry_6.place(x=240,y=330)
    #==================================================================================================
    Button(root3, text='Submit',width=20,bg='IndianRed',fg='white',command=donate_database).place(x=170,y=390)
    root3.mainloop()
    
#===============================================================================================================================
#===============================================================================================================================
#=======================================================TEXT FILES==============================================================
#===============================================================================================================================
#===============================================================================================================================
    
def about():
    global about
    global root_a
    root_a=Toplevel(root)
    root_a.geometry('1200x600') 
    root_a.configure(background='black')
    global img4
    img4 = PhotoImage(file="haema.png").subsample(3,3)
    #r=Toplevel(root2)
    Label(root_a,image=img4, width=0, height=0,border=0).place(x=10,y=5)
    Label(root_a, text="ABOUT US",width=33,font=("Times New Roman", 40),bg="IndianRed4",fg="white").place(x=400,y=25)

    a=" "
    str=" "
    myfile1=open('about.txt','r')
    while str:
        str=myfile1.readline()
        a=a+str
    myfile1.close()
    label_a = Label(root_a, text=a, justify='left', relief='solid', borderwidth=1,bg='black',font=("Times New Roman", 15),fg="white")
    label_a.place(x=20,y=115)

#===============================================================================================================================
  

def haema_help():
    global haema_help
    global root_h
    root_h=Toplevel(root)
    root_h.geometry('1200x1200')
    root_h.title("Where")
    root_h.configure(background='black')
    canvas = Canvas(root_h, width = 1900, height = 900, bg='black') 
    #canvas.pack(expand=YES)
    global img5
    img5 = PhotoImage(file="haema.png").subsample(3,3)
    #r=Toplevel(root2)
    Label(root_h,image=img5, width=0, height=0,border=0).place(x=10,y=5)
    Label(root_h, text="HELP",width=33,font=("Times New Roman", 40),bg="IndianRed4",fg="white").place(x=400,y=25)

    #buttonw =Button(root_h,image=i5, bg='IndianRed1',borderwidth=6,relief="raised",command=abc)
    #buttonw.place(x=180, y=70, anchor="center")
    #buttonw_ttp = CreateToolTip(button1,'Select to request for blood.')

    a=" "
    str=" "
    myfile1=open('help.txt','r')
    while str:
        str=myfile1.readline()
        a=a+str
    myfile1.close()
    label_h = Label(root_h, text=a, justify='left', relief='solid', borderwidth=1,bg='black',font=("Times New Roman", 15),fg="white")
    label_h.place(x=20,y=125)

#===============================================================================================================================

def contact():
    global contact
    global root_c
    root_c=Toplevel(root)
    root_c.geometry('850x600')
    root_c.title("Contact Us")
    root_c.configure(background='black')
    a=" "
    str=" "
    myfile1=open('contact.txt','r')
    while str:
        str=myfile1.readline()
        a=a+str
    myfile1.close()
    global img6
    img6 = PhotoImage(file="haema.png").subsample(3,3)
    #r=Toplevel(root2)
    Label(root_c,image=img6, width=0, height=0,border=0).place(x=10,y=5)
    Label(root_c, text="CONTACT US",width=18,font=("Times New Roman", 40),bg="IndianRed4",fg="white").place(x=350,y=25)

    label_c = Label(root_c, text=a, justify='left', relief='solid', borderwidth=1,bg='black',font=("Times New Roman", 15),fg="white")
    label_c.place(x=20,y=115)
    print()
    
#==============================================================================================================================
#===============================================================================================================================
#===============================================================================================================================
#===============================================================================================================================


button1 =Button(root, text="REQUEST", bg='IndianRed1',font=("Times New Roman Bold", 30,),fg="white",borderwidth=6,relief="raised",command=request)
button1.place(x=250, y=630, anchor="center")

button2 = Button(root, text="MANAGEMENT",bg='IndianRed1',font=("Times New Roman Bold", 30),fg="white",borderwidth=6,relief="raised",command=login)
button2.place(x=720, y=630, anchor="center")

button3 = Button(root, text="DONATE", bg='IndianRed1',font=("Times New Roman Bold", 30,),fg="white",borderwidth=6,relief="raised",command=donate)
button3.place(x=1190, y=630, anchor="center")

button4 = Button(root, text='ABOUT',bg='black',font=("Times New Roman Bold", 11),fg="white",borderwidth=2,relief="raised",command=about)
button4.place(x=1075, y=50, anchor="center")

button5 = Button(root, text='HELP',bg='black',font=("Times New Roman Bold", 11),fg="white",borderwidth=2,relief="raised",command=haema_help)
button5.place(x=1200, y=50, anchor="center")

button6 = Button(root, text='CONTACT US',bg='black',font=("Times New Roman Bold", 11),fg="white",borderwidth=2,relief="raised",command=contact)
button6.place(x=1325, y=50, anchor="center")



#m.close()


