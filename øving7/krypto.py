import binascii

def toHex(word):
	return int(str(binascii.hexlify(bytes(word, encoding = 'ascii')), 'ascii'), 16)

def toString(word):
	return str(binascii.unhexlify(hex(word)[2:]), 'ascii')

def encrypt(msg, key):
	return toHex(msg) ^ toHex(key)

def decrypt(code, key):
	return toString(code ^ toHex(key))

#k.encrypt("foo","bar")
#k.decrypt(265757,"bar")

def main(msg):
	import string
	import random
	key = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(len(msg)))
	# random.shuffle()?

	encrypted = encrypt(msg, key)
	print('Kryptert melding:', encrypted)

	decrypted = decrypt(encrypted, key)
	print('Dekryptert melding:', decrypted)

	print(key)

#d
# Hacke tid

""" Oppskrift:
Krypter to meldinger med samme nøkkel
Ta xor produktet av de to resulterende kodene
Hvis du kjenner en av meldingene:
	Ta xor med xor produktet og meldingen du kjenner
	Dette returnerer den andre meldingen

Man kan utvikle en mer generell metode, ved å bruke en 
ordbok med ofte brukte ord, og lete gjennom etter to ord som passer
"""


def quickHack(code1,code2):
	dictionary = ['hei','hvordan','hade']
	xor = code1 ^ code2
	for e in dictionary:
		otherWord = decrypt(xor,e)
		if otherWord in dictionary:
			word1 = e
			word2 = otherWord

			key = toString(toHex(word1) ^ code1)

			print('----- Key:',key,'-----')
			print('Msg1:',word1)
			print('Encrypted:',code1,'\n')
			print('Msg2:',word2)
			print('Encrypted:',code2)
			print('------------------------\n')

def hack(code1,code2):
	# Bruk /usr/share/dict/words som ordbok
	#
	with open('/usr/share/dict/wordlist') as f:
		dictionary = f.read().splitlines()
	xor = code1 ^ code2
	for e in dictionary:
		try:
			otherWord = decrypt(xor,e)
			if otherWord in dictionary:
				word1 = e
				word2 = otherWord

				key = toString(toHex(word1) ^ code1)

				print('----- Key:',key,'-----')
				print('Msg1:',word1)
				print('Encrypted:',code1,'\n')
				print('Msg2:',word2)
				print('Encrypted:',code2)
				print('------------------------\n')
		except KeyboardInterrupt:
		        raise
		except:
			lel = 'lel'
""" Tidligere hacks 

TEST 1
>>> k.encrypt("right","posh")
490046233372
>>> k.encrypt("blur","posh")
302188058
>>> k.hack(490046233372,302188058)
----- Key: r{dnn -----
Msg1: blur
Encrypted: 490046233372 

Msg2: right
Encrypted: 302188058
------------------------

----- Key: posh -----
Msg1: right
Encrypted: 490046233372 

Msg2: blur
Encrypted: 302188058
------------------------

TEST 2
>>> k.encrypt("hello","hoho")
446894900224
>>> k.encrypt("john","hoho")
33554433
>>> k.hack(446894900224,33554433)
----- Key: hklas -----
Msg1: foes
Encrypted: 446894900224 

Msg2: hilar
Encrypted: 33554433
------------------------

----- Key: lore -----
Msg1: halve
Encrypted: 446894900224 

Msg2: nord
Encrypted: 33554433
------------------------

----- Key: hoho -----
Msg1: hello
Encrypted: 446894900224 

Msg2: john
Encrypted: 33554433
------------------------
"""