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

# Placing obstacles

obj_beam_array = [Beam(0, 0) for i in range(30)]
for i in range (0,30):
    valx = random.randrange(25)
    valy=random.randrange(250)
    obj_beam_array[i]=Beam(valx,valy)

val = 10
ang = 0

for i in range(len(obj_beam_array)):
    print(str(obj_beam_array[i].x) + "  " +
          str(obj_beam_array[i].y) + " type "+str(val) + " angle "+str(ang))
    obj_beam_array[i].place_beam(val, ang, obj_board.grid)
    if(val == 30):
        val = 10
    else:
        val += 10
    if ang == 90:
        ang = 0
    else:
        ang += 45
    # TODO PLACE 45 DEGREE BEAMS

# Placing coins
for i in range(100):
    valx = random.randrange(5, HT-10)
    valy = random.randrange(0, WIDTH-10)
    obj_coin = Coins(valx, valy)
    if(obj_board.grid[valx][valy] == ' ' and obj_board.grid[valx][valy+1] == ' ' and obj_board.grid[valx][valy-1] == ' ' and obj_board.grid[valx][valy+2] == ' '):
        obj_coin.place_coin(obj_board.grid)


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
        # obj_config.coins_right(obj_board.matrix, obj_din)
        # ispos = obj_din.check_not_collision_right(obj_board.grid)
        ispos = 1

        if ispos == 1:
            obj_din.din_clear(obj_board.grid)
            obj_din.x_cood += 1
            obj_din.direction = 1
            obj_din.din_show(obj_board.grid, obj_din.x_cood, obj_din.y_cood,obj_din.mode)

        elif ispos == 2:
            obj_din.dec_lives()
            # os.system('afplay ./music/mario_dies.wav&')
            obj_din.start_pos(obj_board.grid)
            obj_din.dead = 0

        else:
            o = 1
            # os.system('afplay ./music/bump.wav&')

    if char == 'a':
        # obj_config.coins_right(obj_board.matrix, obj_din)
        # ispos = obj_din.check_not_collision_right(obj_board.grid)
        ispos = 1

        if ispos == 1:
            obj_din.din_clear(obj_board.grid)
            obj_din.x_cood -= 1
            obj_din.direction = -1
            obj_din.din_show(obj_board.grid, obj_din.x_cood, obj_din.y_cood,obj_din.mode)

        elif ispos == 2:
            obj_din.dec_lives()
            # os.system('afplay ./music/mario_dies.wav&')
            obj_din.start_pos(obj_board.grid)
            obj_din.dead = 0

    if char == 'q':
    	os.system("killall afplay")
    	# os.system('afplay ./music/game_over.wav&')
    	quit()

    if char == 'w':
    # 	if(obj_board.matrix[obj_din.ycoo + 3][obj_din.xcoo] == "-"): #standing on surface

    # 		prev_ycoo=obj_din.ycoo

    # 		while(obj_din.ycoo != prev_ycoo-8 and # 8 units; checking if there's anything above
    # 			obj_board.matrix[obj_din.ycoo-1][obj_din.xcoo+2] == " " and
    # 			obj_board.matrix[obj_din.ycoo-1][obj_din.xcoo+1] == " " and
    # 			obj_board.matrix[obj_din.ycoo-1][obj_din.xcoo] == " "):

        obj_din.din_clear(obj_board.grid)
        if obj_din.y_cood > 3 :
            obj_din.y_cood -= 1
        else: 
            obj_din.y_cood=3
        obj_din.din_show(obj_board.grid, obj_din.x_cood, obj_din.y_cood,obj_din.mode)

    # 		os.system('afplay ./music/jump.wav&')
    # 		obj_config.check_brick_collision(obj_scenery, obj_board, obj_din)


    if char == ' ':
        if(obj_din.shield_flag==0):
            obj_din.din_clear(obj_board.grid)
            obj_din.x_cood-=1 
            obj_din.y_cood-=4
            obj_din.shield_flag=1
            obj_din.shield_start_time=time.time()


    # if char == 's':
    # 	obj_board.matrix[obj_din.ycoo-5][obj_din.xcoo + 1] = 'B'
    # 	os.system('afplay ./music/bullet.wav&')

    # 	bosskill = obj_bossenemy.check_boss_kill(obj_board, obj_din)
    # 	# if(bosskill is False):
    # 	# 	obj_board.matrix[obj_din.ycoo-5][obj_din.xcoo] = " "
    # 	# else:
    # 	if bosskill is True:
    # 		if(obj_bossenemy.boss_life == 1):
    # 			obj_bossenemy.boss_kill = True
    # 			obj_scenery.remove_barrier(obj_board.matrix)
    # 		else:
    # 			obj_bossenemy.boss_life -= 1



# Start time of the game
start_time = time.time()
x=time.time()
move=1

os.system('clear')

while True:
    newtime = GAMETIME - (round(time.time()) - round(start_time))
    reposition_cursor(0, 0)
    if(newtime == 0 or obj_din.show_lives() == 0):
        os.system('clear')
        print("GAME OVER!")
        quit()

    movedin()
    print(factor)

    if factor >= 99:
        factor = 99
        move=0
    else:
        factor += 1

    #GRAVITY EFFECT
    if(time.time()-x >=0.4):
        if(obj_din.y_cood  < 35 and obj_din.mode == 0):
            obj_din.gravity(obj_board.grid)
            x=time.time()
        elif (obj_din.y_cood  < 33 and obj_din.mode == 1):
            obj_din.gravity(obj_board.grid)
            x=time.time()

    #SHIELD CHECKER
    if(obj_din.shield_flag==1):
        if(time.time()-obj_din.shield_start_time>=10):
            #remove shield after 10s
            obj_din.remove_shield(obj_board.grid)


    #HEADER PRINTING 
    print(Fore.WHITE + Back.RED + Style.BRIGHT + "THE MANDALORIAN".center(SCREEN))
    print(Style.RESET_ALL)
    stats = str("LIVES: "+str(obj_din.show_lives()) + "  |  SCORE:" + str(obj_din.show_coins())+"  |  TIME: " + str(newtime))
    print(Fore.WHITE + Back.BLUE + Style.BRIGHT + stats.center(SCREEN), end='')
    print(Style.RESET_ALL)

    #PRINT THE BOARD MAP WITH APPROPRIATE SCREEN WIDTH
    obj_board.print_board(factor)

    #PRINTING DIN
    if obj_din.shield_flag == 0 :
        obj_din.mode = 0
    elif obj_din.shield_flag ==1 :
        obj_din.mode=1

    obj_din.din_clear(obj_board.grid)

    obj_din.din_show(obj_board.grid,move+obj_din.x_cood, obj_din.y_cood,obj_din.mode)
    

