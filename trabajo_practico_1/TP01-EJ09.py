#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inteligencia Artificial
Programación I
Trabajo práctico 1
Ejercicio 9

Efrain Pineda
"""

angulos = [int(x) for x in input("Ingresa 3 angulos: ").split()]
try:
    for index, item in enumerate(angulos):
        if item == 90:
            print("Tu figura es un triángulo rectángulo")
except:
    print("Tu figura no es un triangulo rectángulo")
       

