import random

NumeroIntentos = 0
numeroMin = 1
numeroMax = 100
print("Hola Bienvenido al Juego de Adivinar un Numero¡ ¿Cual es tu Nombre?")
usuario = input()

print(
    "okey, "
    + usuario
    + " Tienes que adivinar el Numero que estoy Pensando, entre un rango de "
    + str(numeroMin)
    + " a "
    + str(numeroMax)
)

numeroAletorioSistema = random.randint(numeroMin, numeroMax)
while NumeroIntentos < 6:
    print("Adivina: ")
    intentos = int(input())

    NumeroIntentos = NumeroIntentos + 1

    if intentos < numeroAletorioSistema:
        print("El numero ingresado es muy Bajo, Intenta de Nuevo")
    if intentos > numeroAletorioSistema:
        print("El numero ingresado es muy Alto, Intenta de Nuevo")
    if intentos == numeroAletorioSistema:
        break


if intentos == numeroAletorioSistema:
    print(
        "Buen trabajo "
        + usuario
        + " has logrado adivinar el Numero que estaba Pensando en "
        + str(NumeroIntentos)
        + " Intentos"
    )
elif intentos != numeroAletorioSistema:
    print(
        "Lo siento te has quedado sin Intentos, El numero adivinar era: "
        + str(numeroAletorioSistema)
    )
