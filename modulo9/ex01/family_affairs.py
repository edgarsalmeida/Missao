#!/usr/bin/env python3

def find_the_redheads(dupont_family):

	return list(filter(lambda name: dupont_family[name] == "red", dupont_family.keys()))

# sua definição de método aqui
dupont_family = {
	"florian": "red",
	"marie": "blond",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
}

print(find_the_redheads(dupont_family))
