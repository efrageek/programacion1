# -*- coding: utf-8 -*-
"""
Inteligencia Artificial
Programación I
Trabajo práctico 1
Ejercicio 5

Efrain Pineda
"""
numero = int(input("Ingresa un número: "))

if numero>=0 and numero <= 10:
    print("El número ingresado está entre 0 y 10")
elif numero>=11 and numero <= 20:
    print("El número ingresado está entre 11 y 20")
elif numero>=21 and numero <= 30:
    print("El número ingresado está entre 21 y 30")
    
else:
    print("El número ingresado es mayor a 30")
