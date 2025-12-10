#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print(sys.argv)
    for i in sys.argv[1:]:
        if i.find("ism") == -1:
            print(i+"ism")

else:
    print("none")
