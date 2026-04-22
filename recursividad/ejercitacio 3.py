import random
"""
Implementar una función que calcule la suma de todos los números enteros comprendidos
entre cero y un número entero positivo dado.
"""
"""""
numm= int(input("ingrese numero: "))
def suma_enteros(num: int) -> int:
    if num == 0:
        return num
    else:
        return suma_enteros(num-1)+num



print (suma_enteros(numm))

"""
"""
num11=int(input("ingrese un nro: "))
num22=int(input("ingrese otro: "))
def mult(num1, num2: int) -> int:
    if num1==0 or num2==0:
        return 0
    else:
        return mult(num1-1, num2) + num2 ## aca seria ej 4: en num1-1 iria 3, en num2 4. sumamos 4 en cada llamada simplemente, el num1(3) hace de contador. al final sumamos 3 veces 4==12
    
print (mult(num11, num22))
"""
"""
## 4to ejercicio
num1=int(input("ingrese la base: "))
num2=int(input("ingrese la potencia: "))
def potenciarecursiva(num1, num2: int) -> int:
    if num2==0:
        return 1
    else:
        return potenciarecursiva(num1, num2-1)*num1
    
print(potenciarecursiva(num1, num2))
"""
"""
##5to ejercicio
romanos={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500, "M":1000}
num=input("ingrese un número romano: ").upper()
def numrom(num: str) -> int:
    if len(num)==0:
        return 0
    if len(num)==1:## ponemos 1, porque si puse SOLO UN carcter ya sea una "V"  o una "I" o una "M" entonces SE CUMPLE que hay UN caracter y proximamente en el return busca esa "V" desde la posicion 0
        return romanos [num[0]] ##ACA SI SE CUMPLE LO ANTERIOR ME DEVUELVE ESE UNICO STR/CHAR (SUPONGAMOS "I" o "V" o "M" con el valor correspondiente, y lo devuelve como ya coomo INT)
    if romanos [num[0]] < romanos[num[1]]: ##ACA EN[1] (segundo dcaracter/digito toma, se olvida del primero q seria 0, sup`pngamos una "I") HABIA UNO MAYOR, SUPONGAMOS UNA X
        return - romanos[num[0]] + numrom(num[1:]) ## SI LO ANTERIOR ES TRUE, SE RESTA EL PRIMERO POR EL SEGUNDO Y ME QUEDARIA 9 (X-I)
    else: 
        return romanos[num[0]] + numrom(num[1:]) ## y aca suma si el primer caracter es igual o mayor que el segundo

## vale aclarar que el primer digito se busca en el dicc y el segundo ya se llama ala funncion para generar la recursividad, por eso parentesis en vez de corchete
##romanos[num[0]] vs numrom(num[1:])

##romanos[num[0]] → busca en el diccionario el valor del carácter actual, te devuelve un número
##numrom(num[1:]) → llama recursivamente a la función con el resto del string
##Entonces en romanos[num[0]] + numrom(num[1:]) estás diciendo: "el valor del carácter actual más el resultado de procesar el resto del string".
print (numrom(num))
"""
"""
##EJERCICIO NRO 6

#Dada una secuencia de caracteres, obtener dicha secuencia invertida.
"""
"""
char=input("ingrese los caracteres sin espacio: ")

def invert_caract(char: str)-> str:
    if len (char)==0 or len (char)==1:
        return char 
    else:
        return  invert_caract(char[1:]) + char[0] ## con char[0] me aseguro que el primer caracter quede ultimo, con la funcion y el 1: hago llamada recursiva con el caracter 1 en adelante
                                                     ### o sino char[-1] + invert_caract[:-1]
print (invert_caract(char))    
"""
"""
# 7 Desarrollar un algoritmo recursivo que permita calcular la siguiente serie:
#h(n)=1 + 1/2 + 1/3 + ...+ 1/n

n=int(input("ingrese un número: "))

def serie(n:int)->float:
    if n==1:
        return 1
    else:
        return serie(n-1) + (1/n) ##entonces hago ej: 1/3+ 1/2 (por el n-1)+1/1(caso base)

print (serie(n))
"""
"""
## 8 Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario

n=int(input("ingrese un nro: "))

def decabinario(n:int)->str:
    if n==0:
        return  ""
    else:
        return decabinario(n//2) + str(n % 2) 
    ## 11//2=5   +    1
    ## 5//2=2    +    1
    ## 2//2=0    +    0
print (decabinario(n))
## con n=13:
##decabinario(6) + "1"
##decabinario(3) + "0" + "1"
##decabinario(1) + "1" + "0" + "1"
##decabinario(0) + "1" + "1" + "0" + "1"
##"" + "1" + "1" + "0" + "1" = "1101"

## !!!!!!!!! CLAVE !!!!!!!!!!!!!!!!!!! siempre que hago una recursividad, el primer termino del return, que contiene a la funcion, siempre va a ir haciendo la autollamada, mas nunca devolviendo un resultado, el resultado lo va dando el segundo termino del return como en este caso
"""
"""
##ejercicio 9 resolver logb n + logb b

import math

n= int(input("ingrese un numero entero: "))
b= int(input("ingrese un numero base entero: "))
def resolverlogb(n,b:int)->int:
    if n < b:                            ##Cuántas veces tengo que dividir n por b hasta que el resultado sea menor a b?
        return 0
    else:
        return resolverlogb(n/b,b) + 1


print(resolverlogb(n,b))
"""
"""
##10Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.

num=int(input("ingrese un numero entero: "))

def contarentero(num:int)->str:
    if len (num)==0:
        return 0
    else:
        return contarentero(num[1:]) + 1
    
print(contarentero(str(num)))
"""
"""
## 11 Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.
import math
num=int(input("ingrese un numero: "))

def inversion(num:int, aux=0)->int:
    if num ==0:
        return aux
    else:                                         ##ej con num==123
        return inversion(num//10,aux*10 + num%10) ##num//10 divide en enteros, aux(0)*10 es 0,+ num%10 es 3....ahora aux vale 3 y num 12@@ 12//10=1; aux(3)*10= 30+2= 32 aux--->num=1 aux=32@@ ahora 1//10=0; aux(32)*10+ num(1)%10=1, 320+1=321

print (inversion(num))
## 123
   ## invert(num)= invert(123//10 , 0*10 + 123%10)
##                  num div entera,aux*10 + resto de num  
   ##                       12    , 0*10 + 3=  3
   ##                        1    , 3*10 + 2= 32 
   ##                        0    , 32*10 +1= 321
   """
##Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no
##se puede convertir el número a cadena.



##22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
##otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
##objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
##ayuda de la fuerza” realizar las siguientes actividades:

##a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
##queden más objetos en la mochila;

##b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar
##para encontrarlo;

##c. Utilizar un vector para representar la mochila.


mochila= ["manzana","guantes", "agua", "sanguche", "sable de madera","mapa", "cigarrillo"]
if random.choice([True,False]):
    mochila.append("sable de luz")

random.shuffle(mochila)
cont=-1

def usar_la_fuerza(cont:int, mochila: list)-> str:
    cont+=1
    aux=mochila.pop()
    if aux=="sable de luz":
    
        return f"Con ayuda de la fuerza consegui el {aux} despues de sacar {cont} objetos de la mochila! fue el objeto número {cont+1}"
    
    if len(mochila)==0:
        return "Me olvidé de ponerlo en la mochila, no puedo escapar..."
    
    else:
        return usar_la_fuerza(cont,mochila)
    

print(usar_la_fuerza(cont,mochila))
    