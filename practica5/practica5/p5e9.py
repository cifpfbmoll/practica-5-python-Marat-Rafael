#autor:Marat-Rafael
"""

Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje de la siguiente manera:
Anchura del rectángulo: 5
Altura del rectángulo: 4
*****
*   *
*   *
*****

"""

#esta mal 

anchura=int(input("introduce la anchura del rectangulo: "))

altura=int(input("introduce la altura del rectangulo: "))

dibujo="*"

for i in range (altura):
    
    for j in range (anchura): 
               
        if (j==0 or j==anchura-1 or i==0 or i==anchura-1):
            
            print ((dibujo),end=" ")
        else:
            print ((" "),end=" ")
            
    print(" ")  
    
   
