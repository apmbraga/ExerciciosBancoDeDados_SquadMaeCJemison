## Populando a Tabela de usuarios

import sqlite3

conexao = sqlite3.connect("biblioteca")
cursor = conexao.cursor()

cursor.execute(
    'INSERT INTO usuarios (nome, telefone,nacionalidade) VALUES ("Camila Oliveira", "87390495830", "Brasileira"), ("Rosana Pereira", "20394857293", "Brasielira"), ("Daniel Alves" "98374629045", "Brasileira"), ("Roberto Cabral", "87293847289", "Brasileira"), ("Carol de Moraes", "99283746384", "Brasileira")'
)
cursor.execute(
    'INSERT INTO livros (titulo,autor,genero,editora, FG_disponivel) VALUES ("Clean Code: Código Limpo", "Robert C. Martin", "Programação", "Editora Alta Books", 1), ("Aprenda Python 3.0 com Facilidade", "Fabrizio Romano", "Programação", "Editora Novatec", 1), ("JavaScript: O Guia Definitivo", "David Flanagan", "Programação", "Editora Novatec", 1), ("Python Fluente", "Luciano Ramalho", "Programação", "Editora O''Reilly", 1), ("Algoritmos: Teoria e Prática", "Thomas H. Cormen, "Programação", "Editora Campus", 1)'
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
