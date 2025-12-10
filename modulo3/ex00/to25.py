#!/usr/bin/env python3

numero = int(input("Enter a number lesss than 25\n"))
if numero > 25:
	print("Error")
else:
	while numero <= 25:
		print(f"Inside the loop, my variable is {numero}")
		numero +=1
