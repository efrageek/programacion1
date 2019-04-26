#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inteligencia Artificial
Programación I
Trabajo práctico 1
Ejercicio 12

Efrain Pineda
"""

print("""A continuacion, vamos a comprobar las medidas de los lados de tu figura para determinar
      si es un triangulo""")
lados = [float(x) for x in input("Ingresa las 3 medidas: ").split()]

#Se se suman los angulos
triangulo = sum(lados)

x=lados[0]
y=lados[1]
z=lados[2]
  
if x+y>z or x+z>y or y+z>x:
  
    if x==y and x==z:
        print("Tu triango es equilatero")
    elif x==y or x==z or y==z:
        print("Tu triangulo es isosceles")
    else:
        print("Tu triangulo es escaleno")
else:
    print("Tu figura no es un triangulo") 