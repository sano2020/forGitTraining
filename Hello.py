#print('git training')
from datetime import datetime
import os

def printHello():
	print("Hello")

def printtimeanddate():
	d4 = today.strftime("%b-%d-%Y")
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")

	print("Today: ", d4)
	print("Current Time =", current_time)

def sayHello(name=os.getenv('COMPUTERNAME')):
	print("Hello, ",name)
