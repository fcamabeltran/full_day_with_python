#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Imprimir aquellos nÃºmeros enteros entre 1 y 100 que
sean divisibles entre 7 o 13.
"""
INICIO = 1
FIN = 100

DIVISOR_01 = 7
DIVISOR_02 = 13

for n in range(INICIO, FIN + 1):
    if (n % DIVISOR_01 == 0) or (n % DIVISOR_02 == 0):
        print n
