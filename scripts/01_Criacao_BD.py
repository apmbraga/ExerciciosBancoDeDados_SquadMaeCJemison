# Criando o Banco de Dados da Biblioteca.


import sqlite3

conexao = sqlite3.connect("biblioteca")
cursor = conexao.cursor()

conexao.execute(
    "CREATE TABLE livros(id_livro INTEGER PRIMARY KEY AUTOINCREMENT, titulo VARCHAR(100), autor VARCHAR(50), genero VARCHAR(30), editora VARCHAR(30), FG_disponivel BIT NOT NULL);"
)
conexao.execute(
    "CREATE TABLE usuarios(id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), telefone int (11), nacionalidade VARCHAR(30));"
)
conexao.execute(
    "CREATE TABLE emprestimos(id_op INTEGER PRIMARY KEY AUTOINCREMENT, id_usuario INTEGER, id_livro INTEGER, data_emprestimo DATE, data_devolucao DATE, FG_devolvido BIT NOT NULL,FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario), FOREIGN KEY (id_livro) REFERENCES livros (id_livro));"
)
