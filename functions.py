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






        

