#coding:latin-1
#Practica 5
    #Ejercicio 1
        #linea 1

"""Escribe un programa que escriba a los siguientes número 
(la separación entre número es para facilitar cuántos números se deben escribir 
en cada bucley en el que la función range que utilices tenga un 
ÚNICO argumento y que el valor de este se corresponda con el número de 
elementos que aparecen en la lista por Ejemplo, para la primera lista range (10))."""


lista=(range (10))
for i in range (len(lista)):
    print ((i+1),end=" ")
