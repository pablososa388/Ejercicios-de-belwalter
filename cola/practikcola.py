from stack import Stack
from queue_ import Queue
#12 Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una función
# que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder los datos.



# personajes = [
#     "Luke Skywalker",
#     "Leia Organa",
#     "Han Solo",
#     "Darth Vader",
#     "Obi-Wan Kenobi",
#     "Yoda",
#     "Anakin Skywalker",
#     "Padmé Amidala",
#     "Boba Fett",
#     "Jango Fett",
#     "Rey",
#     "Finn",
#     "Poe Dameron",
#     "Kylo Ren",
#     "Mace Windu",
#     "Qui-Gon Jinn",
#     "Lando Calrissian",
#     "Ahsoka Tano",
#     "Chewbacca",
#     "Palpatine"
# ]
# 12 Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una función
# que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder los datos.

# pila=Stack()
# pilaux=Stack()
# pilaux2=Stack()
# for pj in personajes:
#     pila.push(pj)

# while pila.size()>0:
#     x=pila.pop()
#     if x=="Leia Organa" or x=="Boba Fett":

#        pilaux.push(x)
#     else:
#         pilaux2.push(x)




# if pilaux.size()>0:
#     print("se encontraron los pj buscados")
#     pilaux.show()
# else: print("no se encontraron")

# while pilaux.size()>0:
#     pila.push(pilaux.pop())

# while pilaux2.size()>0:
#     pila.push(pilaux2.pop())

# print()
# print("pila sin datos perdidos:")
# pila.show()


# Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks

class Personajes:
    def __init__(self,nombre,planeta):
        self.nombre=nombre
        self.planeta=planeta

    def __str__(self):
        return f"{self.nombre}--{self.planeta}"
    

personajes=[
    ("Luke Skywalker", "Tatooine"),
    ("Han Solo", "Corellia"),
    ("Yoda", "Dagobah"),
    ("Jar Jar Binks", "Naboo"),
    ("Leia Organa", "Alderaan"),
    ("Owen Lars", "Tatooine"),
    ("Beru Lars", "Tatooine"),
    ("Wicket W. Warrick", "Endor"),
    ("Padmé Amidala", "Naboo"),
    ("Lando Calrissian", "Socorro")
]       

def cargar(cola:Queue):
    for nombre, planeta in personajes:
        cola.arrive(Personajes(nombre,planeta))
cola=Queue()

# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# 

# def planeta(cola:Queue):
#     print("Personajes de los planetas solicitados:")
#     for i in range(cola.size()):
      
#         planeta=cola.on_front()
    
#         if planeta.planeta=="Alderaan" or planeta.planeta=="Endor" or planeta.planeta=="Tatooine":
#             print(planeta.nombre)
#         cola.move_to_end()

def planeta(cola:Queue):
    colaux=Queue()
    for i in range(cola.size()):
      
        planeta=cola.on_front()
    
        if planeta.planeta=="Alderaan" or planeta.planeta=="Endor" or planeta.planeta=="Tatooine":
         
         colaux.arrive(planeta)
        cola.move_to_end()
    colaux.show()

def planetanatal(cola:Queue):
    colaux=Queue()
    for p in range(cola.size()):
        natal=cola.on_front()   
        if natal.nombre=="Luke Skywalker" or natal.nombre=="Han Solo":
            colaux.arrive(f"planeta natal: {natal.planeta}, de: {natal.nombre}")
        cola.move_to_end()
    colaux.show()
#c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks
def insertar(cola:Queue):
    for i in range (cola.size()): # pepito, juan, arrive walter, move to end yoda
        buscado=cola.on_front()
        if buscado.nombre=="Yoda":
            
            cola.arrive(Personajes("Walter Bel","Tierra"))
            cola.move_to_end()
        cola.move_to_end()
    cola.show()   
def eliminar(cola: Queue):
    esta= False
    for i in range(cola.size()):
        buscado = cola.on_front()
        if esta==True: #esto se activa en la iteracion DESPUES de encontrar a jar jar
            cola.attention()
            esta= False#este se vuelve false despues del attention y nunca mas vuelve a activarse
        elif buscado.nombre == "Jar Jar Binks":
            esta= True##acá la activo para la proxima iteracion eliminar
            cola.move_to_end()
        else:
            cola.move_to_end()
    print("Cola sin el pj ubicado despues de jar jar ")        
    cola.show()


cargar(cola)
# print("cola de pj de los planetas solicitados")
# planeta(cola)
# print()
# print("cola completa")
# cola.show()
# print()
# print("planeta natal de cada personaje solicitado")
# planetanatal(cola)
print("insertados en mi cola:")
insertar(cola)
print("cola completa")
print()

cola.show()
print()
eliminar(cola)
