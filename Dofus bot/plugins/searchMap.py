import pyautogui
import cv2 as cv
import json
import os
import win32api, win32con

def searchUpMap():
    width, height = pyautogui.size()
    for x in range(height - height, height, 3):
        win32api.SetCursorPos((600, x))
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save("images\\screen_dump\\screen_dump.png")
        img_rgb = cv.imread("images\\screen_dump\\screen_dump.png")
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        template = cv.imread("images\\cursor\\up_map.png",0)
        res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
        threshold = 0.9
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if max_val >= threshold:
            x, y = pyautogui.position()
            writeConfigJson("UP_MAP", x, y) 
            return

def searchRightMap():
    width, height = pyautogui.size()
    for x in range(width, width-width, -3):
        win32api.SetCursorPos((x, 600))
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save("images\\screen_dump\\screen_dump.png")
        img_rgb = cv.imread("images\\screen_dump\\screen_dump.png")
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        template = cv.imread("images\\cursor\\right_map.png",0)
        res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
        threshold = 0.9
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if max_val >= threshold:
            x, y = pyautogui.position()
            writeConfigJson("RIGHT_MAP", x, y) 
            return

def searchDownMap():
    width, height = pyautogui.size()
    for x in range(height, height - height, -3):
        win32api.SetCursorPos((600, x))
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save("images\\screen_dump\\screen_dump.png")
        img_rgb = cv.imread("images\\screen_dump\\screen_dump.png")
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        template = cv.imread("images\\cursor\\down_map.png",0)
        res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
        threshold = 0.9
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if max_val >= threshold:
            x, y = pyautogui.position()
            writeConfigJson("DOWN_MAP", x, y) 
            return
def searchLeftMap():
    width, height = pyautogui.size()
    for x in range(height, height - height, -3):
        win32api.SetCursorPos((600, x))
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save("images\\screen_dump\\screen_dump.png")
        img_rgb = cv.imread("images\\screen_dump\\screen_dump.png")
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        template = cv.imread("images\\cursor\\left_map.png",0)
        res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
        threshold = 0.9
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if max_val >= threshold:
            x, y = pyautogui.position()
            writeConfigJson("LEFT_MAP", x, y) 
            return

def writeConfigJson(direction, x, y):
    with open("config.json", 'r') as jsonfile:
        data = json.load(jsonfile)
        jsonfile.close()
    
        # print(data[direction][0]['x'])
    data['map_switch_coords'][0][direction][0]["x"] = x
    data['map_switch_coords'][0][direction][0]["y"] = y

    jsonfile = open("config.json", 'w')
    jsonfile.write(json.dumps(data, indent=4))