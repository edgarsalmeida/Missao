#!/usr/bin/env python3

#Definindo o Array origianl
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

#Criando o novo array com apenas valores >5, e cada um soma 2 ao seu valor
new_array = [x + 2 for x in original_array if x >5]

#Exibindo os dois arrays na tela
print("Original array:", original_array)
print("New array:", new_array)
