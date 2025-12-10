#!/usr/bin/env python3

import sys

# Verifica se o número de parâmetros é diferente de 1
if len(sys.argv) != 2:
    print("Erro: O programa espera exatamente um argumento (a string a ser convertida).")
else:
    # Pega a string do primeiro argumento (índice 1)
    texto = sys.argv[1]
    # Converte para maiúsculas e imprime
    print(texto.upper())
