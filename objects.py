from headers import *
from colorama import init
class Objects:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape=np.zeros((100), dtype='<U1000')  #Polymorphism


#CLASS FOR THE BEAMS
class Beam(Objects):

    def __init__(self, x, y):
        # self.shape = np.zeros((20), dtype='<U100')
        self.shape=[]*20
        self.canplace=0
        self.active=0
        self.angle=0
        self.onboard=0
        self.kill=0

        Objects.__init__(self, x, y)

    def create_beam(self):
        for i in range(len(self.shape)):
            self.shape[i]=BEAM1
        self.shape[0]=BEAM2
        self.shape[BEAM_SIZE-1]=BEAM3

       
    def check_beam(self, x,y, task, grid):
        #While placing beams
        if(task==1):
            #Nothing down
            for i in range (y,y+BEAM_SIZE):
                if(grid[x][i]!=' '):
                    return 1
            for i in range (x, x+BEAM_SIZE):
                if(grid[i][y]!= ' '):
                    return 1

            for i in range (x, x+BEAM_SIZE):
                for j in range (y, y+BEAM_SIZE):
                    if(i-x==j-y):
                        if(grid[i][j]!=' '):
                            return 1

            return 0

        #while shooting bullets
        elif(task==2):
            o=1
    
    def place_beam(self,angle, grid):
        x = self.x
        y = self.y
        self.create_beam()
        self.onboard=1 
        #AVOID CROSSING BEAMS
        if (x + BEAM_SIZE > HT-3 or x < 4 or y> WIDTH-30 or y+BEAM_SIZE > WIDTH-10):
            self.canplace=0
            return
        elif (self.check_beam(x,y,1,grid)):
            self.canplace=0
            return
        self.canplace=1  
             
        temp = 0
        if(angle == 90):
            for i in range(x, x+BEAM_SIZE):
                grid[i][y] = self.shape[temp]
                temp += 1
        elif(angle == 0):
            for i in range(y, y+BEAM_SIZE):
                grid[x][i] = self.shape[temp]
                temp += 1
        elif(angle == 45):
            for i in range(x, x+BEAM_SIZE):
                for j in range(y, y+BEAM_SIZE):
                    if(i-x==j-y):
                        grid[i][j] = self.shape[temp]
                        temp += 1
    
    def print_beam(self,angle,grid):
        x = self.x
        y = self.y
        self.create_beam()
        temp = 0
        if(angle == 90):
            for i in range(x, x+BEAM_SIZE):
                grid[i][y] = self.shape[temp]
                temp += 1
        elif(angle == 0):
            for i in range(y, y+BEAM_SIZE):
                grid[x][i] = self.shape[temp]
                temp += 1
        elif(angle == 45):
            for i in range(x, x+BEAM_SIZE):
                for j in range(y, y+BEAM_SIZE):
                    if(i-x==j-y):
                        grid[i][j] = self.shape[temp]
                        temp += 1

    def clear_beam(self,grid):
        a=self.angle
        if(a==0):
            for i in range(self.y, self.y+20):
                grid[self.x][i]=" "
        elif(a==90):
            for i in range(self.x, self.x+20):
                grid[i][self.y]=" "
        elif(a==45):
            for i in range(self.x, self.x+20):
                for j in range(self.y, self.y+20):
                    if(i-self.x==j-self.y):
                        grid[i][j]= " "
           

#CLASS FOR THE COINS 
class Coins (Objects):
    def __init__(self,x,y):
        self.shape=np.zeros((1),dtype='<U100')
        Objects.__init__(self,x,y)
    
    def place_coin(self, grid):
        self.shape.fill(COIN)
        grid[self.x][self.y]=COIN

class Bullet(Objects):
    def __init__(self,x,y):
        self.shape=np.zeros((3),dtype='<U100')
        self.start=0
        self.active=0
        self.__crash=0
        Objects.__init__(self,x,y)

    def set_crash(self,x):
        self.__crash=x
    
    def show_crash(self):
        return self.__crash

    def clear_bullet(self, grid):
        x=self.x
        y=self.y

        for i in range(y-2,y+3):
            grid[x][i]=' '

    def place_bullet(self, grid):
        self.shape[0]='('
        self.shape[1]='0'
        self.shape[2]=')'

        for i in range(3):
            grid[self.x][self.y+i]=self.shape[i]
        
    def shoot(self, grid):
        self.clear_bullet(grid)

        if(self.y+5 > WIDTH -10):
            self.active =0
        else:
            if(self.active==0):
                self.y+=1
            else:
                for i in range(self.y-10, self.y+10):
                    if(grid[self.x][i]==BEAM1 or grid[self.x][i]==BEAM2  or grid[self.x][i]==BEAM3):
                        self.y=i
                        self.set_crash(1)
                self.y+=5
            self.place_bullet(grid)
            self.active=1


    def check_collision(self, grid):
        for i in range(3):
            if(grid[self.x][self.y+i]==BEAM1 or grid[self.x][self.y+i]==BEAM2 or grid[self.x][self.y+i]==BEAM3 ):
                self.set_crash(1)
                return 1
        return 0

class Powerup(Objects):
    def __init__(self,x,y):
        Objects.__init__(self,x,y)

    def place_power(self,grid):
        for i in range (self.x, self.x+2):
            for j in range(self.y, self.y+3):
                grid[i][j]=PLUS


class Magnet(Objects):
    def __init__(self, x,y):
        Objects.__init__(self,x,y)

    def place_magnet(self, grid):
        for i in range(self.x,self.x+5):
            for j in range(self.y,self.y+12):
                if(i-self.x>1):
                    if(j-self.y<4 or j-self.y >=8):
                        grid[i][j]=MAGNET
                    else :
                        grid[i][j]=" "
                elif (i-self.x<=1 and (j-self.y==0 or j-self.y==11)):
                    grid[i][j]=" "
                elif(i-self.x==0 and (j-self.y==1 or j-self.y==10)):
                    grid[i][j]=" "
                else:
                    grid[i][j]=MAGNET





