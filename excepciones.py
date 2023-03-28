def div(num1, num2):
    if num2 == 0:
        raise TypeError("Wasd")
    return num1/num2


try:
    val = div(1, 0)
    print(val)
except Exception as excepcion:
    print("error de operacion", excepcion)
finally:
    print("Wasd")
