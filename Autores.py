
class autores:
    libro = []
    def __init__(self,codigo,apellidos,nombres,nacionalidad):
        self.apall = apellidos
        self.nom = nombres
        self.nacionalidad = nacionalidad
        self.cod = codigo
    def VerLibroPorAutor(self,codigo,libros):
        for LibrosAutor in libros:
            print(f"{libros}")
