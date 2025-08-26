import os
import time
import cv2
from classes import *


# importando as bibliotecas necessárias para o funcionamento do sistema
# romance poesia conto cronica drama
#-----------------------------------------------------------------------------------------------------------#

def adicionar_livro():
    # Exibe as opções de categoria para o usuário
    print("Escolha a categoria do livro:")
    print("1 - Romance")
    print("2 - Poesia")
    print("3 - Conto")
    print("4 - Cronica")
    print("5 - Drama")
    categoria = input("Digite o número da categoria: ")

    # Solicita os dados do novo livro
    nome = input("Nome do livro: ")
    ano = int(input("Ano de publicação: "))
    autor = input("Autor: ")
    editora = input("Editora: ")

    # Adiciona o livro na categoria escolhida e atualiza o dicionário geral de livros
    if categoria == "1":
        novo_id = max(Romance_Dicionario.keys(), default=0) + 1
        # Cria o novo livro e adiciona ao dicionário da classe Romance e ao dicionário geral
        novo_livro = Romance(nome, ano, autor, editora)
        Romance_Dicionario[novo_id] = novo_livro
        livros[novo_id] = novo_livro
        print(f"Livro adicionado à classe Romance! ID: {novo_id}")
    elif categoria == "2":
    # Cria o novo livro e adiciona ao dicionário da classe Poesia e ao dicionário geral
        novo_id = max(Poesia_Dicionario.keys(), default=0) + 1
        novo_livro = Poesia(nome, ano, autor, editora)
        Poesia_Dicionario[novo_id] = novo_livro
        livros[novo_id] = novo_livro
        print(f"Livro adicionado à classe Poesia! ID: {novo_id}")
    elif categoria == "3":
        # Cria o novo livro e adiciona ao dicionário da classe Conto e ao dicionário geral
        novo_id = max(Conto_Dicionario.keys(), default=0) + 1
        novo_livro = Conto(nome, ano, autor, editora)
        Conto_Dicionario[novo_id] = novo_livro
        livros[novo_id] = novo_livro
        print(f"Livro adicionado à classe Conto! ID: {novo_id}")
    elif categoria == "4":
        # Cria o novo livro e adiciona ao dicionário da classe Cronica e ao dicionário geral
        novo_id = max(Cronica_Dicionario.keys(), default=0) + 1
        novo_livro = Cronica(nome, ano, autor, editora)
        Cronica_Dicionario[novo_id] = novo_livro
        livros[novo_id] = novo_livro
        print(f"Livro adicionado à classe Cronica! ID: {novo_id}")
    elif categoria == "5":
        # Cria o novo livro e adiciona ao dicionário da classe Drama e ao dicionário geral
        novo_id = max(Drama_Dicionario.keys(), default=0) + 1
        novo_livro = Drama(nome, ano, autor, editora)
        Drama_Dicionario[novo_id] = novo_livro
        livros[novo_id] = novo_livro
        print(f"Livro adicionado à classe Drama! ID: {novo_id}")
    else:
        print("Categoria inválida.")

#-----------------------------------------------------------------------------------------------------------#

def listar_livros():
    for id_livro, livro in livros.items():
        if isinstance(livro, Romance):
            tipo = "Romance"
            nome = livro.getNome()
            ano = livro.getAno()
            autor = livro.getAutor()
            editora = livro.getEditora()
        elif isinstance(livro, Poesia):
            tipo = "Poesia"
            nome = livro.getNome()
            ano = livro.getAno()
            autor = livro.getAutor()
            editora = livro.getEditora()
        elif isinstance(livro, Conto):
            tipo = "Conto"
            nome = livro.getNome()
            ano = livro.getAno()
            autor = livro.getAutor()
            editora = livro.getEditora()
        elif isinstance(livro, Cronica):
            tipo = "Cronica"
            nome = livro.getNome()
            ano = livro.getAno()
            autor = livro.getAutor()
            editora = livro.getEditora()
        elif isinstance(livro, Drama):
            tipo = "Drama"
            nome = livro.getNome()
            ano = livro.getAno()
            autor = livro.getAutor()
            editora = livro.getEditora()
        else:
            continue
        print(f"{id_livro}: {tipo} - {nome} ({ano}) | Autor: {autor} | Editora: {editora}")

#-----------------------------------------------------------------------------------------------------------#

def remover_livro():
    opcao = input("Deseja ver a lista de livros e seus IDs antes de remover? (s/n): ").strip().lower()
    if opcao == 's':
        for id_livro, livro in livros.items():
            if isinstance(livro, Romance):
                tipo = "Romance"
            elif isinstance(livro, Poesia):
                tipo = "Poesia"
            elif isinstance(livro, Conto):
                tipo = "Conto"
            elif isinstance(livro, Cronica):
                tipo = "Cronica"
            elif isinstance(livro, Drama):
                tipo = "Drama"
            else:
                tipo = "Desconhecido"
            print(f"ID: {id_livro} | Tipo: {tipo} | Nome: {livro.getNome()}")
    id_livro = int(input("Digite o ID do livro que deseja remover: "))
    if id_livro in livros:
        livro = livros[id_livro]
        # Remover do dicionário principal
        del livros[id_livro]
        # Remover do dicionário da categoria e garantir remoção da classe
        if isinstance(livro, Romance):
            Romance_Dicionario.pop(id_livro, None)
            del livro
        elif isinstance(livro, Poesia):
            Poesia_Dicionario.pop(id_livro, None)
            del livro
        elif isinstance(livro, Conto):
            Conto_Dicionario.pop(id_livro, None)
            del livro
        elif isinstance(livro, Cronica):
            Cronica_Dicionario.pop(id_livro, None)
            del livro
        elif isinstance(livro, Drama):
            Drama_Dicionario.pop(id_livro, None)
            del livro
        print("Livro removido com sucesso.")
    else:
        print("ID do livro não encontrado.")

#-----------------------------------------------------------------------------------------------------------#

def listar_autores_e_livros():
    # Coletar todos os autores únicos
    autores = set()
    for livro in livros.values():
        autores.add(livro.getAutor())
    autores = sorted(list(autores))

    # Exibir autores numerados
    print("Autores disponíveis:")
    for idx, autor in enumerate(autores, 1):
        print(f"{idx}. {autor}")

    # Solicitar escolha do usuário
    try:
        escolha = int(input("Escolha o número do autor: "))
        if 1 <= escolha <= len(autores):
            autor_escolhido = autores[escolha - 1]
            print(f"\nLivros de {autor_escolhido}:")
            for livro in livros.values():
                if livro.getAutor() == autor_escolhido:
                    # Tenta chamar o método de descrição correto
                    for metodo in ["mostrarinfo_romance", "mostrarinfo_poesia", "mostrarinfo_conto", "mostrarinfo_cronica", "mostrarinfo_drama"]:
                        if hasattr(livro, metodo):
                            print(getattr(livro, metodo)())
                            break
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida.")

# Exemplo de uso:
# listar_autores_e_livros()

#-----------------------------------------------------------------------------------------------------------#

def listar_generos():

    print("Escolha o gênero:")
    for num, (nome, _) in generos.items():
        print(f"{num} - {nome}")
    try:
        escolha = int(input("Digite o número do gênero desejado: "))
        if escolha in generos:
            nome_genero, dicionario = generos[escolha]
            print(f"\nLivros do gênero {nome_genero}:")
            for livro in dicionario.values():
                if hasattr(livro, f"mostrarinfo_{nome_genero.lower()}"):
                    print(getattr(livro, f"mostrarinfo_{nome_genero.lower()}")())
                else:
                    print(livro.getNome())
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida.")