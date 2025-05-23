from autrores import autores
from milibros import Libros
import time
import os
autore = []
Opciones = ""
def verAutores():
    for MisAutores in autore:
        print(f"{MisAutores.cod}\t{MisAutores.apall}\t{MisAutores.nom}")

def AsignaLibro(codigo,libro):
    for MisAutores in autore:
        if MisAutores.cod == codigo:
            MisAutores.libro.append(libro)

def verLibrosAutor(codigo,libros):
    for MisAutores in autore:
        if MisAutores.cod == codigo:
            print(f"{libros}") 
            

while(Opciones!= 5):
    time.sleep(2)
    os.system("cls")
    print("1.Agregar Autores")
    print("2. Ver Autores")
    print("3.Agregar libro")
    print("4.ver libros por autor")
    print("5.Salir")
    Opciones = int(input("Ingrese la opcion que desea: "))
    if Opciones == 1:
        codigo = int(input("Ingrese codigo del autor: "))
        apellidos = input("Ingrese apellidos del autor: ")
        nombre = input("Ingrese el nombre :")
        nacionalidad = input("Ingrese la nacionalidad: ")
        autor1 = autores(codigo,apellidos,nombre,nacionalidad)
        autore.append(autor1)
    elif Opciones == 2:
        verAutores()
    elif Opciones == 3:
        titulo = input("Ingrese el titulo del libro: ")
        tipo = input("Coloque el tipo de libro: ")
        libro1 = Libros(titulo,tipo)
        verAutores()
        Codigodelautor = int(input("Ingrese al codigo del autor que le corresponde el libro: "))
        AsignaLibro(Codigodelautor,libro1)
    elif Opciones == 4:
        Codigodelautor1 = int(input("ingrese el codigo del autor"))
        verLibrosAutor(Codigodelautor1,libro1)
