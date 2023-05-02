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

nombreUsuario = "Lucas"; #Definición de variable usando camelCase
nombre_usuario = "Lucas"; #Definición de variable usando snake_case

bienvenida =  "Hola " + nombre_usuario + " ¿Cómo estás?";

print(bienvenida);

    #Es importante aprender a utilizar los FSTRING

nombre = "Lucas";
bienvenida = f"Hola {nombreUsuario} ¿Cómo estás?"


    #Borrar una variable
del nombre;


    #Uso de operadores de IDENTIDAD o PERTENENCIA
print("Hola" in bienvenida) #Retorna true porque Hola sí se encuentra dentro de la variable bienvenida

print("Pedro" not in bienvenida) #Retorna true porque Pedro no se encuentra dentro de la variable bienvenida