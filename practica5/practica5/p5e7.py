#autor:Marat-Rafael

"""
Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura del triángulo: 4
****
***
**
*

"""

altura= int(input("introduce la altura del triangulo, por favor: "))

anchura=int(altura+1)

print ("Has indicado la altura",altura)

dibujo="*"

for i in range (altura):
    
    anchura-=1
    
    for j in range (anchura):
        
        print ((dibujo),end=" ")
        
    print (" ")
    
    
    