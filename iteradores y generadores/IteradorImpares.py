#Crear un iterador para numeros impares

#Limite
limit = 10

#Crear iterador
iter = iter(range(1,limit+1,2)) # range(start, stop, step) start: por donde empieza
                                #stop: donde para limit+1 = 10
                                #step: numero de posiciones que avanza

#iter = iter(range(2,limit+1,2)) para numeros pares
#Usar iterador
for num in iter:
    print(num)