from tkinter import *
from PIL import Image, ImageTk
from clockwise import ClockWise
import time

window = Tk()
window.title("Clock")

clock = Canvas(window, width=500, height=500, bg="white")
clock.pack()

#Analog Clock frame

img = Image.open("clock_frame.png")
img = img.resize((500, 500))
analog_clock_photo = ImageTk.PhotoImage(img)
clock.create_image(250, 250, image=analog_clock_photo)

shadow = clock.create_text(
    253, 143,
    text="",
    fill="black",
    font=("Arial", 40, "bold")
)
#Degital Clock
digital_clock = clock.create_text(
    250, 140,
    text="",
    fill="#FFFFFF",
    font=("Arial", 40,"bold")
)

def updateTime():
    nowTime = time.strftime("%I:%M", time.localtime())

    clock.itemconfig(digital_clock, text=nowTime)
    clock.itemconfig(shadow, text=nowTime)

    window.after(1000, updateTime)

updateTime()
#Analog Clock wise

hour = ClockWise(clock,"hour","rectengular",[250,140,240,250,250,270,260,250],"#000000",0)#canvas,title,shape,cordinate,color,width
hour.Active([250,250])

minute = ClockWise(clock,"minute","rectengular",[250,110,245,250,250,275,255,250],"#0000FF",0)#canvas,title,shape,cordinate,color,width
minute.Active([250,250])

second = ClockWise(clock,"second","line",[250,90,250,280],"#FF0000",2)#canvas,title,shape,cordinate,color,width
second.Active([250,250])


window.mainloop()
