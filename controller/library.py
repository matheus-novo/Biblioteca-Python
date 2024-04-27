from models.connection.connection import DBConnectionHandler
from models.repository.book_repository import BookRepository

class Library:
    def __init__(self):
        connection_handler = DBConnectionHandler()
        connection_handler.connect_to_db()
        db_connection = connection_handler.get_db_connection()
        self.book_repository = BookRepository(db_connection)

    def add_book(self, book):
        return self.book_repository.insert_book(book)

    def create_book(self, titulo, autor, genero, edicao):
        return self.book_repository.create_book(titulo, autor, genero, edicao)

    def select_books(self):
        books = self.book_repository.list_books()
        for book in books:
            print("********")
            print(f"Titulo: {book['titulo']}")
            print(f"Autor: {book['autor']}")
            print(f"Genero: {book['genero']}")
            print(f"Edicao: {book['edicao']}")
            print("********")

    def select_by_gender(self, genero):
        books = self.book_repository.list_books(genero)
        for book in books:
            print("********")
            print(f"Titulo: {book['titulo']}")
            print(f"Autor: {book['autor']}")
            print(f"Genero: {book['genero']}")
            print(f"Edicao: {book['edicao']}")
            print("********")

    def delete_book(self, titulo):
        deleted = self.book_repository.delete_book(titulo)
        print(f"{deleted} registros deletados!")
