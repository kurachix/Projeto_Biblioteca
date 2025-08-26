# construtor da classe
livros_emprestados = {}
# romance poesia conto cronica drama

class Romance:

    def __init__(self, nome, ano, autor, editora):
        self.__nome = nome
        self.__ano = ano
        self.__autor = autor
        self.__editora = editora

# get e set dos atributos

    def getNome(self):
        return self.__nome

    def getAno(self):
        return self.__ano

    def getAutor(self):
        return self.__autor

    def getEditora(self):
        return self.__editora

    def setNome(self, nome):
        self.__nome = nome
        return self.__nome

    def setAno(self, ano):
        self.__ano = ano
        return self.__ano

    def setAutor(self, autor):
        self.__autor = autor
        return self.__autor

    def setEditora(self, editora):
        self.__editora = editora
        return self.__editora

# metódo de descrição do livro

    def mostrarinfo_romance(self):
        return f"Romance: {self.__nome} ({self.__ano})\nAutor: {self.__autor}\nEditora: {self.__editora}"

#-----------------------------------------------------------------------------------------------------------#

# construtor da classe

class Poesia:

    def __init__(self, nome, ano, autor, editora):
        self.__nome = nome
        self.__ano = ano
        self.__autor = autor
        self.__editora = editora

# get e set dos atributos

    def getNome(self):
        return self.__nome

    def getAno(self):
        return self.__ano

    def getAutor(self):
        return self.__autor

    def getEditora(self):
        return self.__editora

    def setNome(self, nome):
        self.__nome = nome
        return self.__nome

    def setAno(self, ano):
        self.__ano = ano
        return self.__ano

    def setAutor(self, autor):
        self.__autor = autor
        return self.__autor

    def setEditora(self, editora):
        self.__editora = editora
        return self.__editora

# metódo de descrição do livro

    def mostrarinfo_poesia(self):
        return f"Poesia: {self.__nome} ({self.__ano})\nAutor: {self.__autor}\nEditora: {self.__editora}"

#-----------------------------------------------------------------------------------------------------------#
# construtor da classe

class Conto:

    def __init__(self, nome, ano, autor, editora):
        self.__nome = nome
        self.__ano = ano
        self.__autor = autor
        self.__editora = editora

# get e set dos atributos

    def getNome(self):
        return self.__nome

    def getAno(self):
        return self.__ano

    def getAutor(self):
        return self.__autor

    def getEditora(self):
        return self.__editora

    def setNome(self, nome):
        self.__nome = nome
        return self.__nome

    def setAno(self, ano):
        self.__ano = ano
        return self.__ano

    def setAutor(self, autor):
        self.__autor = autor
        return self.__autor

    def setEditora(self, editora):
        self.__editora = editora
        return self.__editora

# metódo de descrição do livro

    def mostrarinfo_conto(self):
        return f"Conto: {self.__nome} ({self.__ano})\nAutor: {self.__autor}\nEditora: {self.__editora}"

#-----------------------------------------------------------------------------------------------------------#

# construtor da classe

class Cronica:

    def __init__(self, nome, ano, autor, editora):
        self.__nome = nome
        self.__ano = ano
        self.__autor = autor
        self.__editora = editora

# get e set dos atributos

    def getNome(self):
        return self.__nome

    def getAno(self):
        return self.__ano

    def getAutor(self):
        return self.__autor

    def getEditora(self):
        return self.__editora

    def setNome(self, nome):
        self.__nome = nome
        return self.__nome

    def setAno(self, ano):
        self.__ano = ano
        return self.__ano

    def setAutor(self, autor):
        self.__autor = autor
        return self.__autor

    def setEditora(self, editora):
        self.__editora = editora
        return self.__editora

# metódo de descrição do livro

    def mostrarinfo_cronica(self):
        return f"Cronica: {self.__nome} ({self.__ano})\nAutor: {self.__autor}\nEditora: {self.__editora}"
    
#-----------------------------------------------------------------------------------------------------------#

# construtor da classe

class Drama:

    def __init__(self, nome, ano, autor, editora):
        self.__nome = nome
        self.__ano = ano
        self.__autor = autor
        self.__editora = editora

# get e set dos atributos

    def getNome(self):
        return self.__nome

    def getAno(self):
        return self.__ano

    def getAutor(self):
        return self.__autor

    def getEditora(self):
        return self.__editora

    def setNome(self, nome):
        self.__nome = nome
        return self.__nome

    def setAno(self, ano):
        self.__ano = ano
        return self.__ano

    def setAutor(self, autor):
        self.__autor = autor
        return self.__autor

    def setEditora(self, editora):
        self.__editora = editora
        return self.__editora

# metódo de descrição do livro

    def mostrarinfo_drama(self):
        return f"Drama: {self.__nome} ({self.__ano})\nAutor: {self.__autor}\nEditora: {self.__editora}"

#-----------------------------------------------------------------------------------------------------------#

# Adicionando livros as classes
# romance poesia conto cronica drama

Romance_Dicionario = {
1 :Romance("Dom Casmurro", 1899, "Machado de Assis", "Saraiva"),
2 :Romance("É assim que acaba", 2018, "Colleen Hoover", "Galera"),
3 :Romance("A culpa é das estrelas", 2012, "John Green", "Intrínseca"),
4: Romance("Água Viva", 1973, "Clarice Lispector", "Rocco"),
5: Romance("O Morro dos Ventos Uivantes", 1847, "Emily Brontë", "Penguin Classics")
}

Poesia_Dicionario = {
6 :Poesia("Livro de Mágoas", 1851, "Álvares de Azevedo", "Lello & Irmão"),
7 :Poesia("Versos Íntimos", 1852, "Augusto dos Anjos", "José Olympio"),
8 :Poesia("Antologia Poética", 1944, "Carlos Drummond de Andrade", "Companhia das Letras"),
9 :Poesia("Poesia Completa", 1954, "Cecília Meireles", "Nova Fronteira"),
10 :Poesia("A Rosa do Povo", 1945, "Carlos Drummond de Andrade", "Companhia das Letras"),
11: Poesia("O Guardador de Rebanhos", 1913, "Fernando Pessoa", "Penguin Classics"),
12: Poesia("Poemas Escolhidos", 1959, "Manuel Bandeira", "Companhia das Letras")
}

Conto_Dicionario = {
13 :Conto("O Alienista", 1882, "Machado de Assis", "Saraiva"),
14 :Conto("Vidas Secas", 1938, "Graciliano Ramos", "José Olympio"),
15 :Conto("Felicidade Clandestina", 1971, "Clarice Lispector", "Rocco"),
16 :Conto("O Homem Nu", 1925, "Fernando Sabino", "Record"),
17 :Conto("A Cartomante", 1884, "Machado de Assis", "Saraiva"),
18 :Conto("O Primo Basílio", 1878, "José Maria de Eça de Queirós", "Penguin Classics"),
19 :Conto("A Metamorfose", 1915, "Franz Kafka", "Penguin Classics")
}


Cronica_Dicionario = {
20 :Cronica("Crônicas de Nárnia", 1950, "C.S. Lewis", "HarperCollins"),
21 :Cronica("O Pequeno Príncipe", 1943, "Antoine de Saint-Exupéry", "Reynal & Hitchcock"),
22 :Cronica("As Crônicas de Gelo e Fogo", 1996, "George R.R. Martin", "Bantam Books"),
23 :Cronica("O Senhor dos Anéis", 1954, "J.R.R. Tolkien", "Allen & Unwin"),
24 :Cronica("Harry Potter e a Pedra Filosofal", 1997, "J.K. Rowling", "Bloomsbury"),
25 :Cronica("Percy Jackson e os Olimpianos", 2005, "Rick Riordan", "Disney-Hyperion"),
26 :Cronica("As Aventuras de Sherlock Holmes", 1892, "Arthur Conan Doyle", "Penguin Classics")
}

Drama_Dicionario = {
27 :Drama("Hamlet", 1603, "William Shakespeare", "Penguin Classics"),
28 :Drama("Romeu e Julieta", 1597, "William Shakespeare", "Penguin Classics"),
29 :Drama("Macbeth", 1606, "William Shakespeare", "Penguin Classics"),
30 :Drama("A Casa de Bernarda Alba", 1936, "Federico García Lorca", "Penguin Classics"),
31 :Drama("O Auto da Compadecida", 1955, "Ariano Suassuna", "Record"),
32 :Drama("Esperando Godot", 1952, "Samuel Beckett", "Grove Press")
}

generos = {
        1: ("Romance", Romance_Dicionario),
        2: ("Poesia", Poesia_Dicionario),
        3: ("Conto", Conto_Dicionario),
        4: ("Crônica", Cronica_Dicionario),
        5: ("Drama", Drama_Dicionario)
    }

#-----------------------------------------------------------------------------------------------------------#
# livros_drama livros_cronica livros_conto livros_poesia livros_romance

livros = {**Romance_Dicionario, **Poesia_Dicionario, **Conto_Dicionario, **Cronica_Dicionario, **Drama_Dicionario}

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