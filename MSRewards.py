import pyautogui as p
import time
import random


def search(query):
    p.hotkey("ctrl", "e")
    time.sleep(.1)
    p.write(query)
    p.press("enter")
    time.sleep(.9)


def image_find_click(image, g, c):
    a = 0
    b = 0
    while a == 0 and b == 0:
        try:
            a, b = p.locateCenterOnScreen(image, confidence=0.65, grayscale=g)
        except TypeError:
            pass
    if c:
        p.doubleClick(a, b)
    else:
        p.click(a, b)
    return a, b


#time.sleep(10)
p.hotkey("ctrl", "t")
time.sleep(.1)
#image_find_click("Images\\rewards.jpg", True, False)
time.sleep(.1)
p.hotkey("alt", "f")
time.sleep(.5)
image_find_click("Images\\settings.jpg", True, False)
time.sleep(.5)
image_find_click("Images\\search.jpg", True, False)
p.write("search engine")
p.press("enter")
time.sleep(.5)
image_find_click("Images\\search_res.jpg", True, False)
time.sleep(.5)
image_find_click("Images\\google_selected.jpg", True, False)
time.sleep(.5)
image_find_click("Images\\bing_drop.jpg", True, False)
time.sleep(.1)
p.hotkey("ctrl", "t")

searchOps = "qwertyuiopasdfghjklzxcvbnm1234567890!\"£$%^&*()/-+.|¬`[];'#,/{}:@~<>?"
searchQ = ""

for z in range(38):
    searchQ += searchOps[random.randint(0, len(searchOps) - 1)]

for y in range(len(searchQ)):
    search(searchQ[:y])

time.sleep(.1)
p.hotkey("ctrl", "w")
time.sleep(.1)
image_find_click("Images\\bing_selected.jpg", True, False)
time.sleep(.1)
image_find_click("Images\\google_drop.jpg", True, False)
time.sleep(.1)
p.hotkey("ctrl", "w")
#to compile into .exe
#pip install pyinstaller
#pyinstaller -f MSRewards.py
#check if .exe is in the same folder as Images folder if not move it there
