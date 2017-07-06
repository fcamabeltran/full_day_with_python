"""
Calcular el promedio de notas que ingresa el usuario
de forma interactiva. Las notas deben ser valores flotantes
entre 0.0 y 20.0. Para dejar de ingresar notas, consignar
el valor -1.
"""

NOTA_MINIMA = 0.0
NOTA_MAXIMA = 20.0

NOTA_SALIR = -1.0

if __name__ == '__main__':

    contador_notas = 0
    acumulador_notas = 0

    # Leer N notas
    while True:
        # Leer una nota
        while True:
            try:
                mensaje = "Ingrese una nota entre %.1f y %.1f (%d): "
                mensaje = mensaje % (NOTA_MINIMA, NOTA_MAXIMA, contador_notas)
                valor = float(raw_input(mensaje))
                if valor == NOTA_SALIR:
                    break
                if (valor < NOTA_MINIMA) or (valor > NOTA_MAXIMA):
                    mensaje = "Â¡La nota debe estar entre %.1f y %.1f!"
                    mensaje = mensaje % (NOTA_MINIMA, NOTA_MAXIMA)
                    print mensaje
                    continue
                else:
                    # Todo esta OK con el valor leÃ­do
                    break
            except ValueError:
                mensaje = "Â¡Ingrese una nota entre %.1f y %.1f!"
                mensaje = mensaje % (NOTA_MINIMA, NOTA_MAXIMA)
                print mensaje
        # Ver si es valor para finalizar
        if valor == NOTA_SALIR:
            break
        # Trabajamos con el valor leÃ­do
        acumulador_notas += valor
        contador_notas += 1

    # Calcular resultados
    promedio = 0.0
    if contador_notas > 0:
        promedio = acumulador_notas / float(contador_notas)
    print "Promedio: %.2f" % promedio
