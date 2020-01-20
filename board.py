from headers import *

class Board:

    #Creates the entire board for the game

    #constructor function
    def __init__(self, rows,cols):
        self.__rows=rows
        self.__cols=cols
        self.grid=[]
        self.__flag=0

    #function to create the playing board
    def create_board(self):
        for i in range(self.__rows):
            self.temp=[]
            for j in range(self.__cols):
                self.temp.append(" ")
            self.grid.append(self.temp)
        # self.grid=np.array(self.grid)
        

    #function to print the playing board
    def print_board(self, factor):
            for i in range(self.__rows):
                for j in range (factor, SCREEN+factor):
                    
                    # print(Back.LIGHTBLACK_EX +self.grid[i][j] + Back.RESET, end='')
                    print(self.grid[i][j],end='')
                    
                print()

        

