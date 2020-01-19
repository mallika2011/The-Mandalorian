import time
import numpy as np
import signal
import os
import sys
from colorama import init, Fore, Back, Style
# init()
import random
from alarmexception import AlarmException
from getch import _getChUnix as getChar


HT=40
SCREEN=200
WIDTH=275
GAMETIME=100
STARTPOS=25
GRAVITYVAL=1
BEAM_SIZE=20
INPUT_CHAR=''

def line():
    for i in range(SCREEN):
        print('-', end='')
    print()

def reposition_cursor(x,y):
    print("\033[%d;%dH" % (x, y))

#OBJECTS:
BEAM1=Fore.LIGHTGREEN_EX+"#"+Fore.RESET
BEAM2=Fore.LIGHTGREEN_EX+"<"+Fore.RESET
BEAM3=Fore.LIGHTGREEN_EX+">"+Fore.RESET

COIN = Fore.YELLOW + "$"+Fore.RESET
PLUS=Fore.WHITE+Back.CYAN+"+"+Style.RESET_ALL



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

    a=[0]*3
    for i in range(3):
        a[i]=Fore.RED+"#"+Fore.RESET

    b=[0]*4

    for i in range(3):
        b[i]=a[i]

    for i in range(4):
        print(b[i])

    view_colours()

    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     ")                 
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT+ "  _____                         ____                 ")                 
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT+ " / ____|                       / __ \                ")              
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT+ "| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ ")
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT +"| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|")
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT +"| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ")
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT +" \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   ")
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT+ "                                                     "+Style.RESET_ALL)                 
                                                      
                                                      


