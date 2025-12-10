#!/usr/bin/env python3

#Solicitar ao usuário que insira um número
numero = float(input("Me dê um número: "))

#Determinar se o número inserido é decimal ou não e exibir o resultado
if numero.is_integer():
	print("Este número é um inteiro.")
else:
	print("Este número é um decimal.")




