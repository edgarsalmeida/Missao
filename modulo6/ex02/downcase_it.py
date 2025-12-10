#!/usr/bin/env python3
import sys

# sys.argv[0] é o nome do script
# sys.argv[1] é o primeiro argumento e depois ele vai transformar em letra minúscula

if len(sys.argv) > 1:
    texto =sys.argv[1]
    print(f"{texto.lower()}")
else:
    # Se não houver argumentos passados
    print("none")
