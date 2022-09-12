#EJERCICIO 1
# path = open ('/Users/chiara/Documents/GitHub/Fundamentos/FI_UCEMA_entregas/solucion_manipulación_de_archivos.py')
# contador = 0
# def texto (archivo):
#     with open (archivo, 'r') as file:
#         for i in file:
#             if i[0] !="p":
#                 contador +=1

# print("La cantidad de líneas que no empiezan con P son:", contador)

# texto = (path)


#EJERCICIO 2
# path = r'/Users/chiara/Documents/GitHub/Fundamentos/FI_UCEMA_entregas/solucion_manipulación_de_archivos.py'
# def imprimir_n_primeras_lineas(n):
#     with open(path,"r") as file:
#         lineas= file.readlines()
#         for linea in lineas:
#             if lineas.index(linea)<=(n-1):
#                 print (linea)


#EJERCICIO 3
# path = r'/Users/chiara/Documents/GitHub/Fundamentos/FI_UCEMA_entregas/solucion_manipulación_de_archivos.py'
# lista = []
# with open (path,'r') as file:
#     for i in range(6):
#         lista.append(file.readline(i))
# print(len(lista))
# def imprimir_ul(n):
#     print(lista[(6-n):])

# imprimir_ul(2)


#EJERCICIO 4
# path = r'/Users/chiara/Documents/GitHub/Fundamentos/FI_UCEMA_entregas/solucion_manipulación_de_archivos.py'
# with open (path,'r') as file:
#     texto = file.read()
#     palabras = texto.split()
#     print(len(palabras))
#     print(palabras)


#EJERCICIO 5
# import re
# import shutil
# route = r'/Users/chiara/Documents/GitHub/Fundamentos/FI_UCEMA_entregas/solucion_manipulación_de_archivos.py'
# newRoute = r'/Users/chiara/Downloads/Fundamentos_de_informatica-master/Python_intro/myscript.py'
# with open (route,"r") as txt:
#     data = txt.read()
# with open (newRoute,"w") as txt2:
#     shutil.copyfile(route,newRoute)
# with open (newRoute,"r+") as copy:
#     copy.write(re.sub("s", "s\n",copy.read()))

#EJERCICIO 6
# import re
# import shutil
# route = r'/Users/chiara/Documents/GitHub/Fundamentos/FI_UCEMA_entregas/solucion_manipulación_de_archivos.py'
# newRoute = r'/Users/chiara/Downloads/Fundamentos_de_informatica-master/Python_intro/myscript.py'
# with open(route,"r") as txt:
#     originalFile = txt.read()
# with open(newRoute,"w") as newFile:
#     shutil.copyfile(route,newRoute)
# with open(newRoute,"r+") as alteredFile:
#     for line in alteredFile:
#         line = line.replace("\n", "")


#EJERCICIO 7
# import re
# route = r'/Users/chiara/Documents/GitHub/Fundamentos/FI_UCEMA_entregas/solucion_manipulación_de_archivos.py'
# with open(route, 'r') as infile:
#     txt = infile.read().split()
#     max_len = len(max(txt, key=len))
#     longest = [word for word in txt if len(word) == max_len]
#     longest = re.split("[^a-zA-Z\d]+", str(longest))
#     longest = ','.join([ i for i in longest if len(i) > 0 ])
#     print(longest)
#     print(len(longest))


#EJERCICIO 8
# path = r'/Users/chiara/Documents/GitHub/Fundamentos/FI_UCEMA_entregas/solucion_manipulación_de_archivos.py'
# path2 = r'/Users/chiara/Downloads/Fundamentos_de_informatica-master/Python_intro/myscript.py'
# path3 = r'/Users/chiara/Downloads/Fundamentos_de_informatica-master/Python_intro/my_script.py'
# def combinar_archivos(path, path2, path3):
#     with open(path, 'r') as file, open(path2, 'r') as file2, open(path3, 'w') as file3:
#         for l1, l2 in zip(file, file2):
#             file3.write(l1)
#             file3.write('\n')
#             file3.write(l2)
      
# combinar_archivos(path, path2, path3)

#EJERCICIO 9
# import re
# import string
# frequency = {}
# txt = open(r'/Users/chiara/Documents/GitHub/Fundamentos/FI_UCEMA_entregas/solucion_manipulación_de_archivos.py', "r")

# data = txt.read()
# w = data.split()
# wcount = len(w)

# match_pattern = re.findall(r'\b[a-z]{3,15}\b', data.lower())


# for word in match_pattern:
#   count = frequency.get(word,0)
#   frequency[word] = count + 1
   
# frequency_list = frequency.keys()
 
# for words in frequency_list:
#   fr = frequency[words]/wcount
#   print(words, fr)



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
