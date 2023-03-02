import os
import catalogs
from text import *

class Commands_():
	help_ = 'help'
	clear_ = 'clear'
	cd_ = 'cd'
	open_ = 'open'
	del_ = 'del'
	create_ = 'create'
	ls_ = 'ls'

class Commands_func_():
	def help(self):
		print(help_text)

	def clear_(self):
		os.system('cls||clear')

	def off_(self):
		exit(0)

	def catalog_(self):
		catalog = kt.catalog
		return catalog

	def cd(self, name):
		a = kt.kat
		if name == '/':
			kt.kat = kt.df
		elif name == '':
			print('Напиши хоть слово!')
		else:
			b = f'{a}/{name}'
			kt.kat = b

	def create(self, name):
		if name == '':
			print('Напишите имя файла!')
		else:
			kat = self.katalog()
			katalog_ = f'{kat}/{name}'
			my_file = open(katalog_, "w+")
			my_file.write("")
			my_file.close()
			print('Файл успешно создан!')

	def write(self, name, text):
		my_file = open(name, "a")
		my_file.write(f'{text}\n')
		my_file.close()

	def ls(self):
		katalog_ = self.katalog()
		files = os.listdir(katalog_)
		for file in files:
			print(file)