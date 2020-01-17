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
YELLOW=Fore.YELLOW
RESET=Fore.RESET
HT=40
SCREEN=200
WIDTH=500
GAMETIME=100
STARTPOS=25
GRAVITYVAL=5
drop_start_time=-1
def line():
    for i in range(SCREEN):
        print('-', end='')
    print()

def reposition_cursor(x,y):
    print("\033[%d;%dH" % (x, y))

def view_colours():
    print(Fore.WHITE + Back.LIGHTWHITE_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.MAGENTA + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTCYAN_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTBLACK_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTGREEN_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.RED + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTRED_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTYELLOW_EX+ Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.YELLOW + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    

def game_over():

    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     ")                 
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT+ "  _____                         ____                 ")                 
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT+ " / ____|                       / __ \                ")              
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT+ "| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ ")
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT +"| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|")
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT +"| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ")
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT +" \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   ")
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     "+Style.RESET_ALL)                 
                                                      
                                                      


