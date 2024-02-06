import sqlite3

conexao = sqlite3.connect('biblioteca')
cursor = conexao.cursor()

#CONSULTA 3: Localizar os livros escritos por um autor específico - SEM REPETIÇÃO
nomeautor = input('Digite o nome de um autor: ')
autor = cursor.execute(f'SELECT DISTINCT titulo from livros where autor LIKE "%{nomeautor}%" order by titulo')
for _buscaautor in autor:
    print(_buscaautor)
'''E se não houver autor, podemos colocar algum aviso ou só retorna vazio?'''

conexao.commit()

conexao.close