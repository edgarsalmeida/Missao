#!/usr/bin/env python3

import sys
import re

# Verifica se o número de parâmetros é exatamente 2
if len(sys.argv) != 3:
    print("none")
else:
    palavra_chave = sys.argv[1]
    string_pesquisa = sys.argv[2]
    
    # Usa re.findall para encontrar todas as ocorrências da palavra-chave (como palavra inteira)
    # \b garante que encontra palavras inteiras, não partes de palavras (ex: 'sol' em 'girassol')
    ocorrencias = re.findall(r'\b' + re.escape(palavra_chave) + r'\b', string_pesquisa)
    
    # Se a lista de ocorrências estiver vazia (a palavra não foi encontrada)
    if not ocorrencias:
        print("none")
    else:
        # Se encontrou, imprime o número de vezes que apareceu
        print(len(ocorrencias))
