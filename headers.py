import time
import numpy as np
import signal
import os
import sys
import time
from colorama import init, Fore, Back, Style
import random
from alarmexception import AlarmException
from getch import _getChUnix as getChar

#colours
ENDC = '\033[m' # reset to the defaults
TGREEN =  '\033[32m' # Green Text
HT=40
SCREEN=200
WIDTH=2000
GAMETIME=100
STARTPOS=25

def line():
    for i in range(SCREEN):
        print('-', end='')
    print()

def reposition_cursor(x,y):
    print("\033[%d;%dH" % (x, y))
