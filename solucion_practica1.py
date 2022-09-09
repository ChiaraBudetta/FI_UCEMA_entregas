#ejercicio 1
#saludo = "hola me llamo chiara"
#print(len(saludo))

#ejercicio 2
#a = "miercoles"
#print(a[4:6].upper())

#ejercicio 3
#nombre_y_apellido = input("¿cual es tu nombre?: ")
#print("hola", nombre_y_apellido)

#ejercicio 4
# nombre = input("¿cual es tu nombre?: ")
# apellido1 = input("¿cual es tu apellido?: ")
# apellido2 = input("¿cual es tu apellido?: ")
# print(nombre.capitalize(), apellido1.capitalize(), apellido2.capitalize())

#ejercicio 5
# num1 = int(input("poner un numero: "))
# num2 = int(input("poner un numero: "))
# num3 = int(input("poner un numero: "))
# print((num1 + num2 + num3)/3)

#ejercicio 6
# tiempo = int(input("insertar minutos: "))
# horas = tiempo//60
# minutos = tiempo % 60 
# print(horas, "horas", minutos, "minutos")

# ejercicio 7
# sueldo_base = int(input("ingresar un sueldo: "))
# print(sueldo_base*0.4, "pesos de comision por 4 ventas")
# print(sueldo_base*1.4, "sueldo total del mes")

#ejercicio 8 
# respuestas_correctas = int(input("ingresar cantidad de respuestas correctas: "))
# respuestas_incorrectas = int(input("ingresar cantidad de respuestas incorrectas: "))
# if respuestas_correctas >= 1:
#     respuestas_correctas*4
# if respuestas_incorrectas >= 1:
#         respuestas_incorrectas*-1
# print((respuestas_correctas*4)+(respuestas_incorrectas*-1))

#ejercicio en grupo 
from numbers import Number


costo_total = int(input("valor de la casa: "))
porcentaje_desposito = costo_total*0,25
cantidad_ahorrada = int(input("cantidad ahorrada: ")) #0
g = 4/100
sueldo_anual = int(input("sueldo anual: "))
porcentaje_ahorrado = Number(input("que porcentaje de su sueldo quiere ahorar por mes: "))
sueldo_mensual = sueldo_anual/12
ahorro_esperado = sueldo_mensual * (porcentaje_ahorrado/100)

cant_meses = (porcentaje_desposito-(g/12))/ahorro_esperado
print("tomará %d meses en ahorrar el dinero necesario para pagar el depósito" %(cant_meses))









