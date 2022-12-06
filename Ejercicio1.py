num1 = input("Ingresar primer Numero")
while not num1.isdigit():
    num1 = input("Digita Un Numero")
num1 = int(num1)
num2 = input("Ingresar segundo Numero")
while not num2.isdigit():
    num2 = input("Digita Un Numero")
num2 = int(num2)
selecOp = input(
    "Que operacion deseas realizar?,suma(+),resta(-),multiplicacion(*),division(/),divisonEntera(//),exponente(**))"
)
if selecOp == "+":
    suma = num1 + num2
    print("El resultado es:" + str(suma))
elif selecOp == "-":
    resta = num1 - num2
    print("El resultado es:" + str(resta))

elif selecOp == "*":
    multiplicacion = num1 * num2
    print("El resultado es" + str(multiplicacion))
elif selecOp == "/":
    division = num1 / num2
    print("El resultado es:" + str(division))
elif selecOp == "//":
    divisionEntera = num1 // num2
    print("El resultado es: " + str(divisionEntera))
elif selecOp == "**":
    exponente = num1**num2
    print("El resultado es: " + str(exponente))
