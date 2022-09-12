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

# def palabra_encontrada(lista1, string):
#     lista1 = ["fundamentos", "expresiones", "regulares"]
#     if re.search (lista1(), string):
#         return "se encuentra el elemento en la frase"
#     else:
#         return "no se encuentra el elemento en la frase"

# print(palabra_encontrada("fundamentos", "esto es una actividad de fundamentos de informatica"))

#EJERCICIO 7


