#En python se pueden crear listas o arreglos en los que podemos almacenar diferentes tipos de datos e incluso otros datos compuestos.

lista = ["Haziel", "Soy Haziel", True, 1.79];

print(lista); #Esto imprime toda la lista de valores

print(lista[1]); #Con esto le indicamos que queremos retornar el valor que se encuentra en ese índice indicado.

        #Tuplas, Listas, Conjuntos y Diccionarios
    #Una lista permite almacenar datos y valores, estas listas pueden mutar (cambiar)
mi_lista = [1,2,3];
mi_lista.append(4); #append permite agregar un objeto o dato a la lista, por defecto se agrega al final de la lista
mi_lista[0] = 0;
print(mi_lista) #salida final: [0,2,3,4]

    #Una tupla por su lado es un almacen de datos que es inmutable (no puede cambiar)
tupla = (1,2,3);
#tupla.append(4); #Esto devuelve error, puesto que una tupla es inmutable

print(tupla); #Salida final: (1,2,3)

    #Para crear un Conjunto se hace uso de la función set, estos conjuntos no tienen índices y no pueden tener datos duplicados
conjunto = {10};

#A pesar de que son inmutables, sí puede cambiar su estructura, pero no modificar sus valores
conjunto = set({ 1,2,3,4,1}) 

print(conjunto); #A pesar de tener dos "1", el resultado es: {1,2,3,4}

    #Para los diccionarios son similares a los conjuntos, pero sí cuentan con un "índice" o orden
diccionario = {
    'Nombre' : "Haziel", #Nombre es como el índice 0
    'Edad' : 18,    #Edad es como el índice 1
    'Carrera' : "DSM"   #Carrera es como el índice 2
}

print(diccionario['Nombre']); #Devuelve Haziel