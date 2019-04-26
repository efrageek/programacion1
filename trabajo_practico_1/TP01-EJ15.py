#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inteligencia Artificial
Programación I
Trabajo práctico 1
Ejercicio 15

Efrain Pineda
"""
from random import randint

n1=randint(1,100)
n2=randint(1,100)
operador=randint(1,4)

#Se define el simbolo del operador
if operador==1:
    simbolo="+"
elif operador==2:
    simbolo="-"
elif operador==3:
    simbolo="*"
else:
    simbolo="/"

#Se realiza la operacion
if operador==1:
    operacion=n1+n2
elif operador==2:
    operacion=n1-n2
elif operador==3:
    operacion=n1*n2
else:
    operacion=n1/n2
    
respuesta=float(input(f"Cuanto es {n1} {simbolo} {n2}?: "))
operacion=float(operacion)

if respuesta==operacion:
    print("Tu respuesta es correcta. Felicidades!")
else:
    print(f"Tu respuesta es incorrecta. El resultado correcto es {operacion}")
    



