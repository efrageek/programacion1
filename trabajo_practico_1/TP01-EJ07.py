#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inteligencia Artificial
Programación I
Trabajo práctico 1
Ejercicio 7

Efrain Pineda
"""

print("""A continuacion, vamos a comprobar las medidas de tus angulos para determinar
      si es un triangulo""")
x, y, z = input("""Ingresa los 3 valores de tus angulos 
                separados por un espacio: """).split()
x = float(x)
y = float(y)
z = float(z)
#Se realiza la suma de los 3 valores
triangulo = x+y+z

#Se revisa si la suma da 180
if triangulo == 180:
    print(f"Tu figura es un triangulo ya que la suma de sus lados es {triangulo} grados")
else:
    print(f"Tu figura no es un triangulo ya que la suma de sus lados es {triangulo} grados")
