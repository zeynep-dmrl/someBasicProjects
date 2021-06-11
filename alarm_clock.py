from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m%Y")
        print("The set date time is: ",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake Up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)



clock = Tk()

clock.title("Alarm Clock")
clock.geometry("550x550")
clock.config(bg="#33334d")

hrt = str(time.strftime("%H"))
mint = str(time.strftime("%M"))
sect = str(time.strftime("%S"))

hour_label = Label(clock,text=hrt,font="Arial",bg="#ff9900",fg="white")
hour_label.place(x=100,y=80,width=100,height=100)
hr_label = Label(clock,text="HOUR",font=("Arial",10,"bold"),bg="#ff9900",fg="white")
hr_label.place(x=100,y=190,width=100,height=50)

min_label = Label(clock,text=mint,font="Arial",bg="#009999",fg="white")
min_label.place(x=220,y=80,width=100,height=100)
min_lbl = Label(clock,text="MINUTE",font=("Arial",10,"bold"),bg="#009999",fg="white")
min_lbl.place(x=220,y=190,width=100,height=50)

sec_label = Label(clock,text=sect,font="Arial",bg="#99004d",fg="white")
sec_label.place(x=340,y=80,width=100,height=100)
sec_lbl = Label(clock,text="SECOND",font=("Arial",10,"bold"),bg="#99004d",fg="white")
sec_lbl.place(x=340,y=190,width=100,height=50)


Label(clock,text = "Hour",font=60,bg="#ffece6",fg="#cc3300",width=5,height=2).place(x = 150,y = 280)
Label(clock,text = "Min",font=60,bg="#ffece6",fg="#cc3300",width=5,height=2).place(x = 220, y = 280)
Label(clock,text = "Sec",font=60,bg="#ffece6",fg="#cc3300",width=5,height=2).place(x = 290, y = 280)

setYourAlarm = Label(clock,text = "When to \nwake you up",fg="#660033",relief = "solid",font=("Helevetica",10,"bold"),width=12,height=5)
setYourAlarm.place(x=20, y=280)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(clock,textvariable = hour,bg = "#ffc6b3",width = 10).place(x=150,y=340,height=30)
minTime= Entry(clock,textvariable = min,bg = "#ffc6b3",width = 10).place(x=220,y=340,height=30)
secTime = Entry(clock,textvariable = sec,bg = "#ffc6b3",width = 10).place(x=290,y=340,height=30)

submit = Button(clock,text = "Set Alarm",fg="white",bg="#206040",width = 15,height = 2,font=("Arial",10,"bold"),command = actual_time).place(x =220,y=400)

clock.mainloop()
