import pyautogui
import webbrowser
import time

url1 = 'youtube.com/watch?v=iTLUb5UmeJo'

chrome_path ='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url1)
time.sleep(20)
pyautogui.screenshot("/Users/oguzh/Desktop/ekrangoruntusu.jpg")
