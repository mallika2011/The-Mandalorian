from headers import *
from colorama import init
class Others:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape=np.zeros((100), dtype='<U1000')  #Polymorphism


#CLASS FOR THE BEAMS
class Beam(Others):

    def __init__(self, x, y):
        # self.shape = np.zeros((20), dtype='<U100')
        self.shape=[]*20

        Others.__init__(self, x, y)

    def create_beam(self):
        for i in range(len(self.shape)):
            init()
            self.shape[i]=BEAM1
        self.shape[0]=BEAM2
        self.shape[BEAM_SIZE-1]=BEAM3

       
    def check_beam(self, x,y, task, grid):

        #While placing beams
        if(task==1):
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
    
    def place_beam(self,angle, grid,f):

        x = self.x
        y = self.y
     
        self.create_beam()
        #AVOID CROSSING BEAMS
        if (x + BEAM_SIZE > HT-3 or x < 4 or y> WIDTH-30 or y+BEAM_SIZE > WIDTH-10):
            o = 1
        elif (self.check_beam(x,y,1,grid) and f==0):
            return
        else:
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

#CLASS FOR THE COINS 
class Coins (Others):
    def __init__(self,x,y):
        self.shape=np.zeros((1),dtype='<U100')
        Others.__init__(self,x,y)
    
    def place_coin(self, grid):
        self.shape.fill('$')
        grid[self.x][self.y]='$'

class Bullet(Others):
    def __init__(self,x,y):
        self.shape=np.zeros((3),dtype='<U100')
        Others.__init__(self,x,y)

    def clear_bullet(self, grid):
        x=self.x
        grid[x]=' '
        grid[x+1]=' '
        grid[x+2]=' '
    def place_bullet(self, grid):
        self.shape[0]='('
        self.shape[1]='0'
        self.shape[2]=')'

        for i in range(3):
            grid[self.x][self.y+i]=self.shape[i]
        
    def shoot(self, grid):
        grid[self.x][self.y]=' '
        self.y+=1
        self.place_bullet(grid)

    # def check_collision(self, grid):
        