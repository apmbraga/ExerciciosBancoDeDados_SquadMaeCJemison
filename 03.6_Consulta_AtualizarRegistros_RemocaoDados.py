import sqlite3

conexao = sqlite3.connect('biblioteca')
cursor = conexao.cursor()

#CONSULTA: 


conexao.commit()

conexao.close