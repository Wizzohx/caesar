#!/usr/bin/env python3

import sys
from base64 import b16decode
from itertools import combinations

CHARACTER_FREQ = {
	'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
	'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
	'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
	'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

def get_english_score(input_bytes):
	result = 0
	for byte in input_bytes:
		result += CHARACTER_FREQ.get(chr(byte).lower(), 0)
	return result

def singlechar_xor(input_bytes, key_value):
	result = b''
	for char in input_bytes:
		result += bytes([char ^ key_value])
	return result

def hamming_distance(str1, str2):
	assert len(str1) == len(str2)
	result = 0
	for x1, x2 in zip(str1, str2):
		temp = x1 ^ x2
		result += sum([1 for bit in bin(temp) if bit == '1'])
	return result

def repeating_key_xor(plaintext, key):
	ciphertext = b''
	i = 0
	for byte in plaintext:
		ciphertext += bytes([byte ^ key[i]])
		i = i + 1 if i < len(key) - 1 else 0
	return ciphertext

def singlechar_xor_brute_force(ciphertext):
	result = []
	for key in range(256):
		message = singlechar_xor(ciphertext, key)
		score = get_english_score(message)
		data = {
			'key': key,
			'score': score,
			'plaintext': message
		}
		result.append(data)
	return sorted(result, key=lambda c: c['score'], reverse=True)[0]

def break_repeating_key_xor(arg):
	calcul = {}
	for key_size in range(2, 41):
		i = [arg[i:i + key_size] for i in range(0, len(arg), key_size)][:4]
		u = 0
		z = combinations(i, 2)
		for (x, y) in z:
			u += hamming_distance(x, y)
		u /= 6
		temp = u / key_size
		calcul[key_size] = temp
	temp = sorted(calcul, key=calcul.get)[:3]
	msg = []
	for d in temp:
		key = b''
		for i in range(d):
			block = b''
			for j in range(i, len(arg), d):
				block += bytes([arg[j]])
			key += bytes([singlechar_xor_brute_force(block)['key']])
		msg.append((repeating_key_xor(arg, key), key))
	return max(msg, key=lambda k: get_english_score(k[0]))

def main():
	with open(sys.argv[1]) as input_file:
		data = b16decode(input_file.read())
	result = break_repeating_key_xor(data)
	result = ''.join(hex(ord(c))[2:] for c in result[1].decode())
	print(result.upper()[:-int(len(result) / 2)])

if __name__ == "__main__":
	main()