import time
import win32api, win32con
import json
import os
from screen_search import *
import cv2 as cv


firstStart = True
hasToWalkToRoute = False
hasToDoRoute = True

def click(x,y):
    win32api.SetCursorPos((x, y))
    time.sleep(5)
    print("Clicking on object")
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.075)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
def moveToMap(x, y):
    time.sleep(random.randint(10, 13))
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.075)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

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
    for pt in zip(*loc[::-1]):
        click(pt[0] + middleWidth , pt[1] + middleHeight)
        cv.rectangle(img_rgb, pt, (pt[0] + w , pt[1] + h), (0,0,255), 2)
    cv.imwrite('res.png',img_rgb)

def takeScreenshot(path):
    pyautogui.keyDown('y')
    time.sleep(0.25)
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(path)
    pyautogui.keyUp('y')

def searchMapSwitch():
    for x in range(320, 350):
        win32api.SetCursorPos((x, 200))
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save("images\\screen_dump\\screen_dump.png")
        img_rgb = cv.imread("images\\screen_dump\\screen_dump.png")
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        template = cv.imread("images\\cursor\\map_left.png",0)
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
        threshold = 0.7
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if max_val >= threshold:
            print('found left pos')
            print (max_val)
            print(max_loc)
            break
    x, y = pyautogui.position()

    win32api.SetCursorPos((x, y))    
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    # time.sleep(0.075)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        
def main():
    # clickObject("images\\nettles.png", "images\\screen_dump\\screen_dump.png")
    searchMapSwitch()

if __name__ == "__main__":
    main()
# how to calculate middle:
# pt[0] + middleWidth , pt[1] + middleHeight

# def selectModule():
#     counter = 1
#     print("Select your desired module:")
#     for modules in os.walk('modules'):
#         if '\\' in modules[0]:
#             folder, module = modules[0].split('\\')
#             print("Module", counter, ": ",module)
#             counter += 1
            
#     selectedModule = input()
#     for modules in os.walk('modules'):
#         if '\\' in modules[0]:
#             folder, pickedModule = modules[0].split('\\')
#             if selectedModule == pickedModule:
#                 print("Succes!")
#             elif selectedModule != pickedModule:
#                 print('foutttt')

# if(firstStart == True):
#     selectModule()


# if hasToWalkToRoute == True:
#     hasToWalkToRoute == False
#     with open('modules\F2P_Astrub_Nettles\F2P_Astrub_Walk_to_Area.json') as f:
#         data = json.load(f)
#         for i in data['Coordinates']:
#             moveToMap(int(i['x']), int(i['y']))
#     f.close()

# if hasToDoRoute == True :
#     with open('modules\F2P_Astrub_Nettles\F2P_Astrub_Nettles.json') as f:
#         data = json.load(f)
#         for i in data['Coordinates']:
#             click(int(i['x']), int(i['y']))
#         hasToDoRoute = False
#     f.close()  

