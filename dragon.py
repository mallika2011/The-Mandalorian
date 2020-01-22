
dragon=[list("        _(9(9)__        __/^\/^\__            "),
        list("       /o o   \/_     __\_\_/\_/_/_           "),
        list("       \       \/_   _\.'       './_      _/\_"),
        list("        `---`\  \/_ _\/           \/_   _|.'_/"),
        list("              \  \/_\/      /      \/_  |/ /  "),
        list("               \  `-'      |        ';_:' /   "),
        list("               /|          \      \     .'    "),
        list("              /_/   |,___.-`',    /`'---`     "),
        list("               /___/`       /____/            ")]



from headers import *
from person import *

class Dragon(Person):

    def __init__(self,x,y):
        Person.__init__(self,x,y)
        self.__lives=5
        self.__shootstart=0
        self.__cankill=0

    def set_lives(self,x):
        self.__lives=x
    def get_lives(self):
        return self.__lives
    def set_cankill(self,x):
        self.__cankill=x
    def get_cankill(self):
        return self.__cankill
    def dec_lives(self):
        self.__lives-=1

    def get_shootstart(self):
        return self.__shootstart
    def set_shootstart(self,x):
        self.__shootstart=x

    def dragon_clear(self, grid):
        x=self.getx()
        y=self.gety()
        for i in range(y,y+len(dragon)):
            for j in range(x,x+len(dragon[0])):
                grid[i][j]=" "

    def dragon_show(self,grid):
        x=self.getx()
        y=self.gety()
        for i in range(y,y+len(dragon)):
            for j in range(x,x+len(dragon[0])):
                grid[i][j]=dragon[i-y][j-x]
    
    def move_dragon(self, grid, y):
        # print("entered with mando and drago ", y, self.gety())  
        self.dragon_clear(grid)
        new_y=y-5

        if(new_y<3):
            new_y=3
        elif(new_y>28):
            new_y=28
        
        self.sety(new_y)
        self.dragon_show(grid)
        




