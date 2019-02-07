import subprocess

try:
    subprocess.call("curl https://bootstrap.pypa.io/get-pip.py | python",shell=True)
except:
    pass
subprocess.call("pip install pyautogui",shell=True)
subprocess.call("pip install pynput",shell=True)
subprocess.call("pip install future",shell=True)