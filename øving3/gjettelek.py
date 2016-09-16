import random
def begin():
	cap = int(input('Bestem øvre grense for tilfeldig tall: '))
	ran = random.randint(1,cap)
	#print(ran) #debug
	guess = 0
	while guess is not ran:
		guess = int(input('Gjett på et tall: '))
		delta = ran - guess
		if delta is 0: break
		elif delta > 0: s = 'høyere'
		elif delta < 0: s = 'lavere'
		print('Det riktige tallet er',s)
	print('Korrekt!')
begin()