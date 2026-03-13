class Libro:

    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def genero(self):
        return self._genero


    def __str__(self):
        return f"-> Titulo: {self.titulo} Autor: {self.autor} Genero: {self.genero}"