#autor:Marat-Rafael

"""
Escribe un programa que pida un número e imprima todos sus divisores.
Dame un número: 200
Los divisores de 200 son: 1 2 4 5 8 10 20 25 40 50 100 200

"""


"""
num=int(input("introduce un numero, por favor\n"))
print "Los divisores de ",num," son: ",
div=num
for i in range (num):
    div-=1
    if ((num%div)==0):
        print (div),
        
"""
numero=int(input("introduce un numero por favor: "))

print ("Los divisores de ",numero," son:",end=" ")

divisor=int(0)

#for i in range (numero):

while divisor<numero:
    
    divisor+=1
    
    if (numero%divisor==0):
        
        print ((divisor),end=" ")
        
