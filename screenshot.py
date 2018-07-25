import PIL
import pyautogui as pag
import time

#screencap = pyautogui.screenshot("refresh.png")
refresh = pag.locateCenterOnScreen('refresh.png')
pag.click(refresh)