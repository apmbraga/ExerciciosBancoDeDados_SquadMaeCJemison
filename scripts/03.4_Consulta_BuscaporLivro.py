import sqlite3

conexao = sqlite3.connect("biblioteca")
cursor = conexao.cursor()

# CONSULTA 4: Verificar o número de cópias disponíveis de um determinado livro.
copiaslivres = cursor.execute(
    'SELECT COUNT (titulo) from livros where titulo = "As vantagens de ser invisivel"'
)
for _exemplares in copiaslivres:
    print(_exemplares)

conexao.commit()

conexao.close
