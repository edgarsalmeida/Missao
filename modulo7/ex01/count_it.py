#!/usr/bin/env python3

import sys

# sys.argv[0] é o nome do script, então começamos a partir do índice 1
args = sys.argv[1:]

if not args:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for arg in args:
        print(f"{arg} {len(arg)}")
