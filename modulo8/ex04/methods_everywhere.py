#!/usr/bin/env python3

import sys

def shrink(str):
	print(str[0:8])
def enlarge(str):
	while len(str) < 8:
		str+="Z"
	print(str)
lista_argum = sys.argv[1:]
if len(lista_argum) > 0:
	for i in lista_argum:
		if len(i) > 8:
			shrink(i)
		elif len(i) < 8:
			enlarge(i)
		else:
			print(i)
else:
	print("none")
