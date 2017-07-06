#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Leer N nÃºmeros enteros DISTINTOS desde el teclado.
"""
OBJETIVO = 5

if __name__ == '__main__':

    n = 1
    numeros = []

    while len(numeros) < OBJETIVO:
        while True:
            try:
                candidato = int(raw_input("\nIngrese un nÃºmero entero: "))
                break
            except ValueError:
                print "El valor ingresado no es un nÃºmero entero."
        if candidato not in numeros:
            numeros.append(candidato)
            print "Â¡Nuevo nÃºmero!"
        else:
            print "Â¡Ya ha sido ingresado!"

    print "Los %d nÃºmeros distintos son\n" % OBJETIVO

    for num in numeros:
        print num
