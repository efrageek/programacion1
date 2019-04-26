#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inteligencia Artificial
Programación I
Trabajo práctico 1
Ejercicio 13

Efrain Pineda
"""
print("""Es programa te ayudara a determinar tu Indice de Masa Corporal""")
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

#Se calcula el IMC

imc = peso/(altura**2)
imc= round(imc,1)

if imc<20:
    print(f"Te encuentras bajo peso. Tu IMC es de {imc}kg/m2")
elif imc>=20 and imc<30:
    print(f"Tu peso es normal. Tu IMC es de {imc}kg/m2")
elif imc>=30 and imc<40:
    print(f"Tienes sobrepeso ligero. Tu IMC es de {imc}kg/m2")
elif imc<=40 and imc<50:
    print(f"Tienes sobrepeso. Tu IMC es de {imc}kg/m2")
else:
    print(f"Posees obesidad morbida. Tu IMC es de {imc}kg/m2")
