#!/usr/bin/env python3

import codecs
import base64
import sys

def main():
	try:
		hex_str = open(sys.argv[1], "r")
		encoded_str = base64.b64encode(bytes.fromhex(hex_str.read())).decode('utf-8')
		print(encoded_str)
		exit(0)
	except:
		exit(84)

main()