# -*- coding: utf8 -*-
import time
msgNum = 0
messages = []
def logg(name,msg):
	global msgNum
	msgNum += 1
	string = '%i Klokken %s sendte %s følgende melding: %s' %(msgNum,parseTime(),name,msg)
	print(string)
	messages.append(string)
def parseTime():
	return '%i:%i:%i' %(time.localtime().tm_hour,time.localtime().tm_min,time.localtime().tm_sec)
def main():
	for i in messages: print(i)
logg('sigurd','heiheihei')
logg('bob','whatever dude, i don`t care')
main()