# -*- coding: utf-8 -*-
"""
Inteligencia Artificial
Programación I
Trabajo práctico 1
Ejercicio 1

Efrain Pineda
"""
precio = float(input("Ingresa el precio del producto: "))

iva = precio*0.21

precioFinal = precio+iva

print(" El iva de tu producto es de " + str(round(iva,2)) + " pesos")
print("El precio total de tu producto es " + str(round(precioFinal, 2)) + " pesos") 


