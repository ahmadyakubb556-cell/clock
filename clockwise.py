import math
import time

class ClockWise:
    def __init__(self,canvas,title,cordinate,color,width):

        self.canvas = canvas
        self.title = title
        self.cordinate = cordinate
        self.width = width
        self.color = color
        self.canvas.create_line(self.cordinate[0],self.cordinate[1],self.cordinate[2],self.cordinate[3],width=self.width,tags=self.title,fill=self.color)

    def Active(self,rotationDegree,focuspoint):
        
        module = time.localtime().tm_hour % 12
        second = time.localtime().tm_sec
        minute = time.localtime().tm_min
        hour = module if module != 0 else 12

        rotationDegree = (second * 6) if self.title == "second" else (minute * 6) + (0.1 * second) if self.title == "minute" else (hour*30) + (0.5*minute)
        #              =    --------------------------------      -------------------------------------------------------     --------------------------
        #              =               second                                              minute                                    hour

        angle = math.radians(rotationDegree)

        x1 = self.cordinate[0]
        y1 = self.cordinate[1]
        x2 = self.cordinate[2]
        y2 = self.cordinate[3]

        cx = focuspoint[0]
        cy = focuspoint[1]

        rx1 = cx + (x1 - cx) * math.cos(angle) - (y1 - cy) * math.sin(angle)
        ry1 = cy + (x1 - cx) * math.sin(angle) + (y1 - cy) * math.cos(angle)

        rx2 = cx + (x2 - cx) * math.cos(angle) - (y2 - cy) * math.sin(angle)
        ry2 = cy + (x2 - cx) * math.sin(angle) + (y2 - cy) * math.cos(angle)

        self.canvas.delete(self.title)

        self.canvas.create_line(rx1,ry1,rx2,ry2,width=self.width,tags=self.title,fill=self.color)
        self.canvas.create_oval(241,240,261,260,fill="black")
        self.canvas.after(1000, lambda: self.Active(rotationDegree, focuspoint))
