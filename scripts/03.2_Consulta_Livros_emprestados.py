import sqlite3

conexao = sqlite3.connect("biblioteca")
cursor = conexao.cursor()


# CONSULTA 2:  Encontrar todos os livros emprestados no momento, com TITULO DO LIVRO, QUEM PEGOU O LIVRO, DATA DO EMPRÉSTIMO E PRAZO PARA DEVOLUÇÃO
emprestados = cursor.execute(
    "SELECT livros.id_livro, livros.titulo, usuarios.nome, emprestimos.data_emprestimo from emprestimos INNER JOIN livros ON emprestimos.id_livro = livros.id_livro INNER JOIN usuarios ON emprestimos.id_usuario = usuarios.id_usuario where FG_devolvido = 0"
)
print(
    "ID Livro | Titulo | Usuário com o Livro | Data do Empréstimo:"
)
for _livrosindisponiveis in emprestados:
    print(_livrosindisponiveis)


conexao.commit()

conexao.close
