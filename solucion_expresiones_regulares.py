# #EJERCICIO 1
# import re

# def caracteres_permitidos(string):
#     return bool(re.search("[a-zA-Z0-9.]", string))
# """"
# def caracteres_permitidos(string):
#     charRe = re. compile("[a-zA-Z0-9.]")
#     string = charRe.search(string)
#     return bool(string)
#         return bool(charRe.search(string))
# """

# print("El string", "ABCDEFabcdef123450", "tiene caracteres permitidos?")
# print(caracteres_permitidos("ABCDEFabcdef123450"))
# print("El string", "*&%@#!}{", "tiene caracteres permitidos?")
# print(caracteres_permitidos("*&%@#!}{"))

# #EJERCICIO 2
# import re

# def caracteres_permitidos(string):
#     return not bool(re.search("[^a-zA-Z0-9]", string))

# print("El string", "ABCDEFabcdef123450", "tiene todos los caracteres permitidos?")
# print(caracteres_permitidos("ABCDEFabcdef123450"))
# print("El string", "ABCDEFabcdef123450!", "tiene todos los caracteres permitidos?")
# print(caracteres_permitidos("ABCDEFabcdef123450!"))

# #EJERCICIO 3
# #A)
# import re

# def encontrar_patron(string):
#     patron = "he*"
#     if re.search(patron, string) is not None:
#         return "Se encontró el patrón"
#     else:
#         return "No se encontró el patrón"

# print(encontrar_patron("a"))

# #B)
# import re

# def encontrar_patron(string):
#     patron = "he+"
#     if re.search(patron, string) is not None:
#         return "Se encontro el patron"
#     else:
#         return "No se encontro el patron"

# print(encontrar_patron("a"))

# #C)
# import re

# def encontrar_patron(string):
#     patron = "he{2,3}"
#     if re.search(patron, string) is not None:
#         return "Se encontró el patrón"
#     else:
#         return "No se encontró el patrón"

# print(encontrar_patron("he"))
# print(encontrar_patron("hheeeeey"))

# #EJERCICIO 4
# import re

# def palabras_unidas(string):
#     patron = "^[a-z]+_[a-z]+$"
#     if re.search(patron, string) is not None:
#         return "Patrón encontrado"
#     else:
#         return "Patrón no encontrado"

# print (palabras_unidas("aab_bagdsf"))
# print(palabras_unidas("aAa_bagdsf"))
# print(palabras_unidas("aab_b6gdsf"))

# #EJERCICIO 5
# import re

# def numero_especifico(numero, string):
#     if re.match(str(numero), string) is not None:
#         return "Empieza con el número"
#     else:
#         return "No empieza con ese número"

# print(numero_especifico(5, "5sdgf"))
# print(numero_especifico(5, "a5sdgf"))
# print(numero_especifico(65, "5sdgf"))

#EJERCICIO 6
# import re
# lista = ["practica", "fundamentos", "informatica", "ucema"]
# frase = "esto es una practica de fundamentos de informatica"

# for i in lista:
#     patron = i
#     if re.search(patron, frase) is not None:
#         print("la palabra se encuentra en la lista dada")
#     else:
#         print("la palabra no se encuentra en la lista dada")

#EJERCICIO 8
# import re
# numeros = "estamos en el mes 9 del año 2022"
# x = re.split("\D+", numeros)
# for a in x:
#     print(a)

#EJERCICIO 9
# import re
# texto = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
# x = re.split("Hoy estuvimos trabajando con re (.*)\ en python ", texto)
# for a in x:
    # print(a)

#EJERCICIO 10
# import re
# texto = "esto es una @ practica de fundamentos de informatica & de la ucema"
# palabra_a_buscar = re.findall("@(.*)&",texto)
# print(palabra_a_buscar)

# for i in palabra_a_buscar:
#     print(texto.index(i))

#EJERCICIO 11
# import re

# lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
# def letrap (lista):
#   for elemento in lista:
#       resultado = re.match("(P\w*)\W(P\w*)", elemento)
#       if resultado is not None:
#           print (resultado.group())

# print(letrap(lista))

#EJERCICIO 12
# import re
# texto= "esto es: una practica de fundamentos_de_informatica de la ucema"
# patron1=" "
# patron2="_"
# patron3=":"
# texto1=re.sub(patron1,"|",texto)
# texto2=re.sub(patron2,"|",texto1)
# texto3=re.sub(patron3,"|",texto2)
# print(texto3)

#EJERCICIO 13
# import re
# texto = "esto es: una practica de fundamentos_de_informatica de la ucema"
# x = re.sub("^es","-",texto)
# print(x)

#EJERCICIO 14
# import re
# texto = "esto es una pract   ica de fundamentos de informat ica de la ucema"
# patron = ("\s")
# print(re.sub(patron, ";", texto)) 

#EJERCICIO 15
# import re
# mail = input("Ingrese su direccion de mail: ")
# patron = "(\W|^)[\w.\-][^(()<>@,;:%]*((@)((gmail|hotmail|yahoo)\.com){1})(\W|$)"

# if re.search(patron, mail) is not None:
#     print("La direccion de mail es valida")
# else:
#     print("La direccion de mail no es valida")



