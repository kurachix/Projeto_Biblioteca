import os
import time
import cv2
from classes import *

livros = {}
# importando as bibliotecas necessárias para o funcionamento do sistema
# romance poesia conto cronica drama

def registro(livros):
    while True:

        os.system("cls")

        print("Área de acesso restrito!\nRealize o seu login de admin!!".center(50))

        usuario = input("\nUsuário:\n--> ")
        senha = input("Senha:\n--> ")

        if usuario == "admin" and senha == "admin123":
            print("\nLogin realizado com sucesso!")
            time.sleep(2)
            
        os.system("cls")
        print(50 * "-")
        print("Cadastro de livros".center(50))
        print(50 * '-')


        print("\nComece escolhendo o tipo do livro que deseja cadastrar:")
        print("1 - Romance")
        print("2 - Poesia")
        print("3 - Conto")
        print("4 - Crônica")
        print("5 - Drama")
        print("6 - Voltar ao menu principal")
       
        tipo_livro = input("\nDigite o tipo do livro:")

        if tipo_livro == "1":
            os.system("cls")

            nome = input("Nome do livro:\n-->")

            os.system("cls")

            ano = input("Ano de publicação:\n--> ")

            os.system("cls")

            autor = input("Autor do livro:\n-->")

            os.system("cls")

            editora = input("Editora do livro:\n--> ")

            os.system("cls")

            
            livro = Romance(nome, ano, autor, editora)
            livros_romance.append(livro)
            livros[nome] = livro
            print(f"\nLivro '{nome}' cadastrado com sucesso!")
            time.sleep(2)

        if tipo_livro == "2":
            os.system("cls")

            nome = input("Nome do livro:\n-->")

            os.system("cls")

            ano = input("Ano de publicação:\n--> ")

            os.system("cls")

            autor = input("Autor do livro:\n-->")

            os.system("cls")

            editora = input("Editora do livro:\n--> ")

            os.system("cls")
            
            livro = Poesia(nome, ano, autor, editora)
            livros_poesia.append(livro)
            livros[nome] = livro
            print(f"\nLivro '{nome}' cadastrado com sucesso!")
            time.sleep(2)

        if tipo_livro == "3":

            os.system("cls")

            nome = input("Nome do livro:\n-->")

            os.system("cls")

            ano = input("Ano de publicação:\n--> ")

            os.system("cls")

            autor = input("Autor do livro:\n-->")

            os.system("cls")
            editora = input("Editora do livro:\n--> ")

            os.system("cls")

            
            livro = Conto(nome, ano, autor, editora)
            livros_poesia.append(livro)
            livros[nome] = livro
            print(f"\nLivro '{nome}' cadastrado com sucesso!")
            time.sleep(2)

        if tipo_livro == "4":

            os.system("cls")

            nome = input("Nome do livro:\n-->")

            os.system("cls")

            ano = input("Ano de publicação:\n--> ")

            os.system("cls")

            autor = input("Autor do livro:\n-->")

            os.system("cls")

            editora = input("Editora do livro:\n--> ")

            os.system("cls")
            
    
            livro = Cronica(nome, ano, autor, editora)
            livros_cronica.append(livro)
            livros[nome] = livro
            print(f"\nLivro '{nome}' cadastrado com sucesso!")
            time.sleep(2)

        if tipo_livro == "5":

            os.system("cls")

            nome = input("Nome do livro:\n-->")

            os.system("cls")

            ano = input("Ano de publicação:\n--> ")

            os.system("cls")

            autor = input("Autor do livro:\n-->")

            os.system("cls")

            editora = input("Editora do livro:\n--> ")

            os.system("cls")
            
            livro = Drama(nome, ano, autor, editora)
            livros_drama.append(livro)
            livros[nome] = livro
            print(f"\nLivro '{nome}' cadastrado com sucesso!")
            time.sleep(2)

        os.system("cls")
        print("Deseja cadastrar outro livro?")
        print("\n1 - Sim")
        print("2 - Não, voltar ao menu principal")

        voltar = input("\n--> ")

        if voltar == "2":
            break


        return livros, tipo_livro
        
    
    def remover_livro():
        while True:
            os.system("cls")
            print("Remover Livro".center(50, "-"))
            print("\nEscolha o tipo de livro para remover:")
            print("1 - Romance")
            print("2 - Poesia")
            print("3 - Conto")
            print("4 - Crônica")
            print("5 - Drama")
            print("6 - Voltar ao menu principal")
            tipo = input("\nDigite o número do tipo do livro: ")
    
            if tipo == "6":
                break
    
            if tipo == "1":
                lista = livros_romance
            elif tipo == "2":
                lista = livros_poesia
            elif tipo == "3":
                lista = livros_conto
            elif tipo == "4":
                lista = livros_cronica
            elif tipo == "5":
                lista = livros_drama
            else:
                print("Tipo inválido!")
                time.sleep(2)
                continue
    
            if not lista:
                print(f"\nNenhum livro cadastrado nesse tipo.")
                time.sleep(2)
                continue
    
            print(f"\nLivros cadastrados:")
            for idx, livro in enumerate(lista, 1):
                print(f"{idx} - {livro.nome}")
    
            idx_remover = input("\nDigite o número do livro para remover (ou 0 para cancelar): ")
            if idx_remover == "0":
                continue
    
            try:
                idx_remover = int(idx_remover) - 1
                if 0 <= idx_remover < len(lista):
                    livro_removido = lista.pop(idx_remover)
                    print(f"\nLivro '{livro_removido.nome}' removido com sucesso!")
                else:
                    print("Número inválido!")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número.")
                time.sleep(2)
                continue






        

