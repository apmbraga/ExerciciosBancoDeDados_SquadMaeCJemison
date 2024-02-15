import sqlite3
from datetime import date

conexao = sqlite3.connect("biblioteca")
cursor = conexao.cursor()

# Para saber quais livros estão atrasados podemos fazer a seguinte query:

livros_nao_entregues = cursor.execute(
    """
    SELECT 
        e.id_op,
        e.id_usuario,
        e.id_livro,
        e.data_emprestimo,
        e.data_devolucao
    FROM emprestimos e
    where e.data_devolucao = ''
"""
)
print("Livros que não possuem data de devolução:")
for livros in livros_nao_entregues:
    print(livros)

# Porém, caso queiramos inserir uma regra de negócio que diz que um livro é considerado
# como atrasado a partir de 5 dias corridos não entregues podemos rodar a seguinte query:

data_atual = date.today()

livros_nao_entregues_atual = cursor.execute(
    f"""
    SELECT 
        e.id_op,
        u.nome,
        li.titulo,
        li.autor,
        e.data_emprestimo,
        CASE
            WHEN e.data_devolucao IS '' THEN "Livro não devolvido."
        end AS "data_devolucao",
        CASE 
            WHEN e.data_devolucao = '' THEN JULIANDAY('{data_atual}') - JULIANDAY(e.data_emprestimo)
        END AS "dias_corridos_atraso"
    FROM emprestimos e
    INNER JOIN 
	usuarios u ON u.id_usuario = e.id_usuario 
    INNER JOIN 
	livros lI ON li.id_livro = e.id_livro
    WHERE dias_corridos_atraso >= 5
"""
)
print(f"Livros não devolvidos até a data {data_atual}")
print (
    "ID | Emprestado para |Titulo | Autor | Data do empréstimo | Status | Dias Corridos desde o Emprestimo"
)
for livros in livros_nao_entregues_atual:
    print(livros)

conexao.commit()
conexao.close
