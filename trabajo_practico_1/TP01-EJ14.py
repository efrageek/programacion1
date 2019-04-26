#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inteligencia Artificial
Programación I
Trabajo práctico 1
Ejercicio 14

Efrain Pineda
"""

numero1=round(float(input("Ingresa el primer numero: ")),1)
numero2=round(float(input("Ingresa el segundo numero: ")),1)

if numero1>numero2:
    if numero1%numero2==0:
        print(f"{numero1} es mayor que {numero2} y tambien es multiplo de el")
    else:
        print(f"{numero1} es mayor que {numero2} pero no es multiplo de el")
        
elif numero2>numero1:
    if numero2%numero1==0:
        print(f"{numero2} es mayor que {numero1} y tambien es multiplo de el")
    else:
        print(f"{numero2} es mayor que {numero1} pero no es multiplo de el")
else:
    print("Los numeros son iguales")
            
        
