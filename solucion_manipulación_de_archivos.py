#EJERCICIO 1
# path = ('/Users/chiara/Documents/GitHub/Fundamentos/FI_UCEMA_entregas/solucion_manipulación_de_archivos.py')
# contador = 0
# def texto (archivo):
#     with open (archivo, 'r') as file:
#         for i in file:
#             if i[0] !="p":
#                 contador +=1

# print("La cantidad de líneas que no empiezan con P son:", contador)

# texto = (path)


#EJERCICIO 2
# path = open (r'/Users/chiara/Documents/GitHub/Fundamentos/FI_UCEMA_entregas/solucion_manipulación_de_archivos.py')
# def imprimir_n_primeras_lineas(n):
#     with open(path,"r") as file:
#         lineas= file.readlines()
#         for linea in lineas:
#             if lineas.index(linea)<=(n-1):
#                 print (linea)



#EJERCICIO 10
# path = open (r'/Users/chiara/Documents/GitHub/Fundamentos/FI_UCEMA_entregas/solucion_manipulación_de_archivos.py')
# import os,glob

# def unir_txt (carpeta1, nombre):
#     os.chdir(carpeta1)
#     textos = glob.glob("*.txt")
#     with open ("Resultado/" + nombre, "a") as salida:
#         for archivo in textos:
#             with open(archivo, "r") as texto:
#                 salida.write(texto.read())
