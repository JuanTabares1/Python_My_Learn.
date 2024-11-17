def greet(): #Se crea la funcion
    print("Hola mundo")

greet() #Llamar la funcion

def nombre(name): #Crear funcion con el parametro name
    print(name)

nombre("Juan")  #Llamar la funcion pasandole el parametro

def nombreCompleto(name, lastName="Sin apellido"):  #Crear la funcion pidiendo varios parametros
    print("Hola", name, lastName)                #Y lastName="Sin apellido" es por si no se envia ese parametro

nombreCompleto("Juan", "Tabares")  #Se llama la funcion y se le envian los parametros en el orden correcto
nombreCompleto("Jose")  #Se puede llamar mas de una vez
nombreCompleto(lastName="Tabares", name="Juan") #De esta forma no importa el orden, pero siempre ira en orden