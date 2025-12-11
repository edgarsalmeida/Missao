#!/usr/bin/env python3

def add_one(num):
    """Método que recebe um número e retorna ele + 1."""
    # 'num' aqui é uma variável local à função add_one
    print(f"Dentro da função (antes): {num}")
    num = num + 1
    print(f"Dentro da função (depois): {num}")
    return num

# Corpo principal do programa (escopo global/local ao script)
minha_variavel = 8

print(f"No corpo principal (antes da função): {minha_variavel}")

# Chamando a função e armazenando o *resultado* em outra variável
resultado_da_soma = add_one(minha_variavel)

print(f"No corpo principal (depois da função, resultado): {resultado_da_soma}")
print(f"No corpo principal (depois da função, original): {minha_variavel}") 
# Observação principal!
