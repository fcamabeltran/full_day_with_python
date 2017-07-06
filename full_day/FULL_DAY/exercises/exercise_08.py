#!/usr/bin/env python
#Â -*- coding: utf8 -*-

"""
Implementar una funcionn que segÃºn una cadena de texto que represente
la operacion devuelva otra funcion que implemente dicha operacion
para dos argumentos "a" y "b".

'+' -> suma
'-' -> resta
'*' -> multiplicaciÃ³n
'/' -> divisiÃ³n
'%' -> resto de la divisiÃ³n
'^' -> potencia
"""

def obtener_operacion(operador):
    def suma(a, b):
        return a + b
    def resta(a, b):
        return a - b
    def multiplicacion(a, b):
        return a * b
    def division(a, b):
        return a / b
    def modulo(a, b):
        return a % b
    def potencia(a, b):
        return a ** b
    mapa = {
        '+': suma,
        '-': resta,
        '*': multiplicacion,
        '/': division,
        '%': modulo,
        '^': potencia
    }
    if operador in mapa:
        return mapa[operador]


if __name__ == '__main__':

    potencia = obtener_operacion('^')
    print "2 a la 10: %d" % potencia(2, 10)

    division = obtener_operacion('/')
    print "100 entre 4: %d" % obtener_operacion('/')(100, 4)
