# Time-stamp: <2014-01-31 19:28 christophe@pallier.org>

# import parallel
import pygame
from pygame.constants import *
import string
import os, sys, glob
import random
import time

# parallel port
#     a = p.getInError() # button 1
#     b = p.getInSelected() # button 2
#     c = p.getInPaperOut() # button 3
#     d = p.getInBusy() # button 4
    
def Init(ResFile, FullScreen=True):
    #global p
    #p = parallel.Parallel()

    pygame.mixer.pre_init(22050, -16, 1, 4096)
    pygame.init()

    global screen
    W, H = 640, 480
    if FullScreen:
            screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
    else:
            screen =  screen = pygame.display.set_mode((W, H))
    pygame.mouse.set_visible(False)

    global font
    font = pygame.font.Font(None, 24)

    global msgsurf # used to display on the first line of the screen
    msgsurf = pygame.Surface((640, 100))

    global resf
    resf = open(ResFile, 'a+')
    resf.write("#\n")
    resf.write("# Started at " + time.asctime() + "\n")
#    resf.write("# Directory = " + os.environ['PWD'] + "\n")



def Quit():
    resf.close()
    pygame.quit()
    
def Blit(surface,pos):
    screen.blit(surface,pos)

def UpdateScreen():
    pygame.display.update()
    pygame.display.flip()

def Message(string):
    msgsurf.fill((0,0,0))
    msgsurf.blit(font.render(string, True, (255,0,0)), (0,0))
    screen.blit(msgsurf,(0,0))
    UpdateScreen()

def ClearMessage():
    msgsurf.fill((0,0,0))
    screen.blit(msgsurf,(0,0))
    UpdateScreen()

def LoadSound(f):
    return pygame.mixer.Sound(f)
    
def PlaySound(s):
    c = s.play()
    while c.get_busy():
        pygame.time.delay(50)

def WaitForAnyKeyPress():
        pygame.event.clear()
        while not pygame.event.peek([KEYDOWN]): 
            pass
               
def CheckEscape():
    for ev in pygame.event.get():
        if ev.type == KEYDOWN and ev.key == K_ESCAPE: return 1
    return 0
    
def Save(string):
    resf.write(string+"\n")

def Clock():
    return pygame.time.get_ticks()

def Wait(millisec):
    pygame.time.wait(millisec)

def Shuffle(list):
    random.shuffle(list)
