# AutoBot v1.0
Fixed some bugs, actions are now written in a python file, so record your actions, and run the python file written after program is done running. Remember, the program is stopped by a keyboard interrupt, so if you're running it from the terminal, just CTRL-C out of the program, and the python file will be written and saved as autobot-output.py in the same directory. The timing between actions is a bit off, I may update and send out another release in the near future.
View it here: https://github.com/calixo888/AutoBot/releases

# AutoBot
AutoBot is a type of automation bot. These types of bots can be used to copy your actions, keypresses, mouse clicks, and movements on your computer and is stored in a program, ready to be used. If you have a lot of files to delete, or just a mindless task that is really tedious, you can run this program, do it once, and run the generated program on a loop. 
NOTE: 
- The program is started by running it in a terminal, but it is stopped with a KeyboardInterrupt, or CTRL-C
- Two of the modules used here are Pynput and Pyautogui, and both modules are tricky to download, so if there any problems with it, it may be those two packages, and you may have to download them yourself using pip or easy_install. install.py installs everything for you, but I myself have had bad experiences with downloading those two modules.
- For macOS users: if you are using Mojave, I believe there is a security limitation for pyautogui. So if you use Mojave, please follow the following steps:
  1. Go to preferences
  2. Go to Security & Privacy
  3. Go to the Privacy tab
  4. Click on Accessibility
  5. You may have to click on the lock and enter in the administrator's password to continue
  6. Scroll down to the Terminal
  7. Make sure that checkbox is checked
  8. That's it!
