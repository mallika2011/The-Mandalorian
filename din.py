from headers import *
from person import *

class Din(Person):

    #Attributes inherited from Person class

    #personal attributes for din 
    def __init__(self, x_cood, y_cood):
        self.__body=np.array([[" ","O"," "],["{","|","}"],["/"," ","\\"]])   #3x3 matrix
        self.__body_fly=np.array([[" "," ","O"," "," "],["{","|"," ","|","}"],[" ","/"," ", "\\"," "]])
        self.__lives=4
        self.collision_ok=[" ","$"]
        self.__coins=0
        self.dead=0

        Person.__init__(self,x_cood,y_cood)

    def show_lives(self):
        return self.__lives
    
    def show_coins(self):
        return self.__coins
    
    #Function to place din correctly in the beginning
    def start_pos(self,grid):
        for i in range(HT-5,HT-2):
            for j in range(10, 13):
                grid[i][j]=self.__body[i-(HT-5)][j-10]

    #Clearing the position of din as he moves
    def din_clear(self, grid, x,y):
        grid[y:y+3,x:x+3]=' '

    #New position of din as he moves
    def din_show(self, grid, mode,x,y):
        if mode == 0:
            self.din_clear(grid, self.x_cood,self.y_cood)
            self.x_cood=x
            self.y_cood=y
            for i in range(y,y+3):
                for j in range(x, x+3):
                    grid[i][j]=self.__body[i-y][j-x]
        elif mode == 1:
            o=1