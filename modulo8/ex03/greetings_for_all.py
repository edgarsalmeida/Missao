#!/usr/bin/env python3

def greetings(nome="noble stranger"):
	if isinstance(nome, str) == False:
		print("Error! It was not a name.")
	else:
		print(f"Hello, {nome}")

greetings("Alexandra")
greetings("Will")
greetings()
greetings(42)
