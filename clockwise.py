import math
import time
import pygame

def get_degree_of_time(title):
        
    module = time.localtime().tm_hour % 12
    second = time.localtime().tm_sec
    minute = time.localtime().tm_min
    hour = module if module != 0 else 12
        
    if title == "second":
        rotationDegree = (second * 6) 
    elif title == "minute":
        rotationDegree = (minute * 6) + (0.1 * second)
    else:
        rotationDegree = (hour * 30) + (0.5 * minute)
            
    return rotationDegree

def rotate(cordinate,focuspoint,rotationDegree):
            
    angle = math.radians(rotationDegree)
            
    cx,cy = focuspoint
            
    new_cordinate = []
            
    for i in range(0,len(cordinate),2):
                
        x = cordinate[i]
        y = cordinate[i+1]
                
        new_x = cx + (x - cx) * math.cos(angle) - (y - cy) * math.sin(angle)
        new_y = cy + (x - cx) * math.sin(angle) + (y - cy) * math.cos(angle)
                
        new_cordinate.extend([new_x,new_y])
                
    return new_cordinate
        

class ClockWise:
    
    def __init__(self,canvas,title,shape,cordinate,color,width):

        self.canvas = canvas
        self.title = title
        self.cordinate = cordinate
        self.width = width
        self.color = color
        self.shape = "line" if shape == "line" else "polygon"
        self.function = getattr(self.canvas,f"create_{self.shape}")
        
        
        self.function(*tuple(self.cordinate),width = self.width,tags = self.title,fill = self.color)
        
    def Active(self,focuspoint):

        rotation_sound = "clock_sound.mp3"

        pygame.mixer.init()
        pygame.mixer.music.load(rotation_sound)
        pygame.mixer.music.play()
        rotationDegree = get_degree_of_time(self.title)
        new_cordinate = tuple(rotate(self.cordinate,focuspoint,rotationDegree))
       
        self.canvas.delete(self.title)

        self.function(*new_cordinate,width = self.width,tags = self.title,fill = self.color)
        
        
        self.canvas.after(1000, lambda: self.Active(focuspoint))
