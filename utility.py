from headers import *

def movedin():
    #moves the player
	def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException

	def user_input(timeout=0.15):
		''' input method '''
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
		obj_config.coins_right(obj_board.matrix, obj_mario)
		can_he=obj_mario.check_not_collision_right(obj_board.matrix)

		if(obj_board.matrix[obj_mario.ycoo-5][obj_mario.xcoo + 1] == 'B'):
			obj_board.matrix[obj_mario.ycoo-5][obj_mario.xcoo + 1] = " "

		
		if can_he == 1:
			obj_mario.disappear_mario(obj_board)
			obj_mario.xcoo+=1
			obj_mario.direction = 1
			obj_mario.reappear_mario(obj_board)

		elif can_he == 2:
			obj_mario.life -= 1
			os.system('afplay ./music/mario_dies.wav&')
			obj_board.spawn_mario(obj_mario)
			obj_mario.did_he_die = 0


		else:
			os.system('afplay ./music/bump.wav&')

	if char == 'a':
		
		obj_config.coins_left(obj_board.matrix, obj_mario)
		can_he=obj_mario.check_not_collision_left(obj_board.matrix)

		if(obj_board.matrix[obj_mario.ycoo-5][obj_mario.xcoo + 1] == 'B'):
			obj_board.matrix[obj_mario.ycoo-5][obj_mario.xcoo + 1] = " "
		
		if can_he == 1:
			obj_mario.disappear_mario(obj_board)
			obj_mario.xcoo -= 1
			obj_mario.direction = -1
			obj_mario.reappear_mario(obj_board)

		elif can_he == 2:
			obj_mario.life -= 1
			os.system('afplay ./music/mario_dies.wav&')
			obj_board.spawn_mario(obj_mario)
			obj_mario.did_he_die = 0

		else:
			os.system('afplay ./music/bump.wav&')
				
	if char == 'q':
		os.system("killall afplay")
		os.system('afplay ./music/game_over.wav&')
		quit()
	
	if char == 'w':
		if(obj_board.matrix[obj_mario.ycoo + 3][obj_mario.xcoo] == "-"): #standing on surface

			prev_ycoo=obj_mario.ycoo
			
			while(obj_mario.ycoo != prev_ycoo-8 and # 8 units; checking if there's anything above
				obj_board.matrix[obj_mario.ycoo-1][obj_mario.xcoo+2] == " " and
				obj_board.matrix[obj_mario.ycoo-1][obj_mario.xcoo+1] == " " and
				obj_board.matrix[obj_mario.ycoo-1][obj_mario.xcoo] == " "): 

				obj_mario.disappear_mario(obj_board)
				obj_mario.ycoo -= 1

				obj_mario.reappear_mario(obj_board)

			os.system('afplay ./music/jump.wav&')
			obj_config.check_brick_collision(obj_scenery, obj_board, obj_mario)

	if char == 's':
		obj_board.matrix[obj_mario.ycoo-5][obj_mario.xcoo + 1] = 'B'
		os.system('afplay ./music/bullet.wav&')

		bosskill = obj_bossenemy.check_boss_kill(obj_board, obj_mario)
		# if(bosskill is False):
		# 	obj_board.matrix[obj_mario.ycoo-5][obj_mario.xcoo] = " "
		# else:
		if bosskill is True:
			if(obj_bossenemy.boss_life == 1):
				obj_bossenemy.boss_kill = True
				obj_scenery.remove_barrier(obj_board.matrix)
			else:
				obj_bossenemy.boss_life -= 1