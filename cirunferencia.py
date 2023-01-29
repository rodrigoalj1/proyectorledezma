# Creación de un script en Python y prueba de funcionamiento. Cálculo de circunferencias, dados
#  distintos valores de radio, y considerando el valor de pi de 6 decimales. 

import math
# Funcion 
def calculoCircunferencia(radio):
    pi = 3.141592
    return 2 * pi * radio

print("Circunferencia de radio 3: {:.6f}".format(calculoCircunferencia(3)))
print("Circunferencia de radio 8: {:.6f}".format(calculoCircunferencia(8)))
print("Circunferencia de radio 10: {:.6f}".format(calculoCircunferencia(10)))