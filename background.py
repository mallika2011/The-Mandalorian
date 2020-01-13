from headers import *

class Background:

    #Places the background of the game
    #Height of the playing board will be 50 rows 
    #Max width of the playing board will be 1000 coloumns

    #constructor function
    def __init__(self):
        self.__ceil="_"        #Private variables to ensure security
        self.__floor="/"
        self.__middle="="

    #function to create the floor
    def display_floor(self,boundary):
        for i in range(2000):
            boundary[HT-1][i]=self.__floor
            boundary[HT-2][i]=self.__middle

    #function to create the ceil
    def display_ceil(self,boundary):
        for i in range(WIDTH):
            boundary[0][i]=self.__ceil
            boundary[1][i]=self.__middle

