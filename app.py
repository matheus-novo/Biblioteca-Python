from controller.library import Library

biblioteca = Library()


while True:
    print("-----------------")
    print("BEM VINDO A BIBLIOTECA")
    print("1 - Criar Livro")
    print("2 - Deletar Livro")
    print("3 - Listar Livros")
    print("4 - Buscar pelo Genero")
    print("5 - Sair")
    print("-----------------")

    opt = int(input("Digite a opção: "))

    match opt:
        case 1:
            titulo = input("Digite o titulo: ")
            autor = input("Digite o autor: ")
            genero = input("Digite o genero: ")
            edicao = int(input("Digite a edicao: "))
            biblioteca.create_book(titulo, autor, genero, edicao)
        case 2:
            titulo = input("Digite o titulo: ")
            biblioteca.delete_book(titulo)
        case 3:
            biblioteca.select_books()
        case 4:
            genero = input("Digite o genero: ")
            biblioteca.select_by_gender(genero)
        case 5:
            break




