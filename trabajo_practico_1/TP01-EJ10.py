#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inteligencia Artificial
Programación I
Trabajo práctico 1
Ejercicio 10

Efrain Pineda
"""

x, y, z = input("""Ingresa los 3 valores de tus angulos 
                separados por un espacio: """).split()
x = float(x)
y = float(y)
z = float(z)

if x<90 and y<90 and z<90:
    print("Tu triango es acutangulo")
else:
    print("Tu triangulo no es acutangulo")
