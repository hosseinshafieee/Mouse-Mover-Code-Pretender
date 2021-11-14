import time
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Controller as MouseController
mouse = MouseController()
keyboard = KeyboardController()

def start(RANDOM_TIMER, num) :
   coding_pretending(RANDOM_TIMER, num)


def coding_pretending(RANDOM_TIMER, num, lastSavePosition): 
        
        keyboard.press('/')
        keyboard.release('/')
        keyboard.press('/')
        keyboard.release('/')
        keyboard.press('M')
        keyboard.release('M')
        keyboard.press('M')
        keyboard.release('M')
        keyboard.press('d')
        if (lastSavePosition != mouse.position) : return
        time.sleep(RANDOM_TIMER)
        keyboard.release('d')
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        keyboard.press('s')
        keyboard.release('s')
        keyboard.press('h')
        keyboard.release('h')
        if (lastSavePosition != mouse.position) : return
        time.sleep(RANDOM_TIMER)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.press('/')
        keyboard.release('/')
        keyboard.press('/')
        keyboard.release('/')
        keyboard.press('a')
        keyboard.release('a')
        keyboard.press('M')
        keyboard.release('M')
        keyboard.press('d')
        keyboard.release('d')
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        keyboard.press('s')
        keyboard.release('s')
        keyboard.press('v')
        keyboard.release('v')
        if (lastSavePosition != mouse.position) : return
        time.sleep(RANDOM_TIMER)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('s')
            keyboard.release('s')
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
        print('FILE SAVED')

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.press('/')
        keyboard.release('/')
        keyboard.press('/')
        keyboard.release('/')
        keyboard.press('a')
        keyboard.release('a')
        keyboard.press('M')
        keyboard.release('M')
        keyboard.press('d')
        keyboard.release('d')
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        keyboard.press('s')
        keyboard.release('s')
        keyboard.press('v')
        keyboard.release('v')
        if (lastSavePosition != mouse.position) : return
        time.sleep(RANDOM_TIMER)
        keyboard.press('/')
        keyboard.release('/')
        keyboard.press('/')
        keyboard.release('/')
        keyboard.press('M')
        keyboard.release('M')
        keyboard.press('M')
        keyboard.release('M')
        keyboard.press('d')
        keyboard.release('d')
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        keyboard.press('s')
        keyboard.release('s')
        keyboard.press('h')
        keyboard.release('h')
        if (lastSavePosition != mouse.position) : return
        time.sleep(RANDOM_TIMER)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('s')
            keyboard.release('s')
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
        print('FILE SAVED')
        with keyboard.pressed(Key.ctrl):
            keyboard.press('z')
            keyboard.release('z')
        if (lastSavePosition != mouse.position) : return
        time.sleep(RANDOM_TIMER)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('s')
            keyboard.release('s')
        with keyboard.pressed(Key.ctrl):
            keyboard.press('z')
            keyboard.release('z')
        if (lastSavePosition != mouse.position) : return
        time.sleep(RANDOM_TIMER)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('z')
            keyboard.release('z')
        with keyboard.pressed(Key.ctrl):
            keyboard.press('s')
            keyboard.release('s')
        if (lastSavePosition != mouse.position) : return
        time.sleep(RANDOM_TIMER)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('z')
            keyboard.release('z')
        if (lastSavePosition != mouse.position) : return
        time.sleep(RANDOM_TIMER)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('s')
            keyboard.release('s')
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
        print('FILE SAVED')
        with keyboard.pressed(Key.ctrl):
            keyboard.press('z')
            keyboard.release('z')
        with keyboard.pressed(Key.ctrl):
            keyboard.press('z')
            keyboard.release('z')
        if (lastSavePosition != mouse.position) : return
        time.sleep(RANDOM_TIMER)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('s')
            keyboard.release('s')
        with keyboard.pressed(Key.ctrl):
            keyboard.press('z')
            keyboard.release('z')
        if (num % 2 == 0):
            print('==================================================== \n\n\n CTRL Z pressed you have 30s to stop proccess \n\n\n====================================================')
            time.sleep(30)
