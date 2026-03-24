from tkinter import *
from PIL import Image,ImageTk # type: ignore
from clockwise import ClockWise

window = Tk()
window.config(background="#F8F9FE")
clock_frame = Canvas(width=500,height=500,bg="#F8F9FE")
clock_frame.pack()

#clock frame
original_img = Image.open("clock_frame.png")
tk_img = ImageTk.PhotoImage(original_img)
clock_frame.create_image(250, 250, image=tk_img)
#end

Second = ClockWise(clock_frame,"second",[251,300,251,90],"black",1)
Second.Active(180,[251,250])
Minute = ClockWise(clock_frame,"minute",[251,280,251,105],"black",3)
Minute.Active(180,[251,250])
Hour = ClockWise(clock_frame,"hour",[251,270,251,120],"black",8)
Hour.Active(180,[251,250])

window.mainloop()