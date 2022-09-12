#ejercicio 1
lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabón", "alcohol"]
try:
    lista_super + "arroz"
except:
    print("no puedo agregar arroz")

#el uso no es correcto porque pueden ocurrir mas errores que solo no poder agregar "arroz", por lo tanto en except 
# imprimiría "ha ocurrido un error"

#ejercicio 2


def division_de_elementos (lista1, numero):
    lista1= [1-100000]
    numero= [int(input("dame un numero: "))]
    dividir= int(lista1)/numero
    