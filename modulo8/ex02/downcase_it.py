#!/usr/bin/env python3
import sys

lista_argum = sys.argv[1:]

def downcase_it(str):
	print(str.lower())

if len(lista_argum) > 0:
	for i in lista_argum:
		downcase_it(i)
else:
	print("none")
