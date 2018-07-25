from PIL import Image, ImageGrab, ImageOps
import pyautogui as pag
import time
from numpy import *

 

class Coordinates():
    '''This class finds the coordinates for the replay button of the dino 
    game'''
    
    #This finds the center of the score and top right of dinosaur on
    #the screen and if it is not found it raises an exception
    score = pag.locateCenterOnScreen('score.png')
    if score == None:
        refresh = pag.locateCenterOnScreen('refresh.png')
        pag.click(refresh)
        time.sleep(2)
        score = pag.locateCenterOnScreen('score.png')
    dino = pag.locateOnScreen("dino_screenshot.png")
    if dino == None:
            raise Exception("Make sure the dino is on screen")
    dino = (dino[0] + dino[2] + 14  , dino[1] - 15)
    
    
def start_game():
    '''This function presses the restart button if necessary. The first click
    makes sure that the proper window is open and the second click restarts
    the game'''
    pag.click(Coordinates.score)
    pag.press('space')
    pag.keyDown('down')


def press_space():
    '''This funtion presses the space button when needed'''
    pag.keyUp('down')
    pag.keyDown('space')
    time.sleep(0.07)
    pag.keyUp('space')
    pag.keyDown('down')
    

def screen_grab():
    '''This function grabs the image of the box used to see if the dino has an 
    object in the way. Then it turns that into an array of greyscale values
    and returns the sum of the array'''
    #box = (Coordinates.dino[0] + 130, Coordinates.dino[1], Coordinates.dino[0] +
     #      190, Coordinates.dino[1] + 30)
    box = (Coordinates.dino[0] + 40, Coordinates.dino[1], Coordinates.dino[0] +
           180, Coordinates.dino[1] + 30)
    image = ImageGrab.grab(box)
    image = ImageOps.grayscale(image)
    a = array(image.getcolors())
    print(a.sum())
    if(a.sum() > 4447):
        return True
    return False 
 
def main():
    '''This file contains the loop that keeps checking if the dino should jump'''  
    start_game()
    while True: 
        if(screen_grab()):
            press_space()

main()