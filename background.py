from headers import *

class Background:

    #constructor function
    def __init__(self):
        self.__ceil=Fore.BLACK + Back.LIGHTYELLOW_EX + Style.BRIGHT +"_" +Style.RESET_ALL       #Private variables to ensure security
        self.__floor=Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"/"+ Style.RESET_ALL
        self.__middle=Fore.BLACK + Back.LIGHTYELLOW_EX + Style.BRIGHT +"="+Style.RESET_ALL

    #function to create the floor
    def display_floor(self,boundary):
        for i in range(WIDTH-1):
            boundary[HT-1][i]= self.__floor
            boundary[HT-2][i]=self.__middle

    #function to create the ceil
    def display_ceil(self,boundary):
        for i in range(WIDTH-1):
            boundary[0][i]=self.__ceil
            boundary[1][i]=self.__middle

