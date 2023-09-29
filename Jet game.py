import keyboard
import time
import random
import pygame
import os
import sys

pygame.init()

def L_ctrl() :
  print("Left Arrow Pressed")
  global Rocket_Position
  if Rocket_Position > -3 :
    Rocket_Position = Rocket_Position - 1     
  else :
     Rocket_Position = 3
  print("Rocket Position :- ",Rocket_Position)

def R_ctrl() :
  print("Right Arrow Pressed")
  global Rocket_Position
  if Rocket_Position < 3 :
     Rocket_Position = Rocket_Position + 1
  else :    
    Rocket_Position = -3
  print("Rocket Position :- ",Rocket_Position)

def Rocket_Pos() :
   print("Start to Navigate :-\n")
   Exiter = True
   while Exiter : 
       if keyboard.is_pressed("Left Arrow") :    
           L_ctrl()
           Exiter = False
           return True    
       elif keyboard.is_pressed("Right Arrow") :  
           R_ctrl()
           Exiter = False
           return True
       elif keyboard.is_pressed("Down Arrow") :
           print("Rocket Position :- ",Rocket_Position)
           Exiter = False
           return True
       elif keyboard.is_pressed("esc") : 
           global running
           running = False
           print("<<<----The End---->>>")
           return False
       elif keyboard.is_pressed("ctrl + alt + s") : 
           global Score
           Score = Score + 10
           Exiter = False
           return True
       
def Object_Int_Pos() :
    global Object_Position
    Object_Position = complex(random.randint(-3,3),0)

def Object_Pos() :
    global Object_Position
    c = complex(0,1)
    Object_Position = Object_Position + c
 
def Obj_Collusion_Check() :
    global Score
    if Rocket_Position == int(Object_Position.real) and int(Object_Position.imag) == 4 :
       Score = Score + 1 
       print("Score is :- ",Score)
  
def Coordinate() :
    global x1,x2,y1,y2
    x1 = 432 + (96*Rocket_Position)
    y1 = 432
    x2 = 432 + int(Object_Position.real)*96
    if int(Object_Position.imag) == 5 : 
       y2 = int(Object_Position.imag-1)*108
    else :
       y2 = int(Object_Position.imag)*108
    print("Co-ordinate's of rocket: ",x1,y1,"Co-ordinate's of Object ",x2,y2)
    
def main() :
   global Rocket_Position 
   global color
   global screen
   global Score
   font =pygame.font.SysFont("SansitaOne.tff",30)
   #font = pygame.font.Font('freesansbold.ttf', 20)
   Exiter = True
   while Exiter :
    Exiter = Rocket_Pos()
    if int(Object_Position.imag) >= 5 :
        Object_Int_Pos()
    else :  
         Object_Pos()
    print("Object Position :-",Object_Position)
    Obj_Collusion_Check()
    Coordinate()
    screen.blit(Backround_Img, (0, 0))
    if int(Object_Position.imag) < 4 :
        screen.blit(Fuel_Img, (x2, y2)) 
        screen.blit(Rocket_Img, (x1, y1))
        Score_Display = f"Score : {Score}"
        text = font.render(Score_Display, True,(random.randint(200,255),random.randint(200,255),random.randint(200,255)))
        width = text.get_width()
        screen.blit(text, (960 - width - 20,20))
        esc = font.render("esc",True,(random.randint(200,255),random.randint(200,255),random.randint(200,255)))
        screen.blit(esc,(20,20))
    pygame.display.update()
    time.sleep(0.20)

#Start
print("Press Enter to start Engine or esc to Exit :-\n")
print("Engine Started :-\n")
Rocket_Position = 0
Object_Position = complex(0,0)
Object_Int_Pos()
Score = 0
width = 960
height = 540
color=(126,132,247)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rocket_Jet')

current_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
Image_Rocket_Path    = current_directory + '\Jet.png'
Image_Earth_Path     = current_directory + '\earth.png'
Image_Backround_Path = current_directory + '\Backround.png'

Rocket_Img = pygame.image.load(Image_Rocket_Path).convert_alpha()
Fuel_Img = pygame.image.load(Image_Earth_Path).convert_alpha()
Backround_Img = pygame.image.load(Image_Backround_Path).convert_alpha()

x1 = 432
y1 = 430
x2 = 432
y2 = 0

screen.blit(Backround_Img, (0, 0))
screen.blit(Rocket_Img, (x1, y1))
screen.blit(Fuel_Img, (x2, y2))

pygame.display.flip()
main()
pygame.quit()

