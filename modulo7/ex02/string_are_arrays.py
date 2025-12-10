#!/usr/bin/env python3

import sys # Importa o módulo sys para acessar argumentos da linha de comando

# Verifica se o número de parâmetros é exatamente 1 (o nome do script + 1 argumento)
if len(sys.argv) != 2:
    print("none") # Se não for 1, exibe "none"
else:
    # Pega a string do argumento (o primeiro argumento é sys.argv[0], o segundo é sys.argv[1])
    texto = sys.argv[1]
    # Verifica se o caractere 'z' está na string
    if 'z' in texto:
        # Itera sobre cada caractere da string
        for char in texto:
            # Se o caractere for 'z', imprime 'z' seguido de uma nova linha
            if char == 'z':
                print("z",end="")
    else:
        # Se não houver 'z' na string, exibe "none"
        print("none")


