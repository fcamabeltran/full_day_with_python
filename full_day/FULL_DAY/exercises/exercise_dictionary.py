#!/usr/bin/env python
#Â -*- coding: utf8 -*-

"""
Utilizando listas por compresiÃ³n crear una lista de diccionarios
ordenados de la forma:

OrderedDict([
    ('nombre', 'Juan Alberto'),
    ('apellido_paterno', 'Palacios'),
    ('apellido_materno', 'Melchor'),
    ('edad', 38),
    ('telefono', 965321237),
    ('profesion', 'abogado')
])

Al procesar los datos originales:

- Debe eliminarse el "whitespace" al inicio y fin de cada valor
- Deben ignorarse las lÃ­neas en blanco o sin contenido significativo
  que no sea "whitespace"

"""

from collections import OrderedDict

DATA = """
Juan Alberto, Palacios, Melchor, 38, 965321237,  abogado

Maria, VerÃ¡stegui, RÃ­os, 24, 943234042, enfermera
Ronald, BendezÃº, Pendavis, 18, 938732321, programador

"""

def crear_diccionario_ordenado(valores):
    import pdb
    cabecera = [
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'edad',
        'telefono',
        'profesion'
    ]

    lista_de_tuplas = []

    if len(cabecera) != len(valores):
        return None

    for indice, elemento in enumerate(valores):
        t = (cabecera[indice], elemento)
        lista_de_tuplas.append(t)

    #lista_de_tuplas = zip(cabecera, valores)

    return OrderedDict(lista_de_tuplas)


if __name__ == '__main__':

    # Eliminamos espacios en blanco y saltos de lÃ­nea al inicio y al final
    data = DATA.strip()

    # Cortamos por el salto de lÃ­nea y nos quedamos con cada lÃ­nea
    data = data.split('\n')

    # Eliminamos "whitespace" al inicio y el final de cada lÃ­nea
    data = [linea.strip() for linea in data]

    # Eliminamos las lÃ­neas en blanco

    data = [linea for linea in data if len(linea)>0]

    # Separamos los elementos de cada lÃ­nea por coma
    data = [linea.split(',') for linea in data]

    # Eliminamos los espacios en blanco al inicio y fin de cada elemento
    data = [[elemento.strip() for elemento in registro] for registro in data]

    data = [crear_diccionario_ordenado(registro) for registro in data]

    print data
