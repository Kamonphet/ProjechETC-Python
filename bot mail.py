import pyautogui as pg
import time

def botclick ():
    pg.click(x=383, y=199)
    pg.click(x=421, y=351)
    pg.click(x=542, y=199)

for i in range (100):
    botclick()
    time.sleep(1)

    
