from headers import *
from utility import * 

# Start time of the game
start_time = time.time()
screen_time=time.time()
x=time.time()
move=1

os.system('clear')
beams_on_board()
coins_on_board()
create_power()
power_on_board()


while True:

    newtime = GAMETIME - (round(time.time()) - round(start_time))
    reposition_cursor(0, 0)
    if(newtime == 0 or obj_din.show_lives() <= 0):
        os.system('clear')
        game_over()

        print()
        if(obj_din.show_lives() <= 0):
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"LIVES OVER :(".center(SCREEN)+Style.RESET_ALL)
        print(Fore.MAGENTA+Style.BRIGHT+"BETTER LUCK NEXT TIME!".center(SCREEN)+Style.RESET_ALL)
        print(Fore.MAGENTA+Style.BRIGHT+"YOUR SCORE IS : ".center(SCREEN)+Style.RESET_ALL, Fore.MAGENTA+Style.BRIGHT+str(obj_din.show_coins()*10).center(SCREEN)+Style.RESET_ALL)
        quit()

    #BOUNDARY CONDITIONS FOR DIN:

    if(obj_din.show_magnet_flag()==0):
        if(obj_din.getx() < factor+1):
            obj_din.setx(factor+1)
        if(obj_din.getx() >= factor+SCREEN-5):
            obj_din.setx(factor+SCREEN-5)
    elif(obj_din.getx() < factor+1):
            os.system('clear')
            game_over()
            print()
            print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"DON'T LET THE MAGNET DEFEAT YOU!".center(SCREEN)+Style.RESET_ALL)
            print(Fore.MAGENTA+Style.BRIGHT+"BETTER LUCK NEXT TIME!".center(SCREEN)+Style.RESET_ALL)
            print(Fore.MAGENTA+Style.BRIGHT+"YOUR SCORE IS : ".center(SCREEN)+Style.RESET_ALL, Fore.MAGENTA+Style.BRIGHT+str(obj_din.show_coins()*10).center(SCREEN)+Style.RESET_ALL)
        
            quit()

    #GRAVITY EFFECT
    if(obj_din.show_fly_flag()==0 and obj_din.show_magnet_flag()==0):
        if(obj_din.gety()  < 35):
            if(obj_din.show_drop_air_time()==0):
                obj_din.set_drop_air_time(obj_din.show_drop_air_time()+1)
            obj_din.gravity(obj_board.grid)
        
    #SHIELD CHECKER
    if(obj_din.show_shield_flag()==1):
        if(time.time()-obj_din.show_sstart_time()>=10):
            #remove shield after 10s
            obj_din.remove_shield(obj_board.grid)

    #MOVING EXISTING BULLETS:
    for i in range (len(obj_bullets_array)):
        if(obj_bullets_array[i].active==0):
            continue
        if(obj_bullets_array[i].check_collision(obj_board.grid,obj_dragon,1)==1 or obj_bullets_array[i].show_crash()==1): #If collision with beams
            obj_bullets_array[i].active=0
            no_beam(obj_bullets_array[i].getx(), obj_bullets_array[i].gety(),obj_board.grid)
            obj_bullets_array[i].clear_bullet(obj_board.grid)
        elif(obj_bullets_array[i].check_collision(obj_board.grid, obj_dragon,2)==2):
            o=1
        
        else:
            obj_bullets_array[i].shoot(obj_board.grid)
        
        if(time.time()-obj_bullets_array[i].start > 10):
            obj_bullets_array[i].active=0
            obj_bullets_array[i].clear_bullet(obj_board.grid)

    print_header(newtime)

    #Check Magnet
    check_magnet(obj_din, obj_board.grid)
     
    #PRINTING DIN
    if obj_din.show_shield_flag() == 0 :
        obj_din.set_mode(0)
    elif obj_din.show_shield_flag() ==1 :
        obj_din.set_mode(1)

    #POWER UP CHECK
    if(obj_din.show_pstart_time()!=0 and time.time()-obj_din.show_pstart_time()>5):
        obj_din.set_pstart_time(0)
        obj_din.set_power(0)
        move=1


    #MOVING THE BOARD AND MANDO
    # print(factor)
    if(time.time()-screen_time>=0.1):
        if factor >= WIDTH-SCREEN-1:
            factor = WIDTH-SCREEN-1
            move=0
            #DRAGON MANDO FIGHT BEGINS!!!!
            obj_dragon.move_dragon(obj_board.grid,obj_din.gety())
            
            if(time.time()-obj_dragon.get_shootstart()>=1):
                obj_dragon.set_shootstart(time.time())
                create_shoot_iceballs(obj_board.grid)
            elif(obj_dragon.get_lives()<=0):
                os.system('clear')
                game_over()
                os.system('aplay -q ./sounds/win.wav&')
                print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"YOU WON!".center(SCREEN)+Style.RESET_ALL)
                print(Fore.MAGENTA+Style.BRIGHT+"YOUR SCORE IS : ".center(SCREEN)+Style.RESET_ALL+Fore.MAGENTA+Style.BRIGHT+str(obj_din.show_coins()*10).center(SCREEN)+Style.RESET_ALL)
                quit()
            move_iceballs()           

        elif(obj_din.show_power()==0):
            factor += 1
        elif(obj_din.show_power()==1):
            factor+=4
            if(factor >= WIDTH-SCREEN-1):
                move=0
            else:
                move=4
        screen_time=time.time()
        obj_din.din_clear(obj_board.grid)
        obj_din.din_show(obj_board.grid,move+obj_din.getx(), obj_din.gety(),obj_din.show_mode())
    
    #PRINT THE BOARD MAP WITH APPROPRIATE SCREEN WIDTH
    beams_on_board()
    obj_board.print_board(factor)
    movedin()
    obj_magnet.show(obj_board.grid,obj_magnet.shape,obj_magnet.getx(), obj_magnet.gety())
    power_on_board()
    