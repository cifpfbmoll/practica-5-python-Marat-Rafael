#autor:Marat-Rafael

"""Escribe un programa que pida dos números y escriba qué números entre ese 
par de números son pares y cuáles impares"""

num1=int(input("introduce primer numero por favor: "))
num2=int(input("introduce segundo numero, mayor que '{0}' : ".format(num1)))

for i in range(num1,num2):
    if i%2==0:
        print ((i),"es un numero par")
    else:
        print ((i),"es un numero impar")