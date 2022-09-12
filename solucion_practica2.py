# **Práctica de introducción a Python - Parte 2**

##### **Ejercicio 1** Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.

#cadena = input("insertar una frase: ")

# if (cadena[0].isupper()):
#     print("la primera letra es mayuscula")
# else:
#     print("la primera letra es minuscula")



##### **Ejercicio 2** Escribí un programa que pida un número y diga si es positivo, negativo o 0 y además 
# informe si es par o impar (el 0 es un número par).

# numero = int(input("ingrese un numero: "))
# if numero == 0:
#     print("el numero ingresado es 0")
# elif numero > 0:
#     print("el numero ingrsado es positivo")
# else:
#     print("el numero ingresado es negativo")

# if numero % 2 == 0:
#     print("el numero ingresado es par")
# else:
#     print("el numero ingresado es impar")



##### **Ejercicio 3** Escribí un programa que dado un número del 1 al 6, ingresado por teclado, muestre cuál es el número que está en 
# la cara opuesta de un dado. Si el número es menor a 1 y mayor a 6 se debe mostrar un mensaje indicando que es incorrecto el número ingresado.

# numero = int(input("ingresar un numero del 1 al 6 inclusive: "))
# if numero == 1:
#     print("el numero que esta en la cara opuesta del dado es 6")
# elif numero == 2:
#     print("el numero que esta en la cara opuesta del dado es 5")
# elif numero == 3:
#     print("el numero que esta en la cara opuesta del dado es 4")
# elif numero == 4:
#     print("el numero que esta en la cara opuesta del dado es 3")
# elif numero == 5:
#     print("el numero que esta en la cara opuesta del dado es 2")
# elif numero == 6:
#     print("el numero que esta en la cara opuesta del dado es 1")
# else:
#     print("se ingreso un valor incorrecto")



##### **Ejercicio 4** Una compañía de transporte internacional tiene servicio en algunos países de América del Sur, América Central, 
# América del Norte, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido, 
# tal como se muestra en la tabla:
# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. 
# Realizá un programa para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.


# zona = int(input("ingrese a que zona le gustaria enviar (1-4): "))
# peso = int(input("ingrese cual es el peso del paquete que quiere enviar (en gramos): "))
# zona1 = peso*10
# zona2 = peso*15
# zona3 = peso*18
# zona4 = peso*24
# zona5 = peso*30

# if zona == 1 and 5000 >= peso:
#     print(f"el costo es de {zona1} dolares")
# elif zona == 2 and 5000 >= peso:
#     print(f"el costo es de {zona2} dolares")
# elif zona == 3 and 5000 >= peso:
#     print(f"el costo es de {zona3} dolares")
# elif zona == 4 and 5000 >= peso:
#     print(f"el costo es de {zona4} dolares")
# elif zona == 5 and 5000 >= peso:
#     print(f"el costo es de {zona5} dolares")
# else:
#     print("el peso del paquete es superior a lo aceptado")



##### **Ejercicio 5** Creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente. 
# Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.

# dia_de_la_semana = int(input("ingrese el numero de dia de la semana (1-7): "))

# if dia_de_la_semana == 1:
#     print("Lunes")
# elif dia_de_la_semana == 2:
#     print("Martes")
# elif dia_de_la_semana == 3:
#     print("Miercoles")
# elif dia_de_la_semana == 4:
#     print("Jueves")
# elif dia_de_la_semana == 5:
#     print("Viernes")
# elif dia_de_la_semana == 6:
#     print("Sabado")
# elif dia_de_la_semana == 7:
#     print("Domingo")
# else: 
#     print("el numero es incorrecto")



### Listas



##### **Ejercicio 6** Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copiá los elementos de la lista 
# en otra lista pero en orden inverso, imprimí los elementos de esta última lista.

# lista1 = []
# for i in range(5):
#     lista1.append(input("dame una palabra: "))

# lista2 = list(lista1)

# lista2.reverse()

# for elemento in lista2:
#     print(elemento)


##### **Ejercicio 7** Creá un programa que declare una lista y la vaya llenando de números leídos por teclado hasta que se introduzca 
# un número negativo. Una vez hecho esto se deben imprimir los elementos de la lista.

# lista = []
# n = int(input("introducí un numero: "))
# while n>=0:
#     lista.append(n)
#     n = int(input("introducí un numero: "))
# for n in lista:
#     print (n,"", end="")



