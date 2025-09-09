import tkinter as Tk
from tkinter import font,filedialog
from datetime import time,timedelta,datetime
import playsound
import threading
import time

root = Tk.Tk()
root.geometry("360x400")
root.title("Herambha Alarm")
root.config(bg="lightblue")

music = None
     
Heading = Tk.Label(root,text="Alarm",font=("Arial",24),background="orange")
Heading.place(relx=0.5,rely=0.1,anchor="center")

instruct1 = Tk.Label(root,text='Set Time ',font=("Arial",14),background="orange")
instruct1.place(relx=0.2,rely=0.2)

hour = Tk.Label(root, text='H:', font=('Arial', 10, 'bold'),background='yellow')
hour.place(relx=0.2, rely=0.27)

hour_Enter = Tk.Spinbox(root, from_=0, to=12, width=4)
hour_Enter.place(relx=0.25, rely=0.27)

# Minute Label and Spinbox
minute = Tk.Label(root, text='M:', font=('Arial', 10, 'bold'),background='yellow')
minute.place(relx=0.4, rely=0.27)

min_enter = Tk.Spinbox(root, from_=0, to=59, width=4)
min_enter.place(relx=0.45, rely=0.27)

# Second Label and Spinbox
sec = Tk.Label(root, text='S:', font=('Arial', 10, 'bold'),background='yellow')
sec.place(relx=0.6, rely=0.27)

sec_enter = Tk.Spinbox(root, from_=0, to=59, width=4)
sec_enter.place(relx=0.65, rely=0.27)

Music_label = Tk.Label(root,text='Select Song : ',font=('Arial',14,'bold'),background='orange')
Music_label.place(relx=0.3,rely=0.5)

def location():
    global music
    
    music = filedialog.askopenfilename(title='Select file')



music_btn = Tk.Button(root,text='Choose Song',font=('Arial',10,'bold'),command=location,background='gray')
music_btn.place(relx=0.3,rely=0.6)

def play_song():
    if music:
        playsound.playsound(music)


def Start_alarm():
    h = int(hour_Enter.get())
    m = int(min_enter.get())
    s = int(sec_enter.get())

    alarm_time = datetime.now() + timedelta(hours=h, minutes=m, seconds=s)

    def check_alarm():
        while True:
            now = datetime.now()
            if now >= alarm_time:
                play_song()
                break
            time.sleep(1)

    threading.Thread(target=check_alarm).start()

Start_btn = Tk.Button(root,text='Start',font=('Arial',20,'bold'),background='cyan',command=Start_alarm)
Start_btn.place(relx=0.4,rely=0.8)

root.mainloop()