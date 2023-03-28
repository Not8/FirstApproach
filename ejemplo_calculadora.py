def operaciones(numero1, operacion, i: bool):
    match operacion:
        case "+":
            numero2 = int(input("Ingrese el segundo numero: "))
            numero1 += numero2
            print("Resultado: ", numero1)
        case "-":
            numero2 = int(input("Ingrese el segundo numero: "))
            numero1 -= numero2
            print("Resultado: ", numero1)
        case "*":
            numero2 = int(input("Ingrese el segundo numero: "))
            numero1 *= numero2
            print("Resultado: ", numero1)
        case "/":
            numero2 = int(input("Ingrese el segundo numero: "))
            numero1 /= numero2
            print("Resultado: ", numero1)
        case _:
            print("Operacion invalida, saliendo del programa")
            i = False


def calculadora() -> None:
    i = True
    numero1 = int(input("Ingrese el primer numero: "))
    while (numero1 is None):
        numero1 = int(input("Ingrese el primer numero: "))
    while i:
        operacion = (input("Ingrese la operacion: "))
        operaciones(numero1, operacion, i)


calculadora()
