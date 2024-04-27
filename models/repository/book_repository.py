class BookRepository:
    def __init__(self, db_connection):
        self._db_connection = db_connection
        self._collection = self._db_connection['books']

    def create_book(self, titulo, autor, genero, edicao):
        book = {"titulo": titulo, "genero": genero, "autor": autor, "edicao": edicao}
        return self.insert_book(book)
    def insert_book(self, book_document):
        return self._collection.insert_one(book_document)

    def list_books(self, genero = None):
        if(genero == None):
            books = self._collection.find({}, {'_id': 0})
        else:
            books = self._collection.find({"genero": genero}, {'_id': 0})
        return list(books)

    def delete_book(self, titulo):
        data = self._collection.delete_one({"titulo":titulo})
        return data.deleted_count