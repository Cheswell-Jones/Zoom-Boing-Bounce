from guizero import *
import pygame

def zoom():
      pygame.mixer.music.load('zoom.mp3')
      pygame.mixer.music.play(1)
def boing():
      pygame.mixer.music.load('boing.mp3')
      pygame.mixer.music.play(1)
def bounce():
      pygame.mixer.music.load('bounce.mp3')
      pygame.mixer.music.play(1)

#-----main----
pygame.init()  
app = App("Zoom, boing,bounce",height=210,width=620,layout="grid")
zoomButton = PushButton(app,text="zoom",height=200,width=200,grid=[0,0],image="zoom.png",command=zoom)
boingButton = PushButton(app,text="boing",height=200,width=200,grid=[1,0],image="boing.png",command=boing)
bounceButton = PushButton(app,text="bounce",height=200,width=200,grid=[2,0],image="bounce.png",command=bounce)
