from sys import platform
import os

if platform == "darwin":
    os.system('python calc_mac.py')

elif platform == "win32":
    os.system('python calc.py')
