import time
import json
import handler

com = handler.Commands_()
cfunc = handler.Commands_func_()

class Starting():

	def starting_():
		for i in range(2):
			print('Wait')
			time.sleep(0.3)
			cfunc.clear_()
			print('Wait.')
			time.sleep(0.3)
			cfunc.clear_()
			print('Wait..')
			time.sleep(0.3)
			cfunc.clear_()
			print('Wait...')
			time.sleep(0.3)
			cfunc.clear_()
			print('Wait..')
			time.sleep(0.3)
			cfunc.clear_()
			print('Wait.')
			time.sleep(0.3)
			cfunc.clear_()

	def main_(handler):
		if handler[:5] == com.clear_:
			cfunc.clear_()
		elif handler == com.help_:
			cfunc.help()
		elif handler[:6] == com.create_:
			cfunc.create(commands[7:])
		elif handler[:2] == com.ls_:
			cfunc.ls()
		elif handler[:2] == com.cd_:
			cfunc.cd(commands[3:])

Starting.starting_()
while True:
	commands = input('Catos<3 ')
	Starting.main_(commands)