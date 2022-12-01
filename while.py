edad=input("Cuantos años Tienes")
while not edad.isdigit():
    edad=input("Digita Un Numero")
edad = int(edad)
if edad < 25:
    print("Eres Un Estudiante")
if edad > 25:
        print("Eres un Profesor")
if edad > 65:
    print("Eres un Master")     