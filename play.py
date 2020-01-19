from headers import *

# importing classes
# from board import Board
# from din import Din
# from background import Background
# from objects import *
from utility import * 

# Start time of the game
start_time = time.time()
screen_time=time.time()
x=time.time()
move=1

os.system('clear')
beams_on_board()
coins_on_board()
power_on_board()


while True:
    newtime = GAMETIME - (round(time.time()) - round(start_time))
    reposition_cursor(0, 0)
    if(newtime == 0 or obj_din.show_lives() <= 0):
        os.system('clear')
        game_over()

        print()
        print("Better luck next time!")
        print("YOUR SCORE IS : ", obj_din.show_coins())
        quit()

    #BOUNDARY CONDITIONS FOR DIN:
    if(obj_din.x_cood < factor+1):
        obj_din.x_cood=factor+1
    if(obj_din.x_cood >= factor+SCREEN-5):
        obj_din.x_cood=factor+SCREEN-5

    #GRAVITY EFFECT
    if(obj_din.show_fly_flag()==0):
        if(obj_din.y_cood  < 35 and obj_din.mode == 0):
            if(obj_din.show_drop_air_time()==0):
                obj_din.set_drop_air_time(obj_din.show_drop_air_time()+1)
            obj_din.gravity(obj_board.grid)
        elif (obj_din.y_cood  < 33 and obj_din.mode == 1):
            if(obj_din.show_drop_air_time()==0):
                obj_din.set_drop_air_time(obj_din.show_drop_air_time()+1)
            obj_din.gravity(obj_board.grid)

    #SHIELD CHECKER
    if(obj_din.shield_flag==1):
        if(time.time()-obj_din.shield_start_time>=10):
            #remove shield after 10s
            obj_din.remove_shield(obj_board.grid)

    #MOVING EXISTING BULLETS:
    for i in range (len(obj_bullets_array)):
        if(obj_bullets_array[i].active==0):
            continue
        if(obj_bullets_array[i].check_collision(obj_board.grid)==1 or obj_bullets_array[i].show_crash()==1): #If collision
            obj_bullets_array[i].active=0
            no_beam(obj_bullets_array[i].x, obj_bullets_array[i].y,obj_board.grid)
            obj_bullets_array[i].clear_bullet(obj_board.grid)
        else:
            obj_bullets_array[i].shoot(obj_board.grid)
        
        if(time.time()-obj_bullets_array[i].start > 10):
            obj_bullets_array[i].active=0
            obj_bullets_array[i].clear_bullet(obj_board.grid)

    print_header(newtime)
     
    #PRINTING DIN
    if obj_din.shield_flag == 0 :
        obj_din.mode = 0
    elif obj_din.shield_flag ==1 :
        obj_din.mode=1

    #POWER UP CHECK
    if(obj_din.power_start_time!=0 and time.time()-obj_din.power_start_time >4):
        obj_din.power_start_time=0
        obj_din.set_power(0)
        move=1


    #MOVING THE BOARD AND MANDO
    if(time.time()-screen_time>=0.4):
        if factor >= WIDTH-SCREEN-1:
            factor = WIDTH-SCREEN-1
            move=0
        elif(obj_din.show_power()==0):
            factor += 1
        elif(obj_din.show_power()==1):
            factor+=4
            move=4
        screen_time=time.time()
        obj_din.din_clear(obj_board.grid)
        obj_din.din_show(obj_board.grid,move+obj_din.x_cood, obj_din.y_cood,obj_din.mode)
    
    #PRINT THE BOARD MAP WITH APPROPRIATE SCREEN WIDTH
    beams_on_board()
    obj_board.print_board(factor)
    movedin()
    