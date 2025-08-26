# construtor da classe

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

livros_romance = Romance(nome="Dom Casmurro", ano=1899, autor="Machado de Assis", editora="Saraiva")
livros_romance= Romance(nome="É assim que acaba", ano=2018, autor="Colleen Hoover", editora="Galera")
livros_romance = Romance(nome="A culpa é das estrelas", ano=2012, autor="John Green", editora="Intrínseca")
livros_romance = Romance(nome="Água Viva", ano=1973, autor="Clarice Lispector", editora="Rocco")
livros_romance = Romance(nome="O Morro dos Ventos Uivantes", ano=1847, autor="Emily Brontë", editora="Penguin Classics")

livros_poesia = Poesia(nome="Livro de Mágoas", ano=1851, autor="Álvares de Azevedo", editora="Lello & Irmão")
livros_poesia = Poesia(nome="Versos Íntimos", ano=1852, autor="Augusto dos Anjos", editora="José Olympio")
livros_poesia = Poesia(nome="Antologia Poética", ano=1944, autor="Carlos Drummond de Andrade", editora="Companhia das Letras")
livros_poesia = Poesia(nome="Poesia Completa", ano=1954, autor="Cecília Meireles", editora="Nova Fronteira")
livros_poesia = Poesia(nome="A Rosa do Povo", ano=1945, autor="Carlos Drummond de Andrade", editora="Companhia das Letras")
livros_poesia = Poesia(nome="O Guardador de Rebanhos", ano=1913, autor="Fernando Pessoa", editora="Penguin Classics")
livros_poesia = Poesia(nome="Poemas Escolhidos", ano=1959, autor="Manuel Bandeira", editora="Companhia das Letras")

livros_conto = Conto(nome="O Alienista", ano=1882, autor="Machado de Assis", editora="Saraiva")
livros_conto = Conto(nome="Vidas Secas", ano=1938, autor="Graciliano Ramos", editora="José Olympio")
livros_conto = Conto(nome="Felicidade Clandestina", ano=1971, autor="Clarice Lispector", editora="Rocco")
livros_conto = Conto(nome="O Homem Nu", ano=1925, autor="Fernando Sabino", editora="Record")
livros_conto = Conto(nome="A Cartomante", ano=1884, autor="Machado de Assis", editora="Saraiva")
livros_conto = Conto(nome="O Primo Basílio", ano=1878, autor="José Maria de Eça de Queirós", editora="Penguin Classics")
livros_conto = Conto(nome="A Metamorfose", ano=1915, autor="Franz Kafka", editora="Penguin Classics")


livros_cronica = Cronica(nome="Crônicas de um Diário", ano=1998, autor="Luis Fernando Veríssimo", editora="Companhia das Letras")
livros_cronica = Cronica(nome="O Mundo é um Moinho", ano=2000, autor="Carlos Drummond de Andrade", editora="Companhia das Letras")
livros_cronica = Cronica(nome="A Vida como Ela É...", ano=1964, autor="Nelson Rodrigues", editora="Nova Fronteira")
livros_cronica = Cronica(nome="O Canto da Sereia", ano=2002, autor="Chico Buarque", editora="Companhia das Letras")
livros_cronica = Cronica(nome="Feliz Ano Velho", ano=1975, autor="Marcelo Rubens Paiva", editora="Globo")
livros_cronica = Cronica(nome="O Velho e o Mar", ano=1952, autor="Ernest Hemingway", editora="Scribner")
livros_cronica = Cronica(nome="A Hora da Estrela", ano=1977, autor="Clarice Lispector", editora="Rocco")

livros_drama = Drama(nome="Hamlet", ano=1603, autor="William Shakespeare", editora="Penguin Classics")
livros_drama = Drama(nome="Romeu e Julieta", ano=1597, autor="William Shakespeare", editora="Penguin Classics")
livros_drama = Drama(nome="Macbeth", ano=1606, autor="William Shakespeare", editora="Penguin Classics")
livros_drama = Drama(nome="A Casa de Bernarda Alba", ano=1936, autor="Federico García Lorca", editora="Penguin Classics")
livros_drama = Drama(nome="O Auto da Compadecida", ano=1955, autor="Ariano Suassuna", editora="Record")
livros_drama = Drama(nome="Esperando Godot", ano=1952, autor="Samuel Beckett", editora="Grove Press")
#-----------------------------------------------------------------------------------------------------------#

