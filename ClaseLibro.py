class Libro:
    def __init__(self, id, titulo, autor, idioma, categoria, editorial, copias):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.idioma = idioma
        self.categoria = categoria
        self.editorial = editorial
        self.copias = copias

    def __repr__(self):
        return str(self.__dict__)

'''
    def __str__(self):
        return f'ID: {self.id}\\n' \
            f'Titulo: {self.titulo}\\n' \
            f'Autor: {self.autor}\\n' \
            f'Idioma: {self.idioma}\\n' \
            f'Categoria: {self.categoria}\\n' \
            f'Editorial: {self.editorial}\\n' \
            f'Copias: {self.copias}\\n'
'''