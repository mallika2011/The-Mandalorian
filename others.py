from headers import *


class Others:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape=np.zeros((100), dtype='<U1000')  #Polymorphism


#CLASS FOR THE BEAMS
class Beam(Others):

    def __init__(self, x, y):
        self.shape30 = np.zeros((30), dtype='<U100')
        self.shape20 = np.zeros((20), dtype='<U100')
        self.shape10 = np.zeros((10), dtype='<U100')

        Others.__init__(self, x, y)

    def create_beam(self, type):
        if(type == 10):
            self.shape10.fill('#')
            self.shape10[0] = '<'
            self.shape10[self.shape10.size-1] = '>'
        elif(type == 20):
            self.shape20.fill('#')
            self.shape20[0] = '<'
            self.shape20[self.shape20.size-1] = '>'
        elif(type == 30):
            self.shape30.fill('#')
            self.shape30[0] = '<'
            self.shape30[self.shape30.size-1] = '>'

       
    def check_beam(self, x,y, task, grid, type):

        #While placing beams
        if(task==1):
            for i in range (y,y+type):
                print(grid[x][i])
                if(grid[x][i]!=' '):
                    return 1
            for i in range (x, x+type):
                print(grid[i][y])
                if(grid[i][y]!= ' '):
                    return 1
            
            for i in range (x, x+type):
                for j in range (y, y+type):
                    if(i-x==j-y):
                        print(grid[i][j])
                        if(grid[i][j]!=' '):
                            return 1

            return 0

        #while shooting bullets
        elif(task==2):
            o=1
    
    def place_beam(self, type, angle, grid):

        x = self.x
        y = self.y

       

        print("placing" + str(x) + " " + str(y) +
              " angle " + str(angle) + " type "+str(type))
        self.create_beam(type)

        #AVOID CROSSING BEAMS
        if x + type > HT-3 or x < 4 or y+type > WIDTH:
            o = 1
        elif (self.check_beam(x,y,1,grid, type)):
            return

        # Placing the 10 length beam horizontally, vertically and at 45 degrees.
        if(type == 10):
            temp = 0
            if x + 10 > HT-3 or x < 4 or y+10 > WIDTH:
                o = 1
            else:
                if(angle == 90):
                    for i in range(x, x+10):
                        grid[i][y] = self.shape10[temp]
                        temp += 1
                elif(angle == 0):
                    for i in range(y, y+10):
                        grid[x][i] = self.shape10[temp]
                        temp += 1
                elif(angle == 45):
                    temp1 = 0
                    temp2 = 0
                    for i in range(x, x+10):
                        for j in range(y, y+10):
                            if(i-x== j-y):
                                grid[i][j] = self.shape10[temp]
                                temp += 1

        # Placing the 20 length beam horizontally, vertically and at 45 degrees.
        if(type == 20):
            temp = 0
            if x + 20 > HT-3 or x < 4 or y + 20 > WIDTH:
                o = 1
            else:
                if(angle == 90):
                    for i in range(x, x+20):
                        grid[i][y] = self.shape20[temp]
                        temp += 1
                elif(angle == 0):
                    for i in range(y, y+20):
                        grid[x][i] = self.shape20[temp]
                        temp += 1
                elif(angle == 45):
                    temp1 = 0
                    temp2 = 0
                    for i in range(x, x+20):
                        for j in range(y, y+20):
                            if(i-x==j-y):
                                grid[i][j] = self.shape20[temp]
                                temp += 1

        # Placing the 30 length beam horizontally, vertically and at 45 degrees.
        if(type == 30):
            temp = 0
            if x+30 > HT-3 or x < 4 or y+30 > WIDTH:
                o = 1
            else:
                if(angle == 90):
                    for i in range(x, x+30):
                        grid[i][y] = self.shape30[temp]
                        temp += 1
                elif(angle == 0):
                    for i in range(y, y+30):
                        grid[x][i] = self.shape30[temp]
                        temp += 1
                elif(angle == 45):
                    for i in range(x, x+30):
                        for j in range(y, y+30):
                            if(i-x== j-y):
                                grid[i][j] = self.shape30[temp]
                                temp += 1


#CLASS FOR THE COINS 
class Coins (Others):
    def __init__(self,x,y):
        self.shape=np.zeros((2),dtype='<U20')
        Others.__init__(self,x,y)
    
    def place_coin(self, grid):
        self.shape.fill('$')
        grid[self.x][self.y]='$'
        grid[self.x][self.y+1]='$'

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
        