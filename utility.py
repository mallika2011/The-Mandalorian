from headers import *

# importing classes
from board import Board
from din import Din
from background import Background
from others import *

# The board
obj_board = Board(HT, WIDTH)
obj_board.create_board()
factor = 0

# The player
obj_din = Din(STARTPOS, 35)
obj_din.din_show(obj_board.grid, factor+1+STARTPOS, 35,0)

# The background
obj_back = Background()
obj_back.display_ceil(obj_board.grid)
obj_back.display_floor(obj_board.grid)

#PRINTING HEADERS
def print_header(newtime):
    print(Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT + "THE MANDALORIAN".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTBLUE_EX+ Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    stats = str("LIVES: "+str(obj_din.show_lives()) + "  |  SCORE:" + str(obj_din.show_coins())+"  |  TIME: " + str(newtime))
    print(Fore.WHITE + Back.LIGHTRED_EX + Style.BRIGHT + stats.center(SCREEN))
    print(Fore.WHITE + Back.LIGHTRED_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)



# Placing obstacles

obj_beam_array = [Beam(0, 0) for i in range(30)]
for i in range (0,30):
    valx = random.randrange(35)
    valy=random.randrange(250)
    obj_beam_array[i]=Beam(valx,valy)

def beams_on_board(flag):
    print(obj_board.flag)
    ang = 0
    for i in range(len(obj_beam_array)):
        obj_beam_array[i].place_beam(ang, obj_board.grid, flag)
        if ang == 90:
            ang = 0
        else:
            ang += 45
    if(flag==0):
        flag=1



# Placing coins
def coins_on_board():
    for i in range(100):
        valx = random.randrange(5, HT-10)
        valy = random.randrange(0, WIDTH-10)
        obj_coin = Coins(valx, valy)
        if(obj_board.grid[valx][valy] == ' 'and obj_board.grid[valx][valy-1] == ' ' and obj_board.grid[valx][valy+2] == ' '):
            obj_coin.place_coin(obj_board.grid)

#Bullets array 
obj_bullets_array=[]


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
    char = user_input()
    if char == 'd':
        ispos = obj_din.check_collision(obj_board.grid)
        if ispos == 1:
            obj_din.din_clear(obj_board.grid)
            obj_din.x_cood += 1
            obj_din.direction = 1
            obj_din.din_show(obj_board.grid, obj_din.x_cood, obj_din.y_cood,obj_din.mode)

        elif ispos == 2:
            obj_din.dec_lives()
            obj_din.dead = 0

        else:
            o = 1

    if char == 'a':
        ispos = obj_din.check_collision(obj_board.grid)

        if ispos == 1:
            obj_din.din_clear(obj_board.grid)
            obj_din.x_cood -= 1
            obj_din.direction = -1
            obj_din.din_show(obj_board.grid, obj_din.x_cood, obj_din.y_cood,obj_din.mode)

        elif ispos == 2:
            obj_din.dec_lives()
            obj_din.dead = 0

    if char == 'q':
    	os.system("killall afplay")
    	quit()

    if char == 'w':
        ispos = obj_din.check_collision(obj_board.grid)
        obj_din.din_clear(obj_board.grid)
        if obj_din.y_cood > 3 :
            obj_din.y_cood -= 1
        else: 
            obj_din.y_cood=3
        obj_din.din_show(obj_board.grid, obj_din.x_cood, obj_din.y_cood,obj_din.mode)
        if ispos==2:
            obj_din.dec_lives()
            obj_din.dead = 0


    if char == ' ':
        if(obj_din.shield_flag==0):
            obj_din.din_clear(obj_board.grid)
            obj_din.x_cood-=1 
            obj_din.y_cood-=4
            obj_din.shield_flag=1
            obj_din.shield_start_time=time.time()


    if char == 'l':
        print(obj_din.x_cood, obj_din.y_cood)
        new_bullet=Bullet(obj_din.y_cood+1, obj_din.x_cood+5)
        new_bullet.place_bullet(obj_board.grid)
        obj_bullets_array.append(new_bullet)


