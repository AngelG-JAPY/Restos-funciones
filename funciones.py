def mayor_numeros(num_1, num_2):
    resultado = max(num_1,num_2)
    return f"El mayor entre los números {num_1} y {num_2} es: {resultado}"

def promedio_numeros(num_1, num_2, num_3):
    promedio = (num_1+num_2+num_3)/3
    return f"El promedio de los números {num_1}, {num_2}, {num_3} es {round(promedio,2)}"

def factorial(num_1):

    if(num_1 == 0):
        return 1
    else:
        return num_1 * factorial(num_1-1)

