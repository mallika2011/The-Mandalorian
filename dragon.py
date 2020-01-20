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

    def dragon_show(self,grid):
        x=WIDTH-len(dragon[0])-1
        y=HT-2-len(dragon)-1
        for i in range(y,y+len(dragon)):
            for j in range(x,x+len(dragon[0])):
                grid[i][j]=dragon[i-y][j-x]

