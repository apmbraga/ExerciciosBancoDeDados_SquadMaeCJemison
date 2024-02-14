## Populando a Tabela Livros

import sqlite3

conexao = sqlite3.connect("biblioteca")
cursor = conexao.cursor()

cursor.execute(
    'INSERT INTO livros (titulo,autor,genero,editora, FG_disponivel) VALUES ("1984", "George Orwell", "Ficção Distópica", "Editora Companhia das Letras", 1), ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Literatura Infantil", "Editora Agir", 1), ("Cem Anos de Solidão", "Gabriel García Márquez", "Realismo Mágico", "Editora Record", 0), ("A Revolução dos Bichos", "George Orwell", "Fábula", "Editora Companhia das Letras", 1), ("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", "Editora Martins Fontes", 0), ("Crime e Castigo", "Fyodor Dostoevsky", "Romance Psicológico", "Editora 34", 1), ("Moby Dick", "Herman Melville", "Aventura", "Editora Penguin Companhia", 0), ("Orgulho e Preconceito", "Jane Austen", "Romance", "Editora Martin Claret", 1), ("Clean Code: A Handbook of Agile Software Craftsmanship", "Robert C. Martin", "Programação", "Editora Prentice Hall", 0), ("Inteligência Artificial: Uma Abordagem Moderna", "Stuart Russell e Peter Norvig", "Inteligência Artificial", "Editora Prentice Hall", 1)'
)
conexao.commit()

livros_criados = cursor.execute("SELECT * FROM livros u;")
if isinstance(livros_criados, sqlite3.Cursor):
    print("Tabela livros populada com sucesso!")

conexao.close