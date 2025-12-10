#!/usr/bin/env python3

import sys

# sys.argv[0] é o nome do script
# sys.argv[1] é o primeiro argumento, se existir

if len(sys.argv) > 2:
    texto=sys.argv[1:]
    texto.reverse()
    for i in texto:
    	print(i)

else:
    # Se não houver argumentos passados
    print("none")
