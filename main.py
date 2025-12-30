class Libro:
    def __init__(self, titulo, autor, isbn, disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-3-16-148410-0", True)
otro_libro = Libro("El principito", "Antoine de Saint-Exupéry", "978-3-16-148410-1", False)

for libro in [mi_libro, otro_libro]:
    print(f"Título: {libro.titulo}")
    print(f"Autor: {libro.autor}")
    print(f"ISBN: {libro.isbn}")
    print(f"Disponible: {'Sí' if libro.disponible else 'No'}")