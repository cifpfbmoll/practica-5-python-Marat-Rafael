#autor:Marat-Rafael

"""
Escribe un programa que pida un número y calcule su factorial.
Dame un número: 5
El factorial de 5 es: 120
"""

num_factoral=int(input("Introduce el numero para calcular su factoral: "))

suma=int(1)

for i in range (1,num_factoral+1):
    
    suma=suma*i
    
    if i<num_factoral:
        
        print ((i),"*",end=" ")
        
    elif (i==num_factoral):
        
        print (i)
        
print ("Factoral de '{0}' es : {1}".format(num_factoral,suma))
    


