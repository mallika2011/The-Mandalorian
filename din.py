from headers import *
from person import *

class Din(Person):

    #Attributes inherited from Person class

    #personal attributes for din 
    def __init__(self, x_cood, y_cood):
        # self.x_cood=x_cood
        # self.y_cood=y_cood
        self.__body=np.array([[" ","O"," "],["{","|","}"],["/"," ","\\"]],)   #3x3 matrix
        self.__body_fly=np.array([[" "," ","O"," "," "],["{","|"," ","|","}"],[" ","/"," ", "\\"," "]])
        self.__body_shield=np.array([["-","-","-","-","-","-","-"],["|"," "," ","O"," "," ","|"],["|"," ","{","|","}"," ","|"],["|"," ","/"," ","\\"," ","|"],["-","-","-","-","-","-","-"]])
        self.__lives=10000
        self.__coins=0
        self.shield_flag=0
        self.__fly_flag=0
        self.__powerflag=0
        self.mode=0
        self.shield_start_time=0
        self.power_start_time=0
        self.__drop_air_time=0

        Person.__init__(self,x_cood,y_cood)

    def show_lives(self):
        return self.__lives

    def set_fly_flag(self,x):
        self.__fly_flag=x

    def set_power(self,x):
        self.__powerflag=x
    def show_power(self):
        return self.__powerflag

    def show_fly_flag(self):
        return self.__fly_flag
    
    def set_drop_air_time(self,x):
        self.__drop_air_time=x
    
    def show_drop_air_time(self):
        return self.__drop_air_time

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
    def din_clear(self, grid):  #CAERFUL
        x=self.x_cood
        y=self.y_cood
        flag=self.check_collision(grid)
        if(self.mode==0):
            for i in range(y, y+3):
                for j in range(x,x+3):
                    grid[i][j]=' '
        elif self.mode == 1 :
            for i in range(y-2, y+5):
                for j in range(x-2,x+7):
                    grid[i][j]=' '
        if flag==2:
            self.dec_lives()
            
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

    def gravity_check_coins(self,inc, grid):
        x=self.x_cood
        y=self.y_cood
        for i in range(y, y+inc+1):
            for j in range(x,x+1):
                if(grid[i][j]==COIN):
                    grid[i][j]==" "
                    self.inc_coins()


    def gravity(self,grid):
        self.din_clear(grid)
        inc = (round(0.5*GRAVITYVAL*(self.show_drop_air_time()**2)))
        if(self.mode ==0 ):
            if(self.y_cood+inc<35):
                self.gravity_check_coins(inc,grid)
                for  i in range (inc):
                    self.y_cood+=1
            else:
                self.y_cood=35
        elif(self.mode==1):
            if(self.y_cood+inc<33):
                for i in range(inc):
                    self.y_cood+=inc
            else:
                self.y_cood=33
        self.din_show(grid, self.x_cood, self.y_cood, self.mode)

    def remove_shield(self, grid):
        x=self.x_cood
        y=self.y_cood

        for i in range(x+4,x+7):
            grid[y][i]=' '
        for i in range(y,y+5):
            grid[i][x]=' '
        for i in range(y-2, y+2):
            for j in range(x-2,x+8):
                grid[i][j]=' '
        self.shield_flag=0        


    def check_collision(self,grid):
        x=self.x_cood
        y=self.y_cood

        if(self.shield_flag==1):
            for i in range (y-2,y+2):
                for j in range (x-2, x+8):
                    if(grid[i][j]==COIN):
                        self.inc_coins()
            return 1

        for i in range (y,y+3):
            for j in range (x, x+3):
                if(grid[i][j]==BEAM1 or grid[i][j]==BEAM2 or grid[i][j]==BEAM3):
                    return 2 #not possible
                    #TODO dead sound
                elif(grid[i][j]==COIN):
                    self.inc_coins()

                elif(grid[i][j]==PLUS):
                    self.power_start_time=time.time()
                    self.set_power(1)                    
        return 1
                    
                    