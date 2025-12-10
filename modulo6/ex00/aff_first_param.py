#!/usr/bin/env python3
import sys

# sys.argv[0] é o nome do script
# sys.argv[1] é o primeiro argumento, se existir

if len(sys.argv) > 1:
    # Se houver pelo menos um argumento além do nome do script
    print(sys.argv[1])
else:
    # Se não houver argumentos passados
    print("none")
