from headers import *
from person import *

class Din(Person):

    #Attributes inherited from Person class

    #personal attributes for din 
    def __init__(self, x_cood, y_cood):
        # self.x_cood=x_cood
        # self.y_cood=y_cood
        self.__body=np.array([[" ","O"," "],["{","|","}"],["/"," ","\\"]])   #3x3 matrix
        self.__body_fly=np.array([[" "," ","O"," "," "],["{","|"," ","|","}"],[" ","/"," ", "\\"," "]])
        self.__body_shield=np.array([["-","-","-","-","-","-","-"],["|"," "," ","O"," "," ","|"],["|"," ","{","|","}"," ","|"],["|"," ","/"," ","\\"," ","|"],["-","-","-","-","-","-","-"]])
        self.__lives=4
        self.collision_ok=[" ","$"]
        self.__coins=0
        self.dead=0
        self.direction=0
        self.shield_flag=0
        self.fly_flag=0
        self.mode=0
        self.shield_start_time=0

        Person.__init__(self,x_cood,y_cood)

    def show_lives(self):
        return self.__lives

    def dec_lives(self):
        self.__lives-=1
    
    def show_coins(self):
        return self.__coins

    def inc_coins(self):
        self.__coins+=1
    
    #Function to place din correctly in the beginning
    def start_pos(self,grid):
        for i in range(HT-5,HT-2):
            for j in range(10, 13):
                grid[i][j]=self.__body[i-(HT-5)][j-10]

    def new_din(self,grid):
        for i in range(5,8):
            for j in range(10, 13):
                grid[i][j]=self.__body[i][j-10]

    #Clearing the position of din as he moves
    def din_clear(self, grid):
        x=self.x_cood
        y=self.y_cood

        flag=self.check_collision(grid)
        if flag ==1 :
            if(self.mode==0):
                grid[y:y+3,x:x+3]=' '
            elif self.mode == 1 :
                grid[y-2:y+5,x-2:x+7]=' '
        else :
            self.dec_lives()
            self.start_pos(grid)
            self.dead=0


    #New position of din as he moves
    def din_show(self, grid,x,y, mode):
        if mode == 0:
            self.din_clear(grid)
            self.x_cood=x
            self.y_cood=y
            for i in range(y,y+3):
                for j in range(x, x+3):
                    grid[i][j]=self.__body[i-y][j-x]

        elif mode == 1:  #for shielded mode
            self.din_clear(grid)
            self.x_cood=x
            self.y_cood=y
            for i in range(y,y+5):
                for j in range(x, x+7):
                    grid[i][j]=self.__body_shield[i-y][j-x]
            

    def gravity(self,grid):
        self.din_clear(grid)

        if(self.mode ==0 ):
            if(self.y_cood+3<=35):
                self.y_cood+=2
            else:
                self.y_cood=35
        elif(self.mode==1):
            if(self.y_cood+5<=33):
                self.y_cood+=2
            else:
                self.y_cood=33

    def remove_shield(self, grid):
        x=self.x_cood
        y=self.y_cood
        grid[y,x+4:x+7]=' '
        grid[y:y+5,x]=' '
        grid[y-2:y+2,x-2:x+8]=' '
        self.shield_flag=0        


    def check_collision(self,grid):
        x=self.x_cood
        y=self.y_cood
        # print(x, y)
        for i in range (y,y+3):
            for j in range (x, x+3):
                # print(grid[i][j])
                if(grid[i][j]=='#' or grid[i][j]=='<'):
                    if(grid[i][j]=='#'):
                        grid[i][j]=='#'
                    if(grid[i][j]=='<'):
                        grid[i][j]=='>'
                    return 2 #not possible
                    #TODO dead sound
                elif(grid[i][j]=='$'):
                    self.inc_coins()
                    
        return 1
                    
                    