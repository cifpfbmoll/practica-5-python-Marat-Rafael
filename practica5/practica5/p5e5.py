#autor:Marat-Rafael

"""
Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje de la siguiente manera:
Anchura del rectángulo: 5
Altura del rectángulo: 3

*****
*****
*****

"""


anchura=int(input("introduce la anchura del rectangulo: "))
altura=int(input("introduce la altura del rectangulo: "))

print ("Anchura del rectangulo: ",anchura)
print ("Altura del rectangulo: ",altura)
dibujo="*"

for i in range (altura):    
    
    for j in range (anchura):
        
            print ((dibujo),end="")
            
    print (" ")
    
    
    
    