## Populando a Tabela de usuarios

import sqlite3

conexao = sqlite3.connect("biblioteca")
cursor = conexao.cursor()

cursor.execute(
    'INSERT INTO usuarios (nome, telefone,nacionalidade) VALUES ("Alice Almeida","24991546789","Brasileira"), ("Bernardo Silva","79992746700","Chilena"),("Carlos Brito","32981546789","Brasileira"), ("David Gabriel Soares","21981236755","Brasileira"), ("Eleanor Oliveira","95988446721","Brasileira"), ("Fabian Moscovic","41987541209","Argentina"), ("Geraldo ALves Prado","79980912367","Brasileira")'
)
cursor.execute(
    'INSERT INTO livros (titulo,autor,genero,editora, FG_disponivel) VALUES ("Angústia", "Graciliano Ramos", "Ficção", "Record",1), ("Dona Flor e seus Dois Maridos", "Jorge Amado", "Romance", 1)'
)
cursor.execute(
    'INSERT INTO emprestimos (id_usuario, id_livro, data_emprestimo, data_devolucao, FG_devolvido) VALUES (1,1,"2024-02-01", "2024-02-29",0)'
)
cursor.execute(
    """UPDATE emprestimos SET data_devolucao = '' WHERE id_op IN ("5","6","7")"""
)

# Simulação de empréstimos já devolvidos e ainda em curso para popular a tabela de Empréstimos (Primeiro há o usuarios do empréstimo, depois o Livro muda a Flag para indisponível)

conexao.commit()
usuarios = cursor.execute("SELECT * FROM usuarios u;")
emprestimos_criados = cursor.execute("SELECT * FROM emprestimos u;")
livros_criados = cursor.execute("SELECT * FROM livros u;")
if isinstance(livros_criados, sqlite3.Cursor):
    print("Tabela livros populada com sucesso!")
if isinstance(emprestimos_criados, sqlite3.Cursor):
    print("Tabela empréstimos populada com sucesso!")
if isinstance(usuarios, sqlite3.Cursor):
    print("Tabela usuários populada com sucesso!")

conexao.close