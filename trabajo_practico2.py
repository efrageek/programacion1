# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:12:41 2019

@author: Alumno
"""
# ----------------------Aquí comienza el ejercicio 1----------------------------


def ejercicio1():
    def lanzarDado():
        from random import randint
        return randint(1, 6)
# Álvaro lanza el dado
    alvaro=input("Álvaro, escribe <<lanzar>> para jugar tu dado: ")

    if alvaro == "lanzar":
        dado_alvaro = lanzarDado()
        print(f"Tu dado sacó un {dado_alvaro}")
    else:
        print("Debes escribir <<lanzar>> para lanzar tu dado: ")
# Bárbara lanza el dado
    barbara=input("Te toca a ti Bárbara, escribe <<lanzar>> para lanzar tu dado ")
    
    if barbara == "lanzar":
        dado_barbara= lanzarDado()
        print(f"Tu dado sacó un {dado_barbara}")
# Se comparan los dos numeros
    if dado_alvaro > dado_barbara:
        print(f"¡Gana Álvaro con un {dado_alvaro}!")
    elif dado_alvaro < dado_barbara:
        print(f"¡Gana Bárbara con un {dado_barbara}!")
    else:
        print("¡Es un empate!")      
# --------------------------Aquí termina el ejercicio 1-----------------------

# -------------------------Aquí comienza el ejercicio 2-----------------------


def ejercicio2():
    def lanzarDado():
        from random import randint
        return randint(1,6)
    
# david lanza sus dado
    david=input("David, escribe <<lanzar>> para jugar tus dados: ")

    if david == "lanzar":
        dado_david1= lanzarDado()
        dado_david2= lanzarDado()
        puntaje_david = dado_david1+dado_david2
        print(f"Tus dados suman {puntaje_david}")
    else:
        print("Debes escribir <<lanzar>> para lanzar tu dado")
# carmen lanza sus  dados
    carmen=input("Carmen, escribe <<lanzar>> para jugar tus dados: ")

    if carmen == "lanzar":
        dado_carmen1= lanzarDado()
        dado_carmen2= lanzarDado()
        puntaje_carmen=dado_carmen1+dado_carmen2
        print(f"Tus dados suman {puntaje_carmen}")
    else:
        print("Debes escribir <<lanzar>> para lanzar tus dados")
# Se comparan los dos numeros
    if puntaje_david > puntaje_carmen:
        print(f"¡Gana David con un {puntaje_david}!")
    elif puntaje_david < puntaje_carmen:
        print(f"¡Gana Carmen con un {puntaje_carmen}!")
    else:
        if dado_david1>dado_carmen1 or dado_david1>dado_carmen2 or dado_david2>dado_carmen1 or dado_david2>dado_carmen2:
            print("¡Empate! pero gana David por haber sacado el dado de mayor número")
        else:
            print("¡Empate! pero gana Carmen por haber sacado el dado de mayor número")

# -------------------------Aquí termina el ejercicio 2------------------------

# -------------------------Aquí comienza el ejercicio 3-----------------------


def ejercicio3():
    from random import randint

    def lanzarMano():
        return randint(1,3)
    ines= lanzarMano()
    juan= lanzarMano()
    
    # Se vincula un numero con alguna de las figuras del juego
    if ines == 1:
        ines_mano = "piedra"
    elif ines == 2:
        ines_mano = "papel"
    else:
        ines_mano = "tijera"
    
    if juan == 1:
        juan_mano = "piedra"
    elif juan == 2:
        juan_mano = "papel"
    else:
        juan_mano = "tijera"
    
    # Se determina un ganador
        
    if ines == 1 and juan == 2:
        print(f"""Ines saca {ines_mano}
        Juan saca {juan_mano}
        Gana Juan""")
    elif ines == 1 and juan == 3:
        print(f"""Ines saca {ines_mano}
        Juan saca {juan_mano}
        Gana Ines""")
    elif ines == 2 and juan == 1:
        print(f"""Ines saca {ines_mano}
        Juan saca {juan_mano}
        Gana Ines""")
    elif ines==2 and juan==3:
        print(f"""Ines saca {ines_mano}
        Juan saca {juan_mano}
        Gana Juan""")
    elif ines==3 and juan==1:
        print(f"""Ines saca {ines_mano}
        Juan saca {juan_mano}
        Gana Juan""")
    elif ines==3 and juan==2:
        print(f"""Ines saca {ines_mano}
        Juan saca {juan_mano}
        Gana ines""")
    elif ines==juan:
        print(f"""Ines saca {ines_mano}
        Juan saca {juan_mano}
        Es un empate""")
    else:
        print(f"""Ines saca {ines_mano}
        Juan saca {juan_mano}
        Gana Juan""")

        
# -------------------------Aquí termina el ejercicio 3-----------------------

# -------------------------Aquí comienza el ejercicio 4-----------------------


def ejercicio4():
    n1 = float(input("Ingrese el primer numero: "))
    n2 = float(input("Ingrese el segundo numeri: "))

    if n1 > n2:
        print(f"{n1} es mayor que {n2}")
    elif n1 < n2:
        print(f"{n2} es mayor que {n1}")
    else:
        print("Los numeros son iguales")

# -------------------------Aquí termina el ejercicio 4-----------------------


# -------------------------Aquí comienza el ejercicio 5-----------------------

def ejercicio5():
    n1 = float(input("Ingrese el primer numero: "))
    n2 = float(input("Ingrese el segundo numero: "))
    n3 = float(input("Ingrese el tercer numero: "))

    if n1 > n2 and n1 == n3:
        print(f"{n1} y {n3} son los numeros mayores")
    elif n1 == n2 and n1 > n3:
        print(f"{n1} y {n2} son los numeros mayores")
    elif n2 == n3 and n2 > n1:
        print(f"{n2} y {n3} son los numeros mayores")
    elif n1 > n2 and n1 > n3:
        print(f"{n1} es el numero mayor")
    elif n2 > n1 and n2 > n3:
        print(f"{n2} es el numero mayor")
    elif n3 > n1 and n3 > 2:
        print(f"{n3} es el numero mayor")
    else:
        print("Los numeros son iguales")

# -------------------------Aquí termina el ejercicio 5-----------------------



# -------------------------Aquí comienza el ejercicio 6-----------------------

def ejercicio6():
    caracter = input("Ingresa un caracter: ")

    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        print(f"'{caracter}' es una vocal.")
    elif caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U":
        print(f"'{caracter}' es una vocal.")
    else:
        print(f"{caracter} no es una vocal.")

# -------------------------Aquí termina el ejercicio 6-----------------------


# -------------------------Aquí comienza el ejercicio 7-----------------------

def ejercicio7():
    count = 0
    while count < 100:
        count += 1
        print(f"El contador vale {count} en estos momentos")
    else:
        print("Ya hemos terminado de contar hasta 100")

# -------------------------Aquí termina el ejercicio 7-----------------------


# -------------------------Aquí comienza el ejercicio 8----------------------

def ejercicio8():
    for i in range(101):
        print(i)



# -------------------------Aquí termina el ejercicio 8-----------------------


# -------------------------Aquí comienza el ejercicio 9----------------------

def ejercicio9():
    palabra = input("Ingresa una palabra: ")

    for i in enumerate(palabra):
        print(i)


# -------------------------Aquí termina el ejercicio 9-----------------------


# -------------------------Aquí comienza el ejercicio 10---------------------


def ejercicio10():
    palabra = input("Ingresa una palabra: ")

    for caracter in palabra:
        print(caracter)


# -------------------------Aquí termina el ejercicio 10----------------------


# -------------------------Aquí comienza el ejercicio 11---------------------

def ejercicio11():
    suma = 0
    lista = [1, 2, 3, 4, 5]
    for i in lista:
        suma = suma + i

    print(suma)

# -------------------------Aquí termina el ejercicio 11----------------------


# -------------------------Aquí comienza el ejercicio 12---------------------


def ejercicio12():
    producto = 1
    lista = [2, 4, 5]
    for i in lista:
        producto = producto * i

    print(producto)

# -------------------------Aquí termina el ejercicio 12----------------------


# -------------------------Aquí comienza el ejercicio 13---------------------

def ejercicio13():
    numero = int(input("Ingresa un numero entero: "))
    print(f"Te vamos a mostrar {numero} asteriscos")
    for i in range(numero):
        print("*", end="")

# -------------------------Aquí termina el ejercicio 13----------------------


# -------------------------Aquí comienza el ejercicio 14---------------------

def ejercicio14():
    numero = int(input("Ingresa un numero entero: "))
    caracter = str(input("Ingresa un caracter: "))
    print(f"Te vamos a mostrar '{caracter}' {numero} veces")
    for i in range(numero):
        print(caracter, end="")

# -------------------------Aquí termina el ejercicio 14----------------------


# -------------------------Aquí comienza el ejercicio 15---------------------

def ejercicio15():
    datos = [8, 1, 5]

    for a in range(len(datos)):
        for b in range(datos[a]):
            print("*", end="")
        print("")
