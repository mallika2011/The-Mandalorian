from headers import *

#importing classes
from board import Board
from din import Din
from background import Background
from obstacles import *


#The board
obj_board=Board(HT,WIDTH)
obj_board.create_board()
factor=0

#The player
obj_din=Din(STARTPOS,35)

#The background
obj_back=Background()
obj_back.display_ceil(obj_board.grid)
obj_back.display_floor(obj_board.grid)

#Placing obstacles

obj_beam_array=[Beam(0,0) for i in range(30)]

valy = 10
valx=random.randrange(25)
for i in range (0,30,3):
    obj_beam_array[i]=Beam(valx,valy)
    valy+=100
    valx=random.randrange(25)

valy= 25
for i in range (1,30,3):
    obj_beam_array[i]=Beam(valx, valy)
    valy+=50
    valx=random.randrange(25)

valy=15
for i in range(2,30,3):
    obj_beam_array[i]=Beam(valx,valy)
    valy+=300
    valx=random.randrange(25)

val=10
ang=0

for i in range(len(obj_beam_array)):
    print(str(obj_beam_array[i].x)+ "  "+ str(obj_beam_array[i].y)+ " type "+str(val)+ " angle "+str(ang))

    obj_beam_array[i].place_beam(val,ang,obj_board.grid)
    if(val==30):
        val=10
    else:
        val+=10
    if ang==90:
        ang=0
    else:
        ang+=90
    #TODO PLACE 45 DEGREE BEAMS

#Placing coins

    

#Start time of the game 
start_time = time.time()

os.system('clear')

while True:
    newtime= GAMETIME - (round(time.time()) - round(start_time))
    reposition_cursor(0,0)
    if(newtime==0):
        os.system('clear')
        print("GAME OVER!")
        quit()
    else:
        obj_din.din_show(obj_board.grid,0,factor+1+STARTPOS,35)

        print()
        print()
        time.sleep(0.2)

        if factor == 1800:
            factor=1800
        else:
            factor+=1
        print(Fore.WHITE + Back.RED + Style.BRIGHT + "THE MANDALORIAN".center(SCREEN))
        print(Style.RESET_ALL)
        stats= str("LIVES: "+str(obj_din.show_lives()) + "      SCORE:"+str(obj_din.show_coins())+"     TIME: "+ str(newtime))
        print(Fore.WHITE + Back.BLUE + Style.BRIGHT + stats.center(SCREEN), end='')
        print(Style.RESET_ALL)
        obj_board.print_board(factor)
        print()
        print()