##### **Ejercicio 8** Realizá un programa que declare tres listas _lista1_, _lista2_ y _lista3_, donde las dos primeras listas deben 
# tener cinco enteros cada una, ingresados por teclado y asigne para cada elemento de la _lista3_ la suma de los elementos de la _lista1_ y la _lista2_ 
# (es decir, el primer elemento de la _lista3_ tiene que ser la suma del primer elemento de la _lista1_ y el primero de la _lista2_)

# n1_l1=input("Ingresá el primer número de la primer lista: ")
# n2_l1=input("Ingresá el segundo número de la primer lista: ")
# n3_l1=input("Ingresá el tercer número de la primer lista: ")
# n4_l1=input("Ingresá el cuarto número de la primer lista: ")
# n5_l1=input("Ingresá el quinto número de la primer lista: ")

# n1_l2=input("Ingresá el primer número de la segunda lista: ")
# n2_l2=input("Ingresá el segundo número de la segunda lista: ")
# n3_l2=input("Ingresá el tercer número de la segunda lista: ")
# n4_l2=input("Ingresá el cuarto número de la segunda lista: ")
# n5_l2=input("Ingresá el quinto número de la segunda lista: ")

# lista1=[]
# lista2=[]
# lista3=[]

# list.append(lista1,int(n1_l1))
# list.append(lista1,int(n2_l1))
# list.append(lista1,int(n3_l1))
# list.append(lista1,int(n4_l1))
# list.append(lista1,int(n5_l1))

# list.append(lista2,int(n1_l2))
# list.append(lista2,int(n2_l2))
# list.append(lista2,int(n3_l2))
# list.append(lista2,int(n4_l2))
# list.append(lista2,int(n5_l2))

# n1_l3=lista1[0]+lista2[0]
# n2_l3=lista1[1]+lista2[1]
# n3_l3=lista1[2]+lista2[2]
# n4_l3=lista1[3]+lista2[3]
# n5_l3=lista1[4]+lista2[4]

# list.append(lista3,int(n1_l3))
# list.append(lista3,int(n2_l3))
# list.append(lista3,int(n3_l3))
# list.append(lista3,int(n4_l3))
# list.append(lista3,int(n5_l3))

# print("lista 1: ", lista1)
# print("lista 2: ", lista2)
# print("lista 3: ", lista3)



##### **Ejercicio 9** Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. Se debe introducir el nombre y la edad 
# de cada alumno por teclado. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (__*__). 
# Al finalizar se deben mostrar los siguientes datos:
# * La edad máxima de todos los alumnos.
# * Los alumnos que tengan la edad máxima


# nombres = []
# edades = []

# nom=input("ingrese un nombre: ")

# if nom != "*":
#     nombres.append(nom)
#     edad=int(input("ingrese su edad: "))
#     edades.append(edad)
# else:
#     pass

# while nom!="*":
#     nom= input("ingrese un nombre: ")
#     if nom!="*":
#         nombres.append(nom)
#         edad = int(input("ingrese su edad: "))
#         edades.append(edad)

# edad_max = max(edades)
# nombre_max = nombres[edad_max]

# for i in range(len(edades)):
#     if edades[i] == edad_max:
#         print(nombres[i])

# for i in range(len(nombres)):
#     if nombres[i] == nombre_max:
#         print(nombres[i])



### Diccionarios

##### **Ejercicio 10** Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena 
# (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).

# caracteres={}
# cadena=input("Escribí algo ")

# for caracter in cadena:
#     if caracter in caracteres:
#         caracteres[caracter]+=1
#     else:
#         caracteres[caracter]=1

# for clave,valor in caracteres.items():
#     print(clave,valor)



##### **Ejercicio 11** Modificá el programa anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.

# alfabeto="abcdefghijklmnñopqrstuvwxyz"
# caracteres2={}
# for letra in alfabeto+alfabeto.upper():
#     caracteres2[letra]=0
# cadena2=input("Escribí algo ")
# for caracter in cadena2:
#     if caracter.lower() in alfabeto:
#         caracteres2[caracter]+=1
# for clave,valor in caracteres2.items():
#     print(clave,valor)



##### **Ejercicio 12** Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido.
# Cada alumno puede tener distinta cantidad de notas. Guardá la información en un diccionario cuya claves serán los nombres de los alumnos y 
# los valores serán listas con las notas de cada alumno.
# El programa tiene que pedir el número de alumnos que se va a introducir, luego su nombre y sus notas hasta que introduzcamos un número negativo. 
# Al final el programa tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno 
# que ya existe el programa tiene que dar un error.

# datos_alumnos={}
# cantidad_alumnos=input("Ingrese el número de alumnos que va a introducir ")
# preguntar_nombre=""
# preguntar_nota=0
# for alumno in range(int(cantidad_alumnos)):
#     lista_notas=[]
#     preguntar_nombre=input("Nombre: ")
#     preguntar_nota=int(input("Nota: "))
#     if preguntar_nombre not in datos_alumnos.keys():
#         while preguntar_nota>0:
#             lista_notas.append(preguntar_nota)
#             datos_alumnos[preguntar_nombre]=lista_notas
#             preguntar_nota=int(input("Nota: "))
#             print(lista_notas)
#     else:
#         print("Alumno ya cargado")
# for alumno in datos_alumnos.keys():
#     promedio=sum(datos_alumnos[alumno])/len(datos_alumnos[alumno])
#     print("El promedio de "+alumno+" es "+str(promedio))



### Funciones

##### **Ejercicio 13** Creá un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro creando la función **esMultiplo**.

# def esMultiplo (num1, num2):
#     if num1%num2 == 0:
#         return True
#     else:
#         return False

# num1 = int(input("insertar un numero entero: "))
# num2 = int(input("insertar un numero entero: "))


# if esMultiplo (num1, num2):
#     print (f"{num1} es multiplo de {num2}")
# else:
#     print (f"{num1} no es multiplo de {num2}")

# if esMultiplo (num2, num1):
#     print (f"{num2} es multiplo de {num1}")
# else:
#     print (f"{num2} no es multiplo de {num1}")



##### **Ejercicio 14** Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
# Escribí un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. 
# El programa tiene que pedir el número de días que se van a introducir.

# def temperatura_media(temperatura, temperatura1):
#     return (temperatura+temperatura1)/2

# dias= int(input("ingrese cantidad de días: "))
# num= 0

# while num< dias:
#     num +=1
#     max= float(input("ingrese temperatura max del dia: "))
#     min= float(input("ingrese la temperatura min del dia: "))
#     print(temperatura_media(max,min))



##### **Ejercicio 15**

# socios = {}
# socios["1"] = ["Florencia Ocampo","14/09/2001","cuota al día"]
# socios["2"] = ["David Estévez","14/09/2001","cuota al día"]
# socios["3"] = ["Sofía Cáceres","14/09/2001","cuota al día"]

# numero_socio = int(input("ingresar el numero de socio: "))
# while numero_socio > 0:
#       nombre_y_apellido = input("ingresar el nombre y el apellido: ")
#       fecha_ingreso = input("ingresar la fecha de ingreso con el siguiente formato = dd/mm/aaaa : ")
#       estado_cuota = input("ingresar 'cuota al dia' o 'cuota atrasada': ")
#       socios[numero_socio] = [nombre_y_apellido, fecha_ingreso , estado_cuota ]
#       numero_socio = int(input("ingresar el numero de socio: "))

# print(socios.values())

# print("El club tiene", len(socios.keys()),"socios")

# def pago_cuotas(nro):
#       if socios[nro][2] == "cuota al dia":
#             return print("El socio",nro, "no tiene deudas")
#       else:
#             return print("El socio", nro, "tiene deudas")

# socios["444"] = ["Mario Fernandez", "21/10/2017","cuota al dia" ]
# socios["555"] = ["Juan Perez", "21/10/2017", "cuota al dia"]
# socios["666"] = ["Maria Martinez", "21/10/2017", "cuota al dia"]

# def cambiar_fecha (fecha_nueva,fecha_mal):
#       for a in socios.keys():
#             if socios[a][1] == fecha_mal:
#                   socios[a][1] = fecha_nueva
#             else:
#                    socios[a][1] 
          
# cambiar_fecha("22/10/2017","21/10/2017")
# print(socios.values())

# def dar_de_baja (nombre):
#       for a in socios.keys():
#             if socios [a][0] == nombre:
#                   del socios[a]

# dar_de_baja ("Florencia Ocampo")

# print("Los datos de los socios son:",socios.values())

