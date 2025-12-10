#!/usr/bin/env python3

first_number = int(input("Insira o primeiro número: "))
second_number = int(input("Insira o segundo número: "))

resultado = first_number*second_number
print(f"O resultado da multiĺicação é: {resultado}")

if resultado < 0:
        print("Este número é negativo.")
elif resultado > 0:
        print("Este número é positivo.")
else:
        print("Este número é positivo e negativo")
