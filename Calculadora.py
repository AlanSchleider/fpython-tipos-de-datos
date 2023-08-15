# Lectura del valor de 2 variables enteras por consola:
print("Ingrese el número 1")
numero1 = int(input())
print("Ingrese el número 2")
numero2 = int(input())
print("Ingrese la operación (+, -, *, /)")
operacion = input()

match operacion:
    case 'm':
        # operaqcion modulo:
        modulo = numero1 % numero2
        print("El modulo es: " + str(modulo))
    case 'p':
        # operacion potencia:
        potencia1 = numero1 ** numero1
        potencia2 = numero2 ** numero2
        potencia3 = numero1 ** numero2
        print("La primera potencia es: " + str(potencia1))
        print("La segunda potencia es: " + str(potencia2))
        print("La tercera potencia es: " + str(potencia3))
    case '+':
        # Operación suma:
        suma = numero1 + numero2
        print("La suma es " + str(suma))
    case '-':
        # Operación resta:
        resta = numero1 - numero2
        print("La resta es " + str(resta))
    case '*':
        # Operación multiplicación:
        multiplicacion = numero1 * numero2
        print("La multiplicación es " + str(multiplicacion))
    case '/':
        # Operación división:
        division = numero1 / numero2
        print("La división es " + str(division))
    case _ :
        print("Operación inválida")
