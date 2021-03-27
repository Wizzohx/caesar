#!/usr/bin/env python3

import sys

def main():
	try:
		hex_str = open(sys.argv[1], "r")
		text = hex_str.read()
		test = text.split('\n')
		result = str(hex(int(test[0], 16) ^ int(test[1], 16)))
		print(result[2:].upper())
		exit(0)
	except:
		exit(84)

main()