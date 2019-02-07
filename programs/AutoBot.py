from pynput.mouse import Listener
import pyautogui
import re
import threading
import threading as Thread
from threading import Thread
from time import sleep
import time
import os

t = 0
ti2 = 0
key1 = ''
ti1 = 0
time2 = 0
current_t1 = 0
current = []
mouse_list = []
key_list = []
after = 0
before = 0


def on_click(x, y, button, pressed):
    global mouse_list
    global after
    global before
    global current
    global t1
    global current_t1

    ti1 = str(time.time() - t1)[0:5]
    if current_t1 != 0:
        current_t1 = 0
    else:
        current_t1 = ti1
    button = str(button)
    position = pyautogui.position()
    pattern = re.compile(r'\(.*\)')
    position2 = pattern.findall(str(position))
    if position2 == current:
        current = []
    else:
        for i in position2:
            element = 'pyautogui.moveTo' + i[:-1] + ',duration=1)'
            mouse_list.append(element)
            element = 'pyautogui.click(button=' + "'" + button[7:] + "'" + ')'
            mouse_list.append(element)
            element = 'sleep(' + str(current_t1) + ')'
            mouse_list.append(element)
        current = position2
    t1 = time.time()


def writeFile(mouse_list):
    path = os.getcwd() + '/dist'
    try:
        os.mkdir(path)
        os.chdir(path)
    except:
        os.chdir(path)
    filename = input('Input filename: ')
    with open(path + '/' + filename, 'w') as file:
        file.write(
            'from pynput.keyboard import Key, Controller\nfrom pynput.mouse import Listener\nimport os\nimport pyautogui\nimport re\nimport threading\nimport threading as Thread\nfrom threading import Thread\nfrom time import sleep\nimport time\n\nkeyboard = Controller()\n\n')
        file.write('try:')
        for i in mouse_list:
            file.write('\t' + i)
        file.write('except:')
        file.write("\tprint('[-] Error with the automation code, please debug it.')")


def mouse():
    global mouse_list
    global key_list
    global t1
    try:
        with Listener(on_click=on_click) as listener:
            draw()
            print('[+] Listening for actions...')
            t1 = time.time()
            listener.join()
    except:

        try:
            writeFile(mouse_list)
        except:
            pass
        print('[+] Done')
        print('[+] Thank you for using AutoBot')


def on_press(key):
    global t
    global ti1
    global ti2
    global key1
    key1 = key
    try:
        logging(ti1, ti2, key1)
    except:
        pass
    before = time.time()
    ti2 = time_it()
    after = time.time()
    try:
        ti1 = round(after - before, 2)
        ti1 -= ti2
    except:
        print('[-] Error')


def logging(ti1, ti2, key1):
    global mouse_list
    mouse_list.append('keyboard.press(' + str(key1) + ')')
    mouse_list.append('sleep(' + str(ti2) + ')')
    mouse_list.append('keyboard.release(' + str(key1) + ')')
    mouse_list.append('sleep(' + str(ti1) + ')')


def time_it():
    from pynput import keyboard
    import time
    global ti1
    global key1

    key1 = ''

    def callb(key):
        key1 = key
        get_ti1()  # what to do on key-release#converting float to str, slicing the float
        return False  # stop detecting more key-releases

    def get_ti1():
        ti1 = round(time.time() - t1, 2)
        return ti1

    def callb1(key):  # what to do on key-press
        return False  # stop detecting more key-presses

    with keyboard.Listener(on_press=callb1) as listener1:  # setting code for listening key-press
        listener1.join()

    t1 = time.time()  # reading time in sec

    with keyboard.Listener(on_release=callb) as listener:  # setting code for listening key-release
        listener.join()

    ti1 = get_ti1()
    return ti1


def keyboard():
    global key_list
    global t
    from pynput.keyboard import Key, Listener
    from pynput.keyboard import Key, Controller

    try:
        with Listener(on_press=on_press) as listener:
            t = time.time()
            listener.join()
    except:
        print('[-] Keyboard Error:')

def draw():
    print('''
    *****************************
    *                           *    
    *         Welcome to        *
    *           AutoBot         *
    *                           *
    *****************************
    \n''')
    input("Please press ENTER to start listening...")


try:
    t1 = Thread(target=keyboard)
    t1.start()
    mouse()
except KeyboardInterrupt:
    print('[+] Listener stopped')