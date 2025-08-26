````markdown
# Sistema de Gerenciamento de Biblioteca

Este projeto é um sistema simples em Python para gerenciamento de livros de diferentes gêneros literários, permitindo adicionar, listar e remover livros, além de consultar autores e gêneros específicos.

## Funcionalidades

O sistema permite:

- **Adicionar livros** em diferentes categorias:
  - Romance
  - Poesia
  - Conto
  - Crônica
  - Drama
- **Listar todos os livros** cadastrados com informações detalhadas.
- **Remover livros** pelo ID.
- **Listar autores** disponíveis e consultar os livros de cada autor.
- **Listar livros por gênero**.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

- **classes.py**: Contém as classes que representam cada gênero literário (`Romance`, `Poesia`, `Conto`, `Cronica`, `Drama`) com métodos de acesso (get/set) e método para exibir informações do livro.
- **main.py**: Contém a lógica do sistema, incluindo funções para adicionar, listar e remover livros, além de consultar autores e gêneros.
- **dicionarios de livros**: Cada gênero possui um dicionário que armazena os livros cadastrados, e todos os livros estão agregados no dicionário `livros`.

## Estrutura das Classes

Cada classe de livro possui:

- Atributos privados:
  - `nome`
  - `ano`
  - `autor`
  - `editora`
- Métodos getters e setters para manipulação segura dos atributos.
- Método de exibição das informações do livro, por exemplo:
  ```python
  def mostrarinfo_romance(self):
      return f"Romance: {self.__nome} ({self.__ano})\nAutor: {self.__autor}\nEditora: {self.__editora}"
````

## Como Usar

1. **Adicionar um livro**:

   * Escolha a categoria e insira os dados do livro (nome, ano, autor e editora).

2. **Listar livros**:

   * Exibe todos os livros cadastrados, mostrando ID, tipo, nome, ano, autor e editora.

3. **Remover livro**:

   * Informe o ID do livro que deseja remover.

4. **Listar autores e livros**:

   * Mostra todos os autores cadastrados e permite selecionar um para visualizar seus livros.

5. **Listar livros por gênero**:

   * Escolha o gênero desejado e veja os livros correspondentes.

## Exemplos de Uso

```python
# Listar todos os livros
listar_livros()

# Adicionar novo livro
adicionar_livro()

# Remover livro pelo ID
remover_livro()

# Listar autores e livros de um autor específico
listar_autores_e_livros()

# Listar livros por gênero
listar_generos()
```

## Requisitos

* Python 3.8 ou superior
* Bibliotecas:

  * `os`
  * `time`
  * `cv2` (opcional, caso queira usar recursos de imagem)

## Observações

* Cada livro é armazenado em um dicionário específico do seu gênero e no dicionário geral `livros`.
* O sistema ainda é baseado em terminal/console, podendo ser expandido para interface gráfica no futuro.

```
