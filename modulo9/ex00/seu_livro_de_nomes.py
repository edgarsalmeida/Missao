#!/usr/bin/env python3

def array_de_nomes(pessoas):
	nomes_completos = []
	for primeiro, sobrenome in pessoas.items():
		nome_completo = primeiro.capitalize() + " " + sobrenome.capitalize()
		nomes_completos.append(nome_completo)
	return nomes_completos
#Teste
pessoas = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

print(array_de_nomes(pessoas))
