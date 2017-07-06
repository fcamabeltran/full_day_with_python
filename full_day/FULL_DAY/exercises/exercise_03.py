#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Encontrar los primeros M numeros enteros positivos divisibles entre 7 Ã³ 13.
"""
OBJETIVO = 32

DIVISOR1 = 7
DIVISOR2 = 13

if __name__ == '__main__':
    n = 1
    contador = 0
    while True:
        if (n % DIVISOR1 == 0) or (n % DIVISOR2 == 0):
            contador += 1
            print n
        if contador == OBJETIVO:
            break
        n += 1
