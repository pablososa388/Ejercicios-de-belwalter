from random import randint
from stack import Stack

##Reemplazar todas las ocurrencias de un determinado elemento en una pila.
##4.
"""
pila= Stack()

for i in range(10):
    pila.push(randint(1,12)) ##meto 20 nros random con entre 1 y 12 incluidos
print("pila original:")
print()
pila.show()##muestro pila
print()

buscar= int(input("ingrese el número deseado: ")) 
pila_aux= Stack()

reemplazo= randint(1,12)

while reemplazo== buscar:
    reemplazo=randint(1,12)

print(f"buscando ocurrencia {buscar} que es reemplazado por {reemplazo}")
while pila.size()>0:
    value= pila.pop()
    if value==buscar:
        pila_aux.push(reemplazo)
    else:
        pila_aux.push(value)
    

while pila_aux.size() > 0:
    value = pila_aux.pop()
    pila.push(value)

print("pila despues del reemplazo:")
pila.show()
"""
##ejercicio 2
##2. Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números
##pares.


"""
pila= Stack()

for i in range(10):
    pila.push(randint(1,20))
print("pila completa:")

print()
pila.show()
print()

pila_aux= Stack()
while pila.size()>0:
    valaux= pila.pop()
    if valaux % 2==0:
        pila_aux.push(valaux)
while pila_aux.size()>0:
    valaux= pila_aux.pop()
    pila.push(valaux)

print()
print("la pila sin elementos impares")
pila.show()
"""


##4 Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.
"""
pila= Stack()
pilaux= Stack()

for i in range(10):
    pila.push(randint(1,9))
print("pila original:")

print()
pila.show()
print()


while pila.size()>0:
    valaux= pila.pop()
    pilaux.push(valaux)

print("pila invertida:")

print()
pilaux.show()
"""
 ##0Determinar si una cadena de caracteres es un palíndromo.

pila=Stack()
pilaux= Stack()
pilaux2= Stack()

buscado=input("ingrese una palabra de la lista para ver si es un palíndromo: ") #buscas la palabra

for letra in buscado:#acá PY lo que hace por defecto es iterar los caracteres del string, por eso no estas metiendo un solo elemento (o sea palabra) a la pila, sino que estas metiendo CADA caracter como un elemento distinto
    pila.push(letra)#aca mandé a dos pilas diferentes la misma palabra para poder compararla invertida
    pilaux.push(letra)#como no la popeaste de otra pila a la palabra, los caracteres van a mantener el orden normal, es decir, no estan invertidos en ninguna de las dos pilas

while pilaux.size()>0:#acá se invierte automaticamente cuando la popeas y la pusheas a una auxiliar
    valaux=pilaux.pop()
    pilaux2.push(valaux)


palindromo= True#aca lo pongo como verdadero al palindromo

while pila.size()>0 and pilaux2.size()>0:
    if pila.pop()!=pilaux2.pop():#acá comparo las dos pilas, una que quedo tal cual como la metimos en el for (pila) y otra invertida (pilaux)
        palindromo= False#si al popearlas y compararlas son distintas palindromo es falso

if palindromo:#acá afuera del while directamente pongo que si es true entonces evidentemente era palindromo la palabra
    print(f"la palabra {buscado} es un palíndromo")
else: # y si no se cumple que sean iguales entonces no es:
    print(f"la palabra {buscado} no es un palíndromo")
##comentario a parte, me olvide de retornar los elementos a la pila original pero me da paja pq necesitaria 2 variables auxiliares en el último while

##6. Leer una palabra y visualizarla en forma inversa.

# pila= Stack()

# palabra=input("ingrese una palabra: ")

# print(f"usted ingresó {palabra}")

# print (f"asi se visualiza invertida")

# for letra in palabra:
#     pila.push(letra)

# while pila.size()>0:
#     print(pila.pop(), end="")
    




