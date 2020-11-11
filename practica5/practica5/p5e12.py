#autor:Marat-Rafael

"""
Escribe un programa que pida un número y escriba si primo o no
Dame un número: 123
El número 123 no es primo
Dame un número:127
El número 127 es primo

"""
#numero primo se tiene solo dos divisores positivos, uno y si mismo 
#si un numero tiene mas de dos divisores positivos no es primo


numero=int(input("inroduce un numero por favor: "))

primo=True

for i in range (3,numero):
    
    if (numero % i)==0:
        
        primo=False    
          
if (primo==True):
    
    print (("El numero"),numero,"Es un numero primo")
    
else:
    
    print (("El numero"),numero, "No es un numero primo")


"""
#robado en internet

def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    res = d * d > n
    print(res)
    return res
 
 
if __name__ == '__main__':
    n = int(input())
    IsPrime(n)"""
    
    
