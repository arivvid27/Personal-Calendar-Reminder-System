from replit import db
import datetime
from time import sleep

user_secure_name = input('WHAT IS YOUR REPL.IT USERNAME? > ')
user_secure_pass = int(input('WHAT IS YOUR NUMBER PASSWORD? (just enter the password you want to create a password) > \n'))

sleep(2)

if user_secure_name in db and user_secure_pass in db:
	print(f'Hi, {user_secure_name}!')
	while True:
		now = datetime.datetime.now()
		print ("Current date and time is ")
		print (now.strftime("%Y-%m-%d %H:%M:%S"))
		print('Here\'s what\'s inside your locker:')
		keys = db.keys()
		for keys in keys:
			print(keys)
			sleep(5)
		user_locker = input('Would you like to [insert], [Remove], [Update], [Show], [quit], or ([delete] your account?) > ')
		if user_locker == 'insert':
			user_insert_name = input('What the name of the item would you like to add? > ')
			user_insert_value = input('What is the value of the item you would like to add? > ')
			print('INSERTING...')
			db[user_insert_name] = user_insert_value
			sleep(2)
			print('DONE!')
		elif user_locker.lower() == 'remove':
			user_delete = input('What is the item you want to delete? > ')
			print('Deleting...')
			sleep(2)
			del db[user_delete]
			print('Done!')
		elif user_locker.lower() == 'update':
			user_update_item = input('Which item do you want to update? > ')
			user_update_replace = input('What value do you want to replace it with? > ')
			del db[user_update_item]
			db[user_update_item] = user_update_replace
			print('Updating...')
			sleep(2)
			print('Done!')
		elif user_locker.lower() == 'show':
			print('Ok! Here are all your things:')
			for keys in keys:
				print(keys)
			sleep('3')
		elif user_locker.lower() == 'delete':
			print('Ok! Deleting your account...')
			del db[user_secure_name]
			sleep(2)
			print('Deleted!')
			print('This will now terminate...')
			sleep(2)
			exit()
		elif user_locker.lower() == 'quit':
			print('Ok!')
			print('Quitting...')
			print('Bye!')
			sleep(2)
			exit()		
elif user_secure_name in db and user_secure_pass not in db:
	print('Looks like you forgot your password. Let me print your password for you...')
	value = db[user_secure_name]
	print(f' "{value}" ')
	sleep(3)
	print('Now that you have got your password back, please run the program again.')
	sleep(1)
	print('This program will now terminate for you.')
	sleep(2)
	exit()
elif user_secure_name and user_secure_pass not in db:
	print('Looks like you\'re new!')
	print('I am setting your password right now.')
	db[user_secure_name] = user_secure_pass
	sleep(2)
	print('You now have your account!')
	print('Please run the program again to login to your account.')
	sleep(1)
	print('This program will now terminate for you.')
	sleep(2)
	exit()
elif user_secure_name not in db and user_secure_pass in db:
	print('Oops. This password is either already taken, or your spelled your username wrong. Please run the program again and enter a different password for you.')
	sleep(1)
	print('This program will now terminate.')
	sleep(2)
	exit()