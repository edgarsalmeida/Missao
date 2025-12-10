#!/usr/bin/env python3

#Definindo o Array origianl
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

#Criando o novo array adicionando 2 a cada valor do array original
new_array = [x + 2 for x in original_array]

#Exibindo os dois arrays na tela
print("Original array:", original_array)
print("New array:", new_array)
