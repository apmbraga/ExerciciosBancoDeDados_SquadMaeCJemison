## Populando a Tabela de usuarios

import sqlite3

conexao = sqlite3.connect("biblioteca")
cursor = conexao.cursor()

cursor.execute(
    'INSERT INTO usuarios (nome, telefone,nacionalidade) VALUES ("Alice Almeida","24991546789","Brasileira"), ("Bernardo Silva","79992746700","Chilena"),("Carlos Brito","32981546789","Brasileira"), ("David Gabriel Soares","21981236755","Brasileira"), ("Eleanor Oliveira","95988446721","Brasileira"), ("Fabian Moscovic","41987541209","Argentina"), ("Geraldo ALves Prado","79980912367","Brasileira")'
)
cursor.execute(
    'INSERT INTO livros (titulo,autor,genero,editora, FG_disponivel) VALUES ("Dom Quixote", "Miguel de Cervantes", "Romance", "Editora Saraiva", 1), ("Orgulho e Preconceito", "Jane Austen", "Romance", "Editora Record", 1), ("Crime e Castigo", "Fiódor Dostoiévski", "Romance", "Editora Intrínseca", 1), ("Cem Anos de Solidão", "Gabriel García Márquez", "Romance", "Editora Companhia das Letras", 1), ("O Apanhador no Campo de Centeio", "J.D. Salinger", "Romance", "Editora Globo", 1), ("1984", "George Orwell", "Ficção Científica", "Editora Aleph", 1), ("Fundação", "Isaac Asimov", "Ficção Científica", "Editora Devir", 1), ("Duna", "Frank Herbert", "Ficção Científica", "Editora Nova Fronteira", 1), ("Neuromancer", "William Gibson", "Ficção Científica", "Editora Leya", 1), ("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", "Editora Martins Fontes", 1), ("As Crônicas de Nárnia", "C.S. Lewis", "Fantasia", "Editora WMF Martins Fontes", 1), ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia", "Editora Rocco", 1), ("A Metamorfose", "Franz Kafka", "Ficção", "Editora L&PM", 1), ("O Estrangeiro", "Albert Camus", "Ficção", "Editora Record", 1), ("Memórias Póstumas de Brás Cubas", "Machado de Assis", "Ficção", "Editora Nova Aguilar", 1), ("Ensaio sobre a Cegueira", "José Saramago", "Ficção", "Editora Companhia das Letras", 1), ("Moby Dick", "Herman Melville", "Clássico", "Editora Zahar", 1), ("A Divina Comédia", "Dante Alighieri", "Clássico", "Editora Martin Claret", 1), ("Os Lusíadas", "Luís de Camões", "Clássico", "Editora Leya", 1), ("A Odisséia", "Homero", "Clássico", "Editora Companhia das Letras", 1), ("O Príncipe", "Nicolau Maquiavel", "Filosofia", "Editora Martin Claret", 1), ("Assim Falou Zaratustra", "Friedrich Nietzsche", "Filosofia", "Editora Martin Claret", 1), ("O Segundo Sexo", "Simone de Beauvoir", "Filosofia", "Editora Nova Fronteira", 1), ("O Capital", "Karl Marx", "Filosofia", "Editora Boitempo", 1), ("O Processo", "Franz Kafka", "Drama", "Editora L&PM", 1), ("Hamlet", "William Shakespeare", "Drama", "Editora Penguin-Companhia", 1), ("Odisseia", "Homero", "Épico", "Editora Nova Alexandria", 1), ("Ulisses", "James Joyce", "Épico", "Editora Penguin-Companhia", 1), ("O Grande Gatsby", "F. Scott Fitzgerald", "Romance", "Editora Record", 1), ("Lolita", "Vladimir Nabokov", "Romance", "Editora Alfaguara", 1), ("A Insustentável Leveza do Ser", "Milan Kundera", "Romance", "Editora Companhia das Letras", 1), ("A Revolução dos Bichos", "George Orwell", "Ficção", "Editora Companhia das Letras", 1), ("O Retrato de Dorian Gray", "Oscar Wilde", "Ficção", "Editora L&PM", 1), ("A Hora da Estrela", "Clarice Lispector", "Ficção", "Editora Rocco", 1), ("O Cortiço", "Aluísio Azevedo", "Ficção", "Editora Martin Claret", 1), ("Vidas Secas", "Graciliano Ramos", "Ficção", "Editora Record", 1), ("O Guarani", "José de Alencar", "Romance", "Editora Martin Claret", 1), ("Iracema", "José de Alencar", "Romance", "Editora Martin Claret", 1), ("O Seminarista", "Bernardo Guimarães", "Romance", "Editora Martin Claret", 1), ("Senhora", "José de Alencar", "Romance", "Editora Martin Claret", 1), ("Capitães da Areia", "Jorge Amado", "Romance", "Editora Companhia das Letras", 1), ("Gabriela, Cravo e Canela", "Jorge Amado", "Romance", "Editora Companhia das Letras", 1), ("Don Casmurro", "Machado de Assis", "Romance", "Editora Martin Claret", 1), ("Memorial de Aires", "Machado de Assis", "Romance", "Editora Martin Claret", 1), ("Vidas Secas", "Graciliano Ramos", "Romance", "Editora Record", 1), ("Macunaíma", "Mário de Andrade", "Romance", "Editora Martin Claret", 1), ("São Bernardo", "Graciliano Ramos", "Romance", "Editora Record", 1), ("O Quinze", "Rachel de Queiroz", "Romance", "Editora José Olympio", 1), ("O Guarani", "José de Alencar", "Romance", "Editora Martin Claret", 1), ("Iracema", "José de Alencar", "Romance", "Editora Martin Claret", 1)'
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
