from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title("typing speed")
root.geometry('800x600')

root.configure(bg='black')
words=['love','balo','sunar','printing','droupm','simple','clever','industry','essential','softer','version','ipsum']
random.shuffle(words)


def welcomelabel():
    global count,sliderwrod
    text='wellcome to typing speed'
    if (count>=len(text)):
        count=0
        sliderwrod=''
    sliderwrod += text[count]
    count += 1
    titlelabel.configure(text=sliderwrod)
    titlelabel.after(150,welcomelabel)

def startgame(event):
    global score,miss
    if (timeleft == 60):
        time()
    gamepd.configure(text='enjoy the game ')
    if (worldentry.get()==worldlabel['text']):
        score+=1
        scl.configure(text=score)

    else:
        miss+=1
    random.shuffle(words)
    worldlabel.configure(text=words[0])

    worldentry.delete(0,END)


def time():
    global timeleft,score,miss
    if (timeleft > 11):
        pass
    else:
        tcl.configure(fg='red')
    if (timeleft > 0):
        timeleft -= 1
        tcl.configure(text=timeleft)
        tcl.after(1000,time)

    else:
        gamepd.configure(text='hit={} | miss={} | total score = {}'.format(score,miss,score-miss))
        notific=messagebox.askretrycancel('notification','for play again please hit the retry button')
        if(notific==True):
            score=0
            timeleft=60
            miss=0
            tcl.configure(text=timeleft)
            worldlabel.configure(text=words[0])
            scl.configure(text=score)

score=0
miss=0
timeleft=60
count=0
sliderwrod=''

#root.mainloop()
titlelabel = Label(root, text="",
                   font=('arial', 30, 'italic bold'),  bg='black', fg='green', width=33)
titlelabel.place(x=10,y=10)
welcomelabel()

scorelabel=Label(root, text="Your score :",
                 font=('arial', 30),  bg='black', fg='white')
scorelabel.place(x=10,y=100)

scl=Label(root,text=score,
          font=('arial', 30),  bg='black', fg='white')
scl.place(x=60,y=180)
tl=Label(root,text='Time left',
         font=('arial', 30),  bg='black', fg='white')
tl.place(x=600,y=100)
tcl=Label(root,text=timeleft,font=('arial', 30),  bg='black', fg='white')
tcl.place(x=660,y=180)
worldlabel=Label(root,text=words[0],font=('arial', 30),  bg='black', fg='blue')
worldlabel.place(x=250,y=200)
#entry section
worldentry=Entry(root,font=('arial', 25, 'italic bold'),bd=10,justify='center')
worldentry.focus_set()
worldentry.place(x=200,y=300)


#game detal
gamepd=Label(root,text='type world and entry buton',
             font=('arial', 30),  bg='black', fg='powder blue')
gamepd.place(x=100,y=450)

root.bind('<Return>',startgame)
root.mainloop()