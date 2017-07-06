#!/usr/bin/env python
#-*- coding: utf8 -*-

"""
Ejemplo de ambitos en Python
"""

a_global = 10

def funcion_01():
    print "Estoy en una funciÃ³n *funcion_01*"
    print "a_global vale: %d" % a_global

def funcion_02():
    a_global = 20
    print "Estoy en una funciÃ³n *funcion_02*"
    print "a_global vale: %d" % a_global

def funcion_03():
    global a_global
    a_global = 30
    print "Estoy en una funciÃ³n *funcion_03*"
    print "a_global vale: %d" % a_global


if __name__ == '__main__':

    funcion_01()
    funcion_02()
    funcion_01()
    funcion_03()
    funcion_01()
