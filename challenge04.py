#!/usr/bin/env python3

import sys

def get_english_score(input_bytes):
	character_frequencies = {
		'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
		'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
		'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
		'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
		'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
		'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
		'y': .01974, 'z': .00074, ' ': .13000
	}
	return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


def single_char_xor(input_bytes, char_value):
	output_bytes = b''
	for byte in input_bytes:
		output_bytes += bytes([byte ^ char_value])
	return output_bytes

def algo(table):
	l = 1
	best_score2 = 0
	best_line = 0
	best_key = 0
	for line in table:
		ciphertext = bytes.fromhex(line)
		potential_messages = []
		for key_value in range(256):
			message = single_char_xor(ciphertext, key_value)
			score = get_english_score(message)
			data = {
				'message': message,
				'score': score,
				'key': key_value,
				'line': l
				}
			potential_messages.append(data)
		best_score = sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]
		if best_score['score'] > best_score2:
			best_score2 = best_score['score']
			best_line = l
			best_key = best_score['key']
		l = l + 1
		#print(best_score['line'], hex(best_score['key'])[2:].upper())
	print(best_line, hex(best_key)[2:])

def main():
	try:
		file = open(sys.argv[1], "r")
		hexstring = file.read()
		table = hexstring.split('\n')
		#print(table)
		algo(table)
		exit(0)
	except:
		exit(84)

if __name__ == '__main__':
	main()