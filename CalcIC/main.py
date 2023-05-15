# Calculadora de Interes Compuesto
    #El Interes Compuesto es el cálculo de los intereses generados en
    #un periodo de tiempo agregados a un capital inicial, para luego
    #calcular los intereses sobre el nuevo saldo acumulado
    # "ganar intereses sobre intereses "

#Fórmula
#   montoAcumulado = capitalInicial * (1 - tasaInteres/n) ^ (n * tiempo)

#Variables
capitalInicial = float(input('Ingrese su Capital Inicial: '));
tasaInteres = float(input('Ingrese el porcentaje de interés: '));
n = int(input('Ingrese el número de veces que se compone el interés: '));
tiempo = int(input('Ingrese la duración de la inversión (en meses): '));

tasaInteres = tasaInteres / 100; #Se convierte el porcentaje a decimal
tiempo = tiempo / 12; #Se convierten los meses en años

#Se cálcula el Interés Compuesto
montoAcumulado = capitalInicial * (1 + (tasaInteres / n)) ** (n * tiempo)

#Se imprime el Interés Compuesto
print('El monto acumulado después de ', tiempo, " años es: ", montoAcumulado);