#!/usr/bin/env python3

#Definindo o Array origianl
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

#Criando o novo array aparece somente os > 5, somando a cada um 2 e removendo as duplicatas usando o set
new_set = set([x + 2 for x in original_array if x >5])

#Exibindo os dois arrays na tela
print("Original array:", original_array)
print("New array:", new_set)
