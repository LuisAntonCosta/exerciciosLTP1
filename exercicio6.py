biblioteca = []

while True:
    print("\nMenu:")
    print("1. Adicionar novo livro")
    print("2. Listar todos os livros")
    print("3. Buscar livro pelo título")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = input("Digite o ano de publicação: ")
        livro = [titulo, autor, ano]
        biblioteca.append(livro)
        print("Livro adicionado com sucesso!")
    
    elif opcao == "2":
        print("\nLista de Livros:")
        for livro in biblioteca:
            print(f"Título: {livro[0]}, Autor: {livro[1]}, Ano: {livro[2]}")
    
    elif opcao == "3":
        busca_titulo = input("Digite o título do livro que deseja buscar: ")
        encontrado = False
        for livro in biblioteca:
            if livro[0].lower() == busca_titulo.lower():
                print(f"Livro encontrado: Título: {livro[0]}, Autor: {livro[1]}, Ano: {livro[2]}")
                encontrado = True
                break
        if not encontrado:
            print("Livro não encontrado.")
    
    elif opcao == "4":
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida, tente novamente.")
    