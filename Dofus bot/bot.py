import time
import win32api, win32con
import json
import os
import cv2 as cv
from plugins.searchMap import *
import pyautogui
import numpy as np

firstStart = True
hasToWalkToRoute = False
hasToDoRoute = True

def click(x,y):
    win32api.SetCursorPos((x, y))
    print("Clicking on object")
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.175)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.2)
    
    
def moveToMap():
    with open('modules\F2P_Astrub_Nettles\F2P_Astrub_Nettles.json') as module:
        data = json.load(module)
        for route in data['walk_to_route']:
            time.sleep(10)
            if route['direction'] == 'up':
                win32api.SetCursorPos((int(setMapCoords.up_x), int(setMapCoords.up_y)))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                time.sleep(0.075)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            elif route['direction'] == 'right':
                win32api.SetCursorPos((int(setMapCoords.right_x), int(setMapCoords.right_y)))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                time.sleep(0.075)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            elif route['direction'] == 'down':
                win32api.SetCursorPos((int(setMapCoords.down_x), int(setMapCoords.down_y)))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                time.sleep(0.075)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            elif route['direction'] == 'left':
                win32api.SetCursorPos((int(setMapCoords.left_x), int(setMapCoords.left_y)))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                time.sleep(0.075)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def setMapCoords():
    with open('config.json') as configjson:
        data = json.load(configjson)
    # set the up coords
    setMapCoords.up_x = data['map_switch_coords'][0]["UP_MAP"][0]["x"]
    setMapCoords.up_y = data['map_switch_coords'][0]["UP_MAP"][0]["y"]
    # set the right coords
    setMapCoords.right_x = data['map_switch_coords'][0]["RIGHT_MAP"][0]["x"]
    setMapCoords.right_y = data['map_switch_coords'][0]["RIGHT_MAP"][0]["y"]
    # set the down coords
    setMapCoords.down_x = data['map_switch_coords'][0]["DOWN_MAP"][0]["x"]
    setMapCoords.down_y = data['map_switch_coords'][0]["DOWN_MAP"][0]["y"]
    # set the left coords
    setMapCoords.left_x = data['map_switch_coords'][0]["LEFT_MAP"][0]["x"]
    setMapCoords.left_y = data['map_switch_coords'][0]["LEFT_MAP"][0]["y"]
    configjson.close()
    
def clickObject(needle, haystack):
    takeScreenshot("images\\screen_dump\\screen_dump.png")
    img_rgb = cv.imread(haystack)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread(needle,0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    middleWidth = w // 2
    middleHeight = h // 2
    targetx = None
    targety = None
    for pt in zip(*loc[::-1]):
        # click(pt[0] + middleWidth , pt[1] + middleHeight)
        targetx = pt[0] + middleWidth
        targety= pt[1] + middleHeight
        cv.rectangle(img_rgb, pt, (pt[0] + w , pt[1] + h), (0,0,255), 2)
    cv.imwrite('res.png',img_rgb)
    if targety and targetx:
        click(targetx, targety)
        time.sleep(7)

def takeScreenshot(path):
    pyautogui.keyDown('y')
    time.sleep(0.25)
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(path)
    pyautogui.keyUp('y')

def doRoute():
     with open('modules\F2P_Astrub_Nettles\F2P_Astrub_Nettles.json') as module:
        data = json.load(module)
        for route in data['do_route']:
            clickObject("images\\nettles.png", "images\\screen_dump\\screen_dump.png")
            if route['direction'] == 'up':
                win32api.SetCursorPos((int(setMapCoords.up_x), int(setMapCoords.up_y)))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                time.sleep(0.075)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            elif route['direction'] == 'right':
                win32api.SetCursorPos((int(setMapCoords.right_x), int(setMapCoords.right_y)))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                time.sleep(0.075)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            elif route['direction'] == 'down':
                win32api.SetCursorPos((int(setMapCoords.down_x), int(setMapCoords.down_y)))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                time.sleep(0.075)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            elif route['direction'] == 'left':
                win32api.SetCursorPos((int(setMapCoords.left_x), int(setMapCoords.left_y)))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                time.sleep(0.075)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(10)
def checkConfigSet():
    directions = ["UP_MAP", "RIGHT_MAP", "DOWN_MAP", "LEFT_MAP"]
    with open('config.json') as configjson:
        data = json.load(configjson)
        if data['configSet'] == "False":
            configSet = False
        else:
            return
        for direction in directions:
            if len(data['map_switch_coords'][0][direction][0]["x"]) != 0 or len(data['map_switch_coords'][0][direction][0]["y"]) != 0:
                configSet = True
            else:
                configSet = False
                break
        configjson.close()

    data['configSet'] = str(configSet)
    jsonfile = open("config.json", 'w')
    jsonfile.write(json.dumps(data, indent=4))
    

def main():
    time.sleep(3)
    setMapCoords()
    doRoute()
 
    

if __name__ == "__main__":
    main()


 

