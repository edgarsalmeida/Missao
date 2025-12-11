#!/usr/bin/env python3

import sys # Importa o módulo sys para acessar argumentos da linha de comando

def verificar_palavra(parametro_esperado):
    """
    Solicita ao usuário para inserir uma palavra e verifica se corresponde ao parâmetro esperado.
    """
    palavra_usuario = input("Por favor, insira uma palavra: ")
    if palavra_usuario == parametro_esperado:
        print("Good job!")
    else:
        print("Nope, sorry...")

# Verifica se exatamente um parâmetro foi passado (excluindo o nome do script)
if len(sys.argv) == 2:
    parametro_passado = sys.argv[1]
    verificar_palavra(parametro_passado)
else:
    print("none")
