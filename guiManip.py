import pyautogui
from time import sleep


print("start")
tt = open("new.txt","r")



usernames = []
for i in tt:
    i=i.split(",")
    for y in i:
        usernames.append(y)

sleep(3)
count = 1
for i in range(6):
    if count<=3:
        pyautogui.typewrite(usernames[i])
        print(usernames[i])
        sleep(2)
        pyautogui.moveTo(791, 178,.1)
        pyautogui.click()
    elif count>3 and count<=6:
        pyautogui.typewrite(usernames[i])
        print(usernames[i])
        sleep(2)
        pyautogui.moveTo(807, 216,.1)
        pyautogui.click()
    else:
        pyautogui.typewrite(usernames[i])
        print(usernames[i])
        sleep(2)
        pyautogui.moveTo(779, 243,.1)
        pyautogui.click()
        
    count+=1



print(pyautogui.position())