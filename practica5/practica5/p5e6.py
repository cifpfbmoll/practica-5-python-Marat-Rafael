#autor:Marat-Rafael
"""
Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura del triángulo: 4
*
**
***
****
"""

alt=int(input("introduce la altura del triangulo: "))

print ("has indicado la altuta: ",alt)

anchura=int(0)

dibujo="*"

for i in range(alt):
    
    anchura+=1
    
    print(" ")
    
    for j in range (anchura):
        
        print ((dibujo),end=" ")
        
        
