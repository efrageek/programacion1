#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inteligencia Artificial
Programación I
Trabajo práctico 1
Ejercicio 11

Efrain Pineda
"""

print("""A continuacion, vamos a comprobar las medidas de tus angulos para determinar
      si es un triangulo""")
angulos = [float(x) for x in input("Ingresa 3 angulos: ").split()]

#Se se suman los angulos
triangulo = sum(angulos)

if triangulo==180:
    for index, item in enumerate(angulos):
        if item > 90:
            print("Tu figura es un obtusangulo")
        if item == 90:
            print("Tu figura es un triangulo rectangulo")            
    x=angulos[0]
    y=angulos[1]
    z=angulos[2]
    if x<90 and y<90 and z<90:
        print("Tu triango es acutangulo")
    else:
        print("Tu triangulo no es acutangulo")
else:
    print("Tu figura no es un triangulo")        

    
        
                


