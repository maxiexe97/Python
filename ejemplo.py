from os import truncate
from typing import NamedTuple


print("\n   **** PROGRAMA ****\n")
#Instrucciones
"""#Instrucciones simples Ejemplo:
b = 12
c = (2 + 1 + 8)
a = 'Hola'
print (a)

#instrucciones compuestas
if b == c:
    print (a)"""

#Ejemplo
""" e = True #InstrucciónSimple
f = False #InstrucciónSimple

if e==True: #Instrucción compuesta 1
    print("instrucción 1")
    if f==True: #Instrucción compuesta 2
        print("instrucción 2")
    if f==False:
        print("instrucción 3")
print("instrucción 4")
 """
#Funciones
""" def suma(parametro1,parametro2):
    Resultado = parametro1 + parametro2
    print("La suma es: ", Resultado)

def resta(parametro1, parametro2):
    Resultado = parametro1-parametro2
    print("La Resta es: ", Resultado)

#llamado
suma(30,10)
resta(30,10)
"""
#condicional if-else
""" a = 2 + 3
if a==4:
    print("a es igual a 4")
else:
    print("a no es igual a cuatro") """

#Condicional if-elif-else
""" print('"a" está entre 4 y 6?')
a=3+2
print(">>> a = ",a)

if a==4:
    print("a es igual a 4")
elif a==5:
    print("a es igual a 5")
elif a==6:
    print("a es igual a 6")
else:
    print("a no está entre 4 y 6")
 """

# OPERADORES
"""
OPERADOR        Funcion                   Ejemplo  Resultado
   +            sumar                       2+2         4
   -            restar                      3-2         1
   *          multiplicar                   2*2         4
   /            dividir                     4/2         2
   %    modulo, devuelve el resto           5%2         1
   **   exponente, exponencial de un num    3**2        9
   //         división entera               5//2        2
"""
""" a=5//2
print(a) """

# OPERADORES DE COMPARACIÓN
"""
operador                    función
    ==      True si los dos valores son exactamente iguales
    !=      True si los dos valores son diferentes
     >      True si el de la izquierda es mayor al de la derecha
     <      True si el de la derecha es mayor al de la izquierda
    >=      True si el de la izquierda es mayor O IGUAL al de la derecha
    <=      True si el de la izquierda es menor O IGUAL al de la derecha
"""
# OPERADORES DE ASIGNACIÓN
"""
OPERADOR        FUNCIÓN
    =       asigna un valor a un elemento
    +=      El primer elemento es igual a la SUMA del primero mas el segundo--->contador incrementa
    -=      El primer elemento es igual a la RESTA del primero con el segundo--->contador decrementa
    *=      El primer elemento es igual al PRODUCTO del primero con el segundo
    /=      El primer elemento es igual a la DIVISIÓN del primero con el segundo
    %=      El primer elemento es igual al MODULO: resto de la división del primero con el segundo
    **=     El primer elemento es igual al RESULTADO DEL EXPONENTE del primero con el segundo
"""
# OPERADORES LOGICOS
"""
OPERADOR    FUNCIÓN
    and     True si y sólo si TODOS los elementos son True
    or      True si ALGÚN elemento es True
    not     es unario, de negación. Nos da True si su elemento es False y viceversa
"""
# OPERADORES ESPECIALES
"""
OPERADOR        FUNCIÓN
  in       (en) Devuelve True si un elemento SE ENCUENTRA dentro de otro
  not in   (no-en) Devuelve True si un elemento NO SE ENCUENTRA dentro de otro
  is       (es) Decvuelve True si los elementos so EXACTAMENTE IGUALES 
  not is   (no-es) Decvuelve True si los elementos so EXACTAMENTE IGUALES 
"""
"""
#ejemplos
a=[1,2,3,4]
j=4
k=4
#print(1 in a)
#print(6 not in a)
#print(j is k)
#print(j is not k)
"""

# BUCLE FOR
"""#sintaxis
    for variable in elemento_iterable:
        cuerpo de la repetición
"""
#Ejemplo
numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for num in numeros:     #en "num" se almacenan los datos iterados de "numeros"
    if num % 2 == 0:    #si es divisible por 2 entonces:
        print(num)      #imprimir la variable "num", numeros pares



print("\n")