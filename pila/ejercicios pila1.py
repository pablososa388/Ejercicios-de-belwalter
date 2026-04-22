from random import randint, shuffle
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
##por como lo entiendo, corregime si ves que estoy errado, puedo hacerlo de 2 formas:
##1-cargar una lista como dijimos antes y permitir a un usuario ver esa lista (pila) para elegir una palabra determinada y luego hacer lo necesario par aver si es o no palindromo
##2-no pedirle nada al usuario, con las palabras cargadas, evaluarlas todas directamente  guardar en una pila_aux los palindromos encontrados

"""
pila=Stack()
pilaux= Stack()
pilaux2= Stack()

buscado=input("ingrese una palabra de la lista para ver si es un palíndromo: ")

for letra in buscado:
    pila.push(letra)
    pilaux.push(letra)

while pilaux.size()>0:
    valaux=pilaux.pop()
    pilaux2.push(valaux)


palindromo= True

while pila.size()>0 and pilaux2.size()>0:
    if pila.pop()!=pilaux2.pop():
        palindromo= False

if palindromo:
    print(f"la palabra {buscado} es un palíndromo")
else: 
    print(f"la palabra {buscado} no es un palíndromo")
"""

##6. Leer una palabra y visualizarla en forma inversa.
"""
pila= Stack()

palabra=input("ingrese una palabra: ")

print(f"usted ingresó {palabra}")

print (f"asi se visualiza invertida")

for letra in palabra:
    pila.push(letra)

while pila.size()>0:
    print(pila.pop(), end="")
    
"""
#Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras.

"""
pila= Stack()
pilaux= Stack()

for i in range(10):
    pila.push(randint(1,10))
print("elementos de la pila:")
pila.show()
print()

buscado=int(input("ingrese el número de la posición de la pila que desea eliminar:"))
cont=0
while cont!=buscado-1:
    valaux =pila.pop()
    pilaux.push(valaux)
    cont+=1

pila.pop()

while pila.size()>0:
    valaux=pila.pop()
    pilaux.push(valaux)


while pilaux.size()>0:
    valaux=pilaux.pop()
    pila.push(valaux)

print(f"pila sin el término i-ésimo {buscado} eliminado:")
pila.show()
"""
##Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un mazo de
##cartas de baraja española–,resolver las siguientes actividades:
##a. generar las cartas del mazo de forma aleatoria;
##b. separar la pila mazo en cuatro pilas una por cada palo;
##c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.

class Cartas:
    def __init__(self, palo, numero):
        self.palo= palo
        self.numero= numero

class Mazo:
    def __init__(self):
        self.cartas= Stack()
        self.pilaoro=Stack()
        self.pilaespada= Stack()
        self.pilabasto= Stack()
        self.pilacopa= Stack()
        



    def generar(self):
        listaux=[]
        palos=["oro","espada","basto","copa"]
        for palo in palos:
            for numero in range (1,13):

                carta= Cartas(palo, numero)

                listaux.append(carta)
        shuffle(listaux)
        for carta in listaux:
            self.cartas.push(carta)##me mete todas las cartubis en el Stack de pila


    def separar4palos(self):
        
        while self.cartas.size()>0:
            carta=self.cartas.pop()
            if carta.palo=="oro":
                self.pilaoro.push(carta)
            elif carta.palo=="espada":
                self.pilaespada.push(carta)
            elif carta.palo=="basto":
                self.pilabasto.push(carta)
            else:
                self.pilacopa.push(carta)
    
                

    def ordenar1de4(self):
        pilaux= Stack()
        while self.pilaoro.size()> 0:
            temporal=self.pilaoro.pop()
            while pilaux.size()>0 and pilaux.on_top().numero>temporal.numero:
                temporal2=pilaux.pop()
                self.pilaoro.push(temporal2)
        
            pilaux.push(temporal)
        
        while pilaux.size() > 0:
            self.pilaoro.push(pilaux.pop())




    def showcartas(self):
        auxiliar=Stack()

        while self.cartas.size()>0:
            cartilla=self.cartas.pop()
            print(cartilla.numero,cartilla.palo)
            auxiliar.push(cartilla)

        while auxiliar.size()>0:
            cartilla=auxiliar.pop()
            self.cartas.push(cartilla)

    def showoro(self):
        auxiliar=Stack()

        while self.pilaoro.size()>0:
            cartilla=self.pilaoro.pop()
            print(cartilla.numero,cartilla.palo)
            auxiliar.push(cartilla)

        while auxiliar.size()>0:
            cartilla=auxiliar.pop()
            self.pilaoro.push(cartilla)




mazo = Mazo()
mazo.generar()
print("mazo completo:")
mazo.showcartas()
mazo.separar4palos()
print("pila oro antes de ordenar:")
mazo.showoro()
mazo.ordenar1de4()
print("pila oro ordenada:")
mazo.showoro()