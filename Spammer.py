'''
Our Task Is To Create A Python Program That Spam Message On A Text Messanger
'''
import pyautogui,time
time.sleep(5)
f = open("data.txt",'r')
for word in f:
    pyautogui.tywriter(word)
    pyautogui.press("enter")
