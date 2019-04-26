# -*- coding: utf-8 -*-
"""
Inteligencia Artificial
Programación I
Trabajo práctico 1
Ejercicio 3

Efrain Pineda
"""

n1 = int(input("Escribe el primer número: "))
n2 = int(input("Escribe el segundo número: "))

if n1<n2:
    print(f"El número menor es {n1}")
elif n1==n2:
    print("Los número son iguales")
else:
    print(f"El número menor es {n2}")