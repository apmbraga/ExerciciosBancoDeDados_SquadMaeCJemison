# Consultas Solicitadas
import sqlite3

conexao = sqlite3.connect("biblioteca")
cursor = conexao.cursor()

# CONSULTA 1 :  Listar todos os livros disponíveis - Sem repetição de exemplares.
disponivel = cursor.execute(
    "SELECT DISTINCT titulo, autor from livros where FG_Disponivel = 1 order by titulo"
)
for _livroemestoque in disponivel:
    print(_livroemestoque)

# COM REPETIÇÃO DE EXEMPLARES
disponivel = cursor.execute(
    "SELECT titulo, autor from livros where FG_Disponivel = 1 order by titulo"
)
for _livroemestoque in disponivel:
    print(_livroemestoque)


conexao.commit()

conexao.close
