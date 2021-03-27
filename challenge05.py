#!/usr/bin/env python3

import sys

def main():
	try:
		hex_str = open(sys.argv[1], "r")
		text = hex_str.read()
		test = text.split('\n')
		x = int(len(test[1]) / len(test[0]))
		new = test[0] * (x + 1)
		y = len(new) - len(test[1])
		result = str(hex(int(new[:-y], 16) ^ int(test[1], 16)))
		print(result[2:].upper())
		exit(0)
	except:
		exit(84)

main()