#autor: internet

"""
Escribe un programa que pida la altura de un tri√°ngulo y lo dibuje de la siguiente manera:
Altura de un triangulo: 5
    *
   ***
  *****
 *******
*********

"""

#esta mal

#copiado en internet

"""altura=int(input("introduce la altura del triangulo"))
img="X"
for numero_de_fila in range (altura+1):
    print (" "*(altura-numero_de_fila)+img*(2*numero_de_fila-1))""" #  <<< mi tonto cerebro no es capaz de entenderlo
    
altura=int(input("Escribe la altura del tri·ngulo "))
for i in range(altura):
    if (i==altura-1):
        print(" "+((i*2)+1)*"*")
    else:
        print((" "*(altura-i))+(((i*2)+1)*"*"))

    


