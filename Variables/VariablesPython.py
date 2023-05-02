#Python es un lenguaje de programación de tipado dinámico, es decir , no es necesario indicar el tipo de dato de una variable

a = 5;
b = 15;
c = a + b;

print(c);

#Python al igual que otros lenguajes de programación, admite el uso de operadores de asignación:

suma = 10; 
suma +=5;

#Es lo mismo que decir suma = suma ó (10) + 5;

print(suma);

#y también funciona para concatenar cadenas:

nombre = "Lucas";
bienvenida =  "Hola " + nombre + " ¿Cómo estás?";

print(bienvenida);

    #Es importante aprender a utilizar los FSTRING

nombre = "Lucas";
bienvenida = f"Hola {nombre} ¿Cómo estás?"


    #Borrar una variable
del nombre;


    #Uso de operadores de IDENTIDAD
print("Hola" in bienvenida) #Retorna true porque Hola sí se encuentra dentro de la variable bienvenida

print("Pedro" not in bienvenida) #Retorna true porque Pedro no se encuentra dentro de la variable bienvenida