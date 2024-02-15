import sqlite3

conexao = sqlite3.connect("biblioteca")
cursor = conexao.cursor()

# CONSULTA: 

# -> Querys a serem executadas quando uma pessoa pega um livro emprestado: 
#Colocamos o cadastro dela na aba de empréstimos de livros e a atualizamos a Flag de Disponível em livros para 1, mostrando estar indisponível.
cursor.execute('INSERT INTO emprestimos (id_usuario, id_livro, data_emprestimo, data_devolucao, FG_devolvido) VALUES (10,12,"2024-02-01", "",0)')
cursor.execute('UPDATE livros SET FG_disponivel = 0 where id_livro = 12')

# Quando a pessoa devolve, é feito o update nas duas tabelas - Empréstimos e Livros
cursor.execute('update emprestimos SET FG_devolvido = 1 where id_op = 2') #FG_Devolvido = 1 - FOI DEVOLVIDO
cursor.execute('UPDATE livros SET FG_disponivel = 1 where id_livro = 12') #FG Disponível = 1 - Está disponível para um novo empréstimo


# REMOVER UM LIVRO DANIFICADO DO ACERVO
cursor.execute('DELETE from livros where id_livro = 13')


conexao.commit()

conexao.close
