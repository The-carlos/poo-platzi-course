class Libro:
    def __init__(self, titulo, autor, isbn, disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def __str__(self):
        return f"Libro (titulo={self.titulo}, autor={self.autor}, isbn={self.isbn}, disponible={self.disponible})"
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
        return f"{self.titulo} ha sido prestado."

    def devolver(self):
        self.disponible = True
        return f"{self.titulo} ha sido devuelto."

mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-3-16-148410-0", True)
otro_libro = Libro("El principito", "Antoine de Saint-Exupéry", "978-3-16-148410-1", False)

print(mi_libro.prestar())
print(mi_libro.devolver())

print(otro_libro.prestar())
print(otro_libro.devolver())

for libro in [mi_libro, otro_libro]:
    print(libro)