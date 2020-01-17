from headers import *

class Board:

    #Creates the entire board for the game

    #constructor function
    def __init__(self, rows,cols):
        self.rows=rows
        self.cols=cols
        self.grid=[]

    #function to create the playing board
    def create_board(self):
        for i in range(self.rows):
            self.temp=[]
            for j in range(self.cols):
                self.temp.append(" ")
            self.grid.append(self.temp)
        # self.grid=np.array(self.grid)
        

    #function to print the playing board
    def print_board(self, factor):
            for i in range(self.rows):
                for j in range (factor, SCREEN+factor):
                    print(Fore.WHITE + Back.LIGHTBLACK_EX + Style.BRIGHT+self.grid[i][j], end='')
                print()

        

