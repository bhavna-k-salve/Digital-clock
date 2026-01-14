from tkinter import *
import datetime

#print(datetime.datetime.now())

def date_time():
  time=datetime.datetime.now()
  hr=time.strftime('%I')
  mi=time.strftime('%M')
  sec =time.strftime('%S')
  am=time.strftime('%p')
  date=time.strftime('%d')
  month=time.strftime('%m')
  year=time.strftime('%Y')
  day=time.strftime('%A')  
  
  lab_hr.config(text=hr)
  lab_mn.config(text=mi)
  lab_sc.config(text=sec)
  lab_am.config(text=am)
  lab_date.config(text=date)
  lab_mo.config(text=month)
  lab_year.config(text=year)
  lab_day.config(text=day)
 
  lab_hr.after(200,date_time)
  

clock = Tk()
clock.title("   digital clock")
clock.geometry('1000x500')
clock.config(bg='black')

lab_hr=Label(clock,text="00",font=('Digital-7',100,"bold"),bg='black',fg='red')
lab_hr.place(x=250,y=175,height=150,width=120)
lab_hr_txt=Label(clock,text="Time",font=('time new roman',30,"bold"),bg='black',fg='white')
lab_hr_txt.place(x=80,y=230,height=60,width=100)

lab_mn=Label(clock,text="00",font=('Digital-7',100,"bold"),bg='black',fg='red')
lab_mn.place(x=450,y=175,height=150,width=120)
# lab_mn_txt=Label(clock,text="min",font=('time new roman',30,"bold"),bg='black',fg='red')
# lab_mn_txt.place(x=340,y=190,height=40,width=100)

lab_sc=Label(clock,text="00",font=('Digital-7',100,"bold"),bg='black',fg='red')
lab_sc.place(x=650,y=175,height=150,width=120)
# lab_sc_txt=Label(clock,text="sec",font=('time new roman',30,"bold"),bg='black',fg='red')
# lab_sc_txt.place(x=560,y=190,height=40,width=100)

lab_am=Label(clock,text="00",font=('time new roman',40,"bold"),bg='black',fg='white')
lab_am.place(x=790,y=230,height=70,width=70)
# lab_am_txt=Label(clock,text="am/pm",font=('time new roman',22,"bold"),bg='black',fg='red')
# lab_am_txt.place(x=780,y=190,height=40,width=100)

#date

lab_date=Label(clock,text="00",font=('Digital-7',60,"bold"),bg='black',fg='red')
lab_date.place(x=150,y=50,height=150,width=100)
lab_date_txt=Label(clock,text="Date",font=('time new roman',20,"bold"),bg='black',fg='white')
lab_date_txt.place(x=240,y=125,height=30,width=70)

lab_mo=Label(clock,text="00",font=('DIgital-7',60,"bold"),bg='black',fg='red')
lab_mo.place(x=340,y=50,height=150,width=100)
lab_mo_txt=Label(clock,text="Month",font=('time new roman',20,"bold"),bg='black',fg='white')
lab_mo_txt.place(x=435,y=125,height=30,width=100)

lab_year=Label(clock,text="00",font=('Digital-7',60,"bold"),bg='black',fg='red')
lab_year.place(x=560,y=50,height=150,width=250)
lab_year_txt=Label(clock,text="Year",font=('time new roman',20,"bold"),bg='black',fg='white')
lab_year_txt.place(x=760,y=125,height=30,width=80)

lab_day=Label(clock,text="00",font=('time new roman',60,"bold"),bg='black',fg='red')
lab_day.place(x=400,y=350,height=110,width=500)
lab_day_txt=Label(clock,text="Day",font=('time new roman',30,"bold"),bg='black',fg='white')
lab_day_txt.place(x=250,y=370,height=60,width=80)


date_time()

clock.mainloop()


