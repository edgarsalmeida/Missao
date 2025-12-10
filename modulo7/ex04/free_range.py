#!/usr/bin/env python3

import sys
numeros = []
lista_argum = sys.argv[1:]
if len(sys.argv) > 2:
    print(sys.argv)
    for i in range(int(lista_argum[0]), int(lista_argum[1])+1):
        numeros.append(i)
else:
	print("none")
if len(numeros) > 0:
	print(numeros)
