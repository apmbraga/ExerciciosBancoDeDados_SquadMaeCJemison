## Populando a Tabela de usuarios

import sqlite3

conexao = sqlite3.connect("biblioteca")
cursor = conexao.cursor()

cursor.execute(
    'INSERT INTO usuarios (nome, telefone,nacionalidade) VALUES ("Valesca de Andrade","2199652345","Brasileira"), ("Carlos Alberto","11965324589","Mexicano"), ("Maite Gonzales","11956892341","Mexicana"), ("Leandro de Oliveira","65995623584","Brasileiro"), ("Luciana Mendes","11995632859","Sueca"), ("Madalena Almeida","82985693241","Espanhola"), ("Mariana Lima","72956845236","Brasileira"),("Antonio Nunes","85945874521","Chileno"),("Maria Fernandes","61978653245","Peruana"),("Yolanda Lima","91998562365","Portuguesa")'
)
cursor.execute(
    'INSERT INTO livros (titulo,autor,genero,editora, FG_disponivel) VALUES ("O Iluminado","Stephen King","Terror","Editora Objetiva", 1),("Psicose","Robert Bloch","Suspense Psicológico","Editora Darkside",1),("O Exorcista","William Peter Blatty","Terror","Editora HarperCollins",1),("Coraline","Neil Gaiman","Terror/Fantasia","Editora Rocco",1),("O Silêncio dos Inocentes","Thomas Harris","Suspense Psicológico","Editora Record",1),("It-A Coisa","Stephen King","Terror","Editora Suma de letras",1),("O Colecionador","John Fowles","Suspense Psicológico","Editora Companhia das Letras",1),("Drácula","Bram Stoker","Terror Gótico","Editora Zahar",1),("Garota Exemplar","Gillian Flynn","Suspense Psicológico","Editora Intrínseca",1),("Misery","Stephen King","Terror Psicológico","Editora Objetiva",1)'
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