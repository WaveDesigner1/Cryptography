import secrets
from binascii import hexlify, unhexlify
import sys
from time import sleep
import os
a = 1

while a == 1:

	msg = input('Wpisz wiadomość do zaszyfrowania, nie używaj polskich znaków ')
	key = '' 
	

	def keyGen(msg, key):
		for i in range(len(msg)):
			key += secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWYZ!@#$%^&*()-=+')
		
		
		return key

	key = keyGen(msg, key)	 
	print('Wiadomość: ', msg)
	print('Twój klucz: ', key + ' Skopiuj lub zapamiętaj')
	i = 1	
	while i < 10:
				
		sleep(1)
		print(i)
			
		i += 1
		if i == 10:
			os.system('clear') # dla Windows - os.system('cls')
			
	def KeyEnc(msg, key):

		EncMsg = msg.encode()
		hexmsg = hexlify(EncMsg)
		hexint = int(hexmsg, 16)
		
		keyGen = key.encode()
		hexkey = hexlify(keyGen)
		keyint = int(hexkey, 16) ^ hexint
		return keyint	

	msg = KeyEnc(msg,key)
	print()
	print('Szyfrogram: ', msg)
	print()

	def Dec(msg, key):
		
		msgDec = key ^ msg
		back2hex = format(msgDec , 'x')
		jawny = unhexlify(back2hex)
		print(jawny)

	Jawny = input('Podaj klucz aby odczytać tekst jawny: ')

	if Jawny == key:
		key = key.encode()
		key = hexlify(key)
		key = int(key, 16)
		print(key)
		msgDec = Dec(msg, key)
		
		
	else:
		print('Podałeś nieprawidłowy klucz...')
	
			
	exit = 'a'
	while exit != 0:
	
		exit = input('Czy chcesz zaszyfrować kolejną wiadomość? (T/N)')
			
		if exit == 'T':
			a = 1
			break
		elif exit == 't':
			a = 1
			break
		elif exit == 'N':
			a = 0
			break
		elif exit == 'n':
			a = 0
			break
		else:
			continue
		
	
	
sys.exit(0)
	


