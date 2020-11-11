#autor:Marat-Rafael
"""
Practica 5
Ejercicio 8

Escribe un programa que pida la anchura de un triángulo y lo dibuje de la siguiente manera:
Altura del triángulo: 4
*
**
***
****
***
**
*

"""

anchura=int(input("Introduce la anchura del triangulo, por favor: "))

print ("Has indicado ancho de: ",anchura)

dibujo="*"

altura=int(anchura)

paso=int(0)

for i in range (altura):
    paso+=1
    for j in range (paso):
        print ((dibujo),end=" ")
    print (" ")
for i in range (altura):
    paso-=1
    for j in range (paso):
        print ((dibujo),end=" ")
    print (" ")
