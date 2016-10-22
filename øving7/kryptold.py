# -*- coding: utf8 -*-
import binascii

def toHex(word):
	return int(str(binascii.hexlify(word), 'ascii'))

def toString(word):
	return str((binascii.unhexlify(str(word))), 'ascii')

def encrypt(msg,key):
	if len(msg) != len(key): return "Strings of unequal size"
	msg, key = bytes(msg, 'ascii'), bytes(key, 'ascii')
	return toHex(msg) ^ toHex(key)

def decrypt(crypt,key):
	crypt = str_base(crypt,10)
	if len(crypt) != len(key): return "Strings of unequal size"
	crypt, key = bytes(crypt, 'ascii'), bytes(key, 'ascii')
	return toString(toHex(crypt)) ^ toString(toHex(key))

def digit_to_char(digit):
	if digit < 10: return chr(ord('0') + digit)
	else: return chr(ord('a') + digit - 10)

def str_base(number,base):
	if number < 0:
		return '-' + str_base(-number,base)
	else:
		(d,m) = divmod(number,base)
		if d:
			return str_base(d,base) + digit_to_char(m)
		else:
			return digit_to_char(m)