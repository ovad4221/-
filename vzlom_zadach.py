import pyautogui as pug
import time


def sleepy(n):
    print(1)
    time.sleep(n)


sleepy(3)
x0, y0 = pug.position()
sleepy(3)
x1, y1 = pug.position()
sleepy(3)

for i in range(0, 100):
    time.sleep(4)
    pug.click(x0, y0)
    pug.hotkey('ctrl', 'a')
    pug.hotkey('delete')
    pug.typewrite(str(i/10))
    time.sleep(1)
    pug.click(x1, y1)
