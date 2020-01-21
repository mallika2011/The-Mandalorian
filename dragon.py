# dragon = [list("                          __,----'~~~~~~~~~`-----.__  "),
#         list("               .  .     //====-              ____,-'~`"),
#         list("              \_|// .   /||\\\  `~~~~`---.___./        "), 
#         list("           _-~o  `\/    |||  \\\           _,'`        "),
#         list("         ;_,_,/ _-'|-   |`\   \\\        ,'            "),
#         list("           '',/~7  /-   /  ||   `\.     /             "),  
#         list("            '  /  /-   /   ||      \   /              "),
#         list("             /  /|- _/   ,||       \ /                "), 
#         list("            /  `| \\'--===-'       _/`                 "),   
#         list("          /|    )-'\~'      _,--''                    "),
#         list("         / |    |   `\_   ,^             /\           "),
#         list("        /  \     \__   \/~               `\__         "),
#         list("    _,-' _/'\ ,-'~____-'`-/                 ``===\    "),
#         list("   ((->/'    \|||' `.     `\.  ,                _||   "),
#         list("              \_     `\      `~---|__i__i__\--~'_/    "),
#         list("             __-^-_    `)  \-.______________,-~'      "),
#         list("            ///,-'~`__--^-  |-------~~~~^'            "),
#         list("                   ///,--~`-\                         ")]



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
        self.__iceball=Fore.LIGHTWHITE_EX+"@"+Fore.RESET
        self.__shootstart=0
        self.__icex=0
        self.__icey=0

    def set_lives(self,x):
        self.__lives=x
    def get_lives(self):
        return self.__lives

    def set_icex(self,x):
        self.__icex=x
    def get_icex(self):
        return self.__icex

    def set_icey(self,y):
        self.__icey=y
    def get_icey(self):
        return self.__icey

    def get_shootstart(self):
        return self.__shootstart
    def set_shootstart(self,x):
        self.__shootstart=x

    def dragon_show(self,grid):
        x=WIDTH-len(dragon[0])-1
        y=HT-2-len(dragon)-1
        for i in range(y,y+len(dragon)):
            for j in range(x,x+len(dragon[0])):
                grid[i][j]=dragon[i-y][j-x]


    def show_iceball(self,grid):
        grid[self.__icey][self.__icex]=self.__iceball
    
    def clear_iceball(self,grid):
        grid[self.__icey][self.__icex]=" "

    def dragon_shoot(self, grid):
        self.clear_iceball(grid)
        self.set_icex(self.get_icex()-1)
        self.show_iceball(grid)




