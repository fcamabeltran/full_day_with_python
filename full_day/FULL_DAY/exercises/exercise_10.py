#!/usr/bin/env python
#Â -*- coding: utf8 -*-

"""
Subrayar una cadena.
"""

def subrayar(cadena, caracter='*'):
    print cadena
    print '*' * len(cadena)


if __name__ == '__main__':
    print subrayar('Hola')
    print subrayar('Hola', '=')
    print subrayar('Â¡Hola mundo!', '-')
