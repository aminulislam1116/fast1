import datetime
import time
from tkinter import *
screen=Tk()
screen.title('Digital clock')
screen.geometry("700x500")
screen.resizable(0,0)

screen.configure(bg="black")
f1=Frame(screen,borderwidth=3,bg='red',relief=SUNKEN)
f1.pack(side=TOP,fill="y")

t1=Label(f1,text=' Python Digital Clock',font=("Arial",30),fg='red',bg='green')

t1.pack()

def clock():
    t2=time.strftime("%I:%M:%S %p")
    #f2=Frame(screen,borderwidth=4,bg='red',relief=SUNKEN)
    #f2.pack()
    t3=Label(screen,text=t2,font=('ds digital',40,'bold'),fg='light green',bg='green')
    t3.after(200,clock)
    t3.place(x=150,y=200)
    t4=datetime.date.today()
    t5=Label(screen,text=t4.year,font=('ds digitl',40,'bold'),fg='light green',bg='black').place(x=150,y=75)
    t6=Label(screen,text=t4.month,font=('ds digitl',40,'bold'),fg='light green',bg='black').place(x=300,y=75)
    t7=Label(screen,text=t4.day,font=('ds digitl',40,'bold'),fg='light green',bg='black').place(x=400,y=75)
    t8=Label(screen,text="YEAR",font=('ds digitl',15,'bold'),fg='olivedrab1',bg='black').place(x=180,y=140)
    t9=Label(screen,text="MONTH",font=('ds digitl',15,'bold'),fg='olivedrab1',bg='black').place(x=290,y=140)
    t10=Label(screen,text="DATE",font=('ds digitl',15,'bold'),fg='olivedrab1',bg='black').place(x=405,y=140)
    t11=Label(screen,text="HOUR",font=('ds digitl',10,'bold'),fg='white',bg='green').place(x=160,y=260)
    t12=Label(screen,text="MIN",font=('ds digitl',10,'bold'),fg='white',bg='green').place(x=235,y=260)
    t13=Label(screen,text="SEC",font=('ds digitl',10,'bold'),fg='white',bg='green').place(x=315,y=260)
    t14=Label(screen,text="Create by:",font=('ds digitl',10,'bold'),fg='white',bg='green').place(x=530,y=460)

    t15 = Label(screen, text="  AMINUL", font=('ds digitl', 8, 'bold'), fg='red', bg='green').place(x=601, y=480)

clock()

screen.mainloop()