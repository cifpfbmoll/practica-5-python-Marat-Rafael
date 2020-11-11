#autor:Marat-Rafael
"""
Escribe un programa que pida dos números y escriba la suma de enteros 
desde el primero hasta el último.
Dame un número: 30
Dame otro número mayor que 30: 32
La suma desde 30 hasta a 32 es: 93
30+31+32 = 93
"""

num1=int(input("dame el primer numero: "))

num2=int(input("dame segundo numero mayor que '{0}' :".format(num1)))

num2=num2+1

suma=int(0)

for i in range (num1,num2):
    #empezando por primer numero cada vuelta sumamos siguiente numero
    
    suma=suma+i
    
    #hasta que vueltas no llegen a ultimo numero 
    
    if i<num2-1:
        print ((i),"+",end=" ")
    elif i==(num2-1):
        print ((i),"=",suma)
        

print ("la suma desde",num1," hasta ",num2-1, " es ",suma)

