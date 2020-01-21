from headers import *

# importing classes
from board import Board
from din import Din
from background import Background
from objects import *
from dragon import *

# The board
obj_board = Board(HT, WIDTH)
obj_board.create_board()
factor = 0

# The player
obj_din = Din(STARTPOS, 35)
obj_din.din_show(obj_board.grid, factor+1+STARTPOS, 35,0)

# The Dragon
obj_dragon=Dragon(WIDTH-len(dragon[0]),HT-2-len(dragon)-1)
obj_dragon.dragon_show(obj_board.grid)


# The background
obj_back = Background()
obj_back.display_ceil(obj_board.grid)
obj_back.display_floor(obj_board.grid)

#The magnet
obj_magnet=Magnet(5,random.randrange(30,WIDTH-200))
obj_magnet.show(obj_board.grid,obj_magnet.shape, obj_magnet.getx(), obj_magnet.gety())

#PRINTING HEADERS
def print_header(newtime):
    print(Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT + "THE MANDALORIAN".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTBLUE_EX+ Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    stats = str("LIVES: "+str(obj_din.show_lives()) + "  |  SCORE:" + str(obj_din.show_coins()*10)+"  |  TIME: " + str(newtime) +"  |  ENEMY: "+str(obj_dragon.get_lives()))
    print(Fore.WHITE + Back.LIGHTRED_EX + Style.BRIGHT + stats.center(SCREEN))
    print(Fore.WHITE + Back.LIGHTRED_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)


# Placing obstacles

obj_beam_array = [Beam(0, 0) for i in range(30)]
valy=5
for i in range (0,30):
    if(valy > WIDTH - 100):
        break
    valx = random.randrange(35)
    obj_beam_array[i]=Beam(valx,valy)
    #Placing beams which are horizontally at least 50 units apart
    valy= (valy+50) 
    
def beams_on_board():
    ang = 0
    for i in range(len(obj_beam_array)):
        if(obj_beam_array[i].canplace==0 and obj_beam_array[i].onboard==0):
            obj_beam_array[i].place_beam(ang, obj_board.grid)
            obj_beam_array[i].angle=ang
        elif(obj_beam_array[i].canplace==1):
            obj_beam_array[i].print_beam(ang, obj_board.grid)

        if ang == 90:
            ang = 0
        else:
            ang += 45


# Placing coins
def coins_on_board():
    for i in range(50):
        valx = random.randrange(5, HT-10)
        valy = random.randrange(0, WIDTH-100)
        obj_coin = Coins(valx, valy)
        if(obj_board.grid[valx][valy] == ' 'and obj_board.grid[valx][valy-1] == ' ' and obj_board.grid[valx][valy+1] == ' '):
            obj_coin.show(obj_board.grid, obj_coin.shape,obj_coin.getx(), obj_coin.gety())

obj_powerup_array=[]
#Placing Powerups 
def create_power():
    count = 0
    while(count<5):
        valx = random.randrange(5, HT-10)
        valy = random.randrange(0, WIDTH-150)

        for i in range(valx-1, valx+2+1):
            for j in range(valy-1, valy+3+1):
                if(obj_board.grid[i][j]!=" "):
                    continue
        
        obj_power=Powerup(valx,valy)
        obj_powerup_array.append(obj_power)
        count+=1

def power_on_board():
    for i in range(5):
        obj_powerup_array[i].show(obj_board.grid,obj_powerup_array[i].shape,obj_powerup_array[i].getx(),obj_powerup_array[i].gety())



def no_beam(x,y,grid):
    for i in range(len(obj_beam_array)):
        xco=obj_beam_array[i].getx()
        yco=obj_beam_array[i].gety()
        if(xco<=x<=xco+20    and    yco<=y<yco+20):
            # "found one  "
            obj_beam_array[i].canplace=0
            obj_beam_array[i].clear_beam(grid)

    

def check_magnet(din, grid):
    din.din_clear(grid)
    if(obj_magnet.gety()-din.getx() < 20 and obj_magnet.gety()>din.getx()): #As close as 20 units
        # print("in")
        if(din.gety()>5):
            din.sety(din.gety()-1)
        else:
            din.sety(5)
        din.setx(din.getx()+2)
        din.set_magnet_flag(1)

    elif(din.getx()-obj_magnet.gety()<20 and din.getx() >= obj_magnet.gety()):
        # print("in2")
        if(din.gety()>5):
            din.sety(din.gety()-1)
        else:
            din.sety(5)
        din.setx(din.getx()-1)
        din.set_magnet_flag(1)

    else:
        din.set_magnet_flag(0)
    din.din_show(grid, din.getx(),din.gety(), din.show_mode())


#Bullets array 
obj_bullets_array=[]

obj_iceballs_array=[]
#Dragons iceballs
def create_shoot_iceballs(grid):
    new_iceball=Iceballs(obj_dragon.gety(), obj_dragon.getx())
    new_iceball.shoot(grid)
    obj_iceballs_array.append(new_iceball)

def move_iceballs():
    for i in range(len(obj_iceballs_array)):
        if(obj_iceballs_array[i].get_active()==0):
            continue
        else:
            if(obj_iceballs_array[i].check_collision(obj_board.grid,obj_din)==1):
                obj_iceballs_array[i].set_active(0)
            obj_iceballs_array[i].shoot(obj_board.grid)        


def movedin():
    # moves the player
    def alarmhandler(signum, frame):
        # ''' input method '''
        raise AlarmException

    def user_input(timeout=0.15):
        # ''' input method '''
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''
    INPUT_CHAR = user_input()
    char=INPUT_CHAR


    if char == 'd':
        obj_din.set_fly_flag(0)
        ispos = obj_din.check_collision(obj_board.grid)
        if ispos == 1:
            obj_din.din_clear(obj_board.grid)
            obj_din.setx(obj_din.getx()+1) 
            obj_din.din_show(obj_board.grid, obj_din.getx(), obj_din.gety(),obj_din.show_mode())

        elif ispos == 2:
            obj_din.new_din(obj_board.grid)
            obj_din.dec_lives()

    elif char == 'a':
        obj_din.set_fly_flag(0)
        ispos = obj_din.check_collision(obj_board.grid)

        if ispos == 1:
            obj_din.din_clear(obj_board.grid)
            obj_din.setx(obj_din.getx()-1)
            obj_din.din_show(obj_board.grid, obj_din.getx(), obj_din.gety(),obj_din.show_mode())

        elif ispos == 2:
            obj_din.new_din(obj_board.grid)
            obj_din.dec_lives()

    elif char == 'q':
    	os.system("killall afplay")
    	quit()

    elif char == 'w':
        obj_din.set_fly_flag(1)
        obj_din.set_drop_air_time(0)
        ispos = obj_din.check_collision(obj_board.grid)
        if ispos==1:
            obj_din.din_clear(obj_board.grid)
            if(obj_din.show_mode()==0):
                if obj_din.gety() > 3 :
                    obj_din.sety(obj_din.gety()-1) 
                else: 
                    obj_din.sety(3)
            if(obj_din.show_mode()==1):
                if obj_din.gety() > 5 :
                    obj_din.sety(obj_din.gety()-1)
                else: 
                    obj_din.sety(5)
            obj_din.din_show(obj_board.grid, obj_din.getx(), obj_din.gety(),obj_din.show_mode())
        elif ispos==2:
            obj_din.new_din(obj_board.grid)
            obj_din.dec_lives()
            


    elif char == ' ':
        if(obj_din.show_shield_flag()==0 and obj_din.show_fly_flag()==0):  #Activate shield only when on ground
            obj_din.din_clear(obj_board.grid)
            obj_din.add_shield(obj_board.grid)
            obj_din.set_shield_flag(1)
            obj_din.set_mode(1)
            obj_din.set_sstart_time(time.time())


    elif char == 'l':
        obj_din.set_fly_flag(0)
        new_bullet=Bullet(obj_din.gety()+1, obj_din.getx()+5)
        new_bullet.show(obj_board.grid,new_bullet.shape,new_bullet.getx(), new_bullet.gety())
        new_bullet.start=time.time()
        new_bullet.active=1
        obj_bullets_array.append(new_bullet)
    
    else:
        obj_din.set_fly_flag(0)
        obj_din.set_drop_air_time(obj_din.show_drop_air_time()+1)
        ispos = obj_din.check_collision(obj_board.grid)

        if(ispos==2):
            obj_din.dec_lives()



