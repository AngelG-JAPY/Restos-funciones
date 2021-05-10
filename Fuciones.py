import math as m

#Ejercicio 1
def saludo(nombre):
    return f"¡Hola {nombre}!"

#Ejercicio 2
def factorial(numero):
    factorial_numero = m.factorial(numero)
    return f"El factorial de {numero} es: {factorial_numero}"

#Ejercicio 3
def aumento_iva(precio_base, iva = 19):
    factura = precio_base * (iva/100)
    return f"La factura con iva del {iva}, es {factura}"

#Ejercicio 4
def area_circulo(radio, altura):
    area_del_circulo = round(m.pi,2) * radio**2
    
    def volumen_cilindro():
        volumen = area_del_circulo * altura
        return volumen

    volumen = volumen_cilindro()
    return f"El area del circulo es {area_del_circulo} y el volumen del cilindro que se forma es {volumen}"
    
#Ejercicio 5
def suma_hasta_n(n):
    suma = n * (n + 1) / 2
    return f"La suma desde 1 hasta {n} es 0{int(suma)}"    

#Ejercicio 6
def indice_masa_corporal(peso, altura):
    imc = peso / altura**2
    return f"Tu índice de masa corporal es {round(imc , 2)}"

#Ejercicio 7
def peso_total(cantidad_payasos, cantidad_muñecas):
    peso_por_payasos = 112 * cantidad_payasos
    peso_por_muñecas = 75 * cantidad_muñecas
    peso_final = peso_por_payasos + peso_por_muñecas
    return peso_final

#Ejercicio 8
def descuento_por_barra_de_pan(cantidad_pan):
    costo_sin_descuento = cantidad_pan * 3.49
    descuento = costo_sin_descuento * 0.6
    costo_total = round(costo_sin_descuento - descuento , 1)
    return f"El precio habitual de una barra de pan es 3.49€. El descuento que se le hace por no ser del día es del 60%\ny el coste final total es {costo_total}€"

#Ejercicio 9
def cuenta_ahorro(dinero_depositado):
    ahorros_primer_año = dinero_depositado + (dinero_depositado * 0.05)
    ahorros_segundo_año = ahorros_primer_año + (ahorros_primer_año * 0.05)
    ahorros_tercer_año = ahorros_segundo_año + (ahorros_segundo_año * 0.05)
    return f"Ahorros primer año {ahorros_primer_año}\nAhorros segundo año {ahorros_segundo_año}\nAhorros tercer año {ahorros_tercer_año}"




#Ejercicio 10
def equivalencia_segundos(segundos):
    minutos = segundos / 60
    horas = minutos / 60
    dias = horas / 24
    return f"{round(dias)} días, {round(horas%24)} horas, {round(minutos%60)} minutos, {round(segundos%60)} segundos"