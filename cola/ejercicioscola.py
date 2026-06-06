from queue_ import Queue
from random import randint


##Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.
"""
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

cola=Queue()

for i in range (20):
    cola.arrive(randint(0,20))
print("Cola con primos:")
cola.show()

for _ in range(cola.size()):
    value=cola.attention()

    if es_primo(value):
        cola.arrive(value)
print("Cola sin primos:")
cola.show()
"""

##Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay.

"""
cola=Queue()

for i in range (20):
    cola.arrive(randint(-10,20))

cola.show()
contneg=0
max=cola.on_front()
min=cola.on_front()
for numeros in range(cola.size()):
    if cola.on_front()<0:
        contneg+=1
 
    if cola.on_front()>max:
        max=cola.on_front()
  
    if cola.on_front()<min:
        min=cola.on_front()
    cola.move_to_end()

rango=max-min

print(f"el rango de la cola es {rango}, y hay {contneg} elementos negativos")
"""

##Eliminar el i-ésimo elemento después del frente de la cola.

cola=Queue()

for i in range (1,10):
    cola.arrive(randint(0,10))

cola.show()

for i in range(randint(1,5)):
    cola.move_to_end()
cola.attention()

print("cola sin el término i-esimoluego del frente: ")

cola.show()
