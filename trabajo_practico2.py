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
    n2 = float(input("Ingrese el primer numeri: "))

    if n1 > n2:
        print(f"{n1} es mayor que {n2}")
    elif n1 < n2:
        print(f"{n2} es mayor que {n1}")
    else:
        print("Los numeros son iguales")

# -------------------------Aquí termina el ejercicio 4-----------------------


# -------------------------Aquí comienza el ejercicio 5-----------------------
