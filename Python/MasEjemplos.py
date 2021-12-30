print("\n\t***** PROGRAMA *****\n")

# Ejemplo con While infinito
def sumar():
    x = a + b
    print("Resultado: ", x)
def restar():
    x= a - b
    print("Resultado: ", x)
def multiplicar():
    x= a * b
    print("Resultado: ", x)
def dividir():
    x= a / b
    print("Resultado: ", x)

while True:
    try:
        a=int(input("Ingrese el primer número: \n"))
        b=int(input("Ingrese el segundo número: \n"))
        print(" Qué cálculo quieres realizar entre ",a," y ",b,"?\n")
        op = str(input("""#Ofrecemos las opciones de cálculo las cuales van a llamar las funciones
          1- Sumar
          2- Restar
          3- Multiplicar
          4- Dividir\n"""))
        if op=='1':
            sumar()
            break
        elif op=='2':
            restar()
            break
        elif op=='3':
            multiplicar()
            break
        elif op=='4':
            dividir()
            break
        else:
            print("""Has ingresado un número erróneo""")
    except ZeroDivisionError:
        print("Error, no se puede dividir por cero!!")
    except:
        print("Error")
        op="?"
    finally:
        print("Greacias por utilizar nuestra calculadora!!\n")