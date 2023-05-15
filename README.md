# Learning-Python
This is my *personal* repository of proyects and little programs that i creating for learn about **Python**

# Exercises
  ### PyIMC
  This Python program, calculates your **IMC** (Body Mass Index) and return your body status
  ### Code
  ```python
# Calculadora de IMC (Índice de Masa Corporal)

#Fórmula: IMC = Peso / (Altura x Altura)
#   • IMC < 19: Delgadez
#   • IMC < 20-25: Normal
#   • IMC < 26-30: Sobrepeso
#   • IMC > 30: Obesidad

#Entrada de Datos
Peso = int(input('Ingrese su peso en kg: '));
Altura = int(input('Ingrese su Altura en cm: '));

Altura = Altura / 100; #Se convierte la altura ingresada en cm a m

#Cálculo del IMC
IMC = Peso / (Altura * Altura)

#Se evalua el resultado final
if IMC < 20:
    print('Usted tiene un IMC de: ', IMC, ' su estado es Delgado');
if IMC >= 20 and IMC <= 25:
    print('Su IMC es de: ', IMC, ' su estado es Normal');
if IMC >= 26 and IMC < 30:
    print('Usted tiene un IMC de: ', IMC, ' su estado es Obesidad');
if IMC > 30:
    print('Usted tiene un IMC de ', IMC, ' su estado es Sobrepeso')
```
  
  ### CalcIC 
  This is an automatic and CLI **compound interest** calculator
