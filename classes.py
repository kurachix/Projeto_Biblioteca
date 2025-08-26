# construtor da classe

livros_poesia = []
livros_romance = []
livros_conto = []
livros_cronica = []
livros_drama = []
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

livros_romance.append(Romance("Dom Casmurro", 1899, "Machado de Assis", "Saraiva"))
livros_romance.append(Romance("É assim que acaba", 2018, "Colleen Hoover", "Galera"))
livros_romance.append(Romance("A culpa é das estrelas", 2012, "John Green", "Intrínseca"))
livros_romance.append(Romance("Água Viva", 1973, "Clarice Lispector", "Rocco"))
livros_romance.append(Romance("O Morro dos Ventos Uivantes", 1847, "Emily Brontë", "Penguin Classics"))

livros_poesia.append(Poesia("Livro de Mágoas", 1851, "Álvares de Azevedo", "Lello & Irmão"))
livros_poesia.append(Poesia("Versos Íntimos", 1852, "Augusto dos Anjos", "José Olympio"))
livros_poesia.append(Poesia("Antologia Poética", 1944, "Carlos Drummond de Andrade", "Companhia das Letras"))
livros_poesia.append(Poesia("Poesia Completa", 1954, "Cecília Meireles", "Nova Fronteira"))
livros_poesia.append(Poesia("A Rosa do Povo", 1945, "Carlos Drummond de Andrade", "Companhia das Letras"))
livros_poesia.append(Poesia("O Guardador de Rebanhos", 1913, "Fernando Pessoa", "Penguin Classics"))
livros_poesia.append(Poesia("Poemas Escolhidos", 1959, "Manuel Bandeira", "Companhia das Letras"))

livros_conto.append(Conto("O Alienista", 1882, "Machado de Assis", "Saraiva"))
livros_conto.append(Conto("Vidas Secas", 1938, "Graciliano Ramos", "José Olympio"))
livros_conto.append(Conto("Felicidade Clandestina", 1971, "Clarice Lispector", "Rocco"))
livros_conto.append(Conto("O Homem Nu", 1925, "Fernando Sabino", "Record"))
livros_conto.append(Conto("A Cartomante", 1884, "Machado de Assis", "Saraiva"))
livros_conto.append(Conto("O Primo Basílio", 1878, "José Maria de Eça de Queirós", "Penguin Classics"))
livros_conto.append(Conto("A Metamorfose", 1915, "Franz Kafka", "Penguin Classics"))

livros_cronica.append(Cronica("Crônicas de Nárnia", 1950, "C.S. Lewis", "HarperCollins"))
livros_cronica.append(Cronica("O Pequeno Príncipe", 1943, "Antoine de Saint-Exupéry", "Reynal & Hitchcock"))
livros_cronica.append(Cronica("As Crônicas de Gelo e Fogo", 1996, "George R.R. Martin", "Bantam Books"))
livros_cronica.append(Cronica("O Senhor dos Anéis", 1954, "J.R.R. Tolkien", "Allen & Unwin"))
livros_cronica.append(Cronica("Harry Potter e a Pedra Filosofal", 1997, "J.K. Rowling", "Bloomsbury"))
livros_cronica.append(Cronica("Percy Jackson e os Olimpianos", 2005, "Rick Riordan", "Disney-Hyperion"))
livros_cronica.append(Cronica("As Aventuras de Sherlock Holmes", 1892, "Arthur Conan Doyle", "Penguin Classics"))

livros_drama.append(Drama("Hamlet", 1603, "William Shakespeare", "Penguin Classics"))
livros_drama.append(Drama("Romeu e Julieta", 1597, "William Shakespeare", "Penguin Classics"))
livros_drama.append(Drama("Macbeth", 1606, "William Shakespeare", "Penguin Classics"))
livros_drama.append(Drama("A Casa de Bernarda Alba", 1936, "Federico García Lorca", "Penguin Classics"))
livros_drama.append(Drama("O Auto da Compadecida", 1955, "Ariano Suassuna", "Record"))
livros_drama.append(Drama("Esperando Godot", 1952, "Samuel Beckett", "Grove Press"))
#-----------------------------------------------------------------------------------------------------------#
# livros_drama livros_cronica livros_conto livros_poesia livros_romance