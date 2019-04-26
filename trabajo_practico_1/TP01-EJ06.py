# -*- coding: utf-8 -*-
"""
Inteligencia Artificial
Programación I
Trabajo práctico 1
Ejercicio 6

Efrain Pineda
"""
importe = float(input("¿Cuál es el importe a pagar?: "))
forma_pago = input("""Cómo desea pagar?
                1. Contado
                2. Cheque
                3. Tarjeta de Crédito
                4. Cuenta corriente
                
                Ingresa el número correspondiente al método de pago: """)

if forma_pago==1:
    print(f"El importe a pagar es de ${importe}")
elif forma_pago==2:
    cheque = importe+(importe*0.03)
    print(f"EL importa a pagar es ${cheque}")
elif forma_pago ==3:
    tarjeta = importe+(importe*0.02)
    print(f"EL importa a pagar es ${tarjeta}")
else:
    cuenta = importe+(importe*0.015)
    print(f"EL importe a pagar es ${cuenta}")
    
    