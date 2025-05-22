class Libros:
    def __init__(self,titulo,tipo):
        self.titulo = titulo
        self.tip = tipo
    def __str__(self):
        return f"{self.titulo} {self.tipo}"