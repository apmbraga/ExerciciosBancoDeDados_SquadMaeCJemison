## Populando a Tabela de Cadastro

import sqlite3

conexao = sqlite3.connect('biblioteca')
cursor = conexao.cursor()

#cursor.execute('INSERT INTO cadastro (nome, telefone,nacionalidade) VALUES ("Alice Almeida","24991546789","Brasileira"), ("Bernardo Silva","79992746700","Chilena"),("Carlos Brito","32981546789","Brasileira"), ("David Gabriel Soares","21981236755","Brasileira"), ("Eleanor Oliveira","95988446721","Brasileira"), ("Fabian Moscovic","41987541209","Argentina"), ("Geraldo ALves Prado","79980912367","Brasileira")')
#cursor.execute('INSERT INTO livros (titulo,autor,genero,editora, FG_disponivel) VALUES ("As vantagens de ser invisivel","Stephen Chbosky","Drama","Rocco", 1), ("O Beijo das Sombras","Richelle Mead","Fantasia, Romance","HarperCollins", 1), ("Tocada pelas Sombras","Richelle Mead","Fantasia, Romance","HarperCollins", 1), ("Dom Casmurro","Machado de Assis","Romance, Ficção","Devir", 1), ("Memórias Póstumas de Brás Cubas","Machado de Assis","Romance, Ficção","Tipografia Nacional", 1), ("O Ladrão de Raios - Percy Jackson e os Olimpianos 1","Rick Riordan","Ficção Infantil e Juvenil","Intrínseca", 1), ("O mar de monstros: Série Percy Jackson e os olimpianos 2 ","Rick Riordan","Ficção Infantil e Juvenil","Intrínseca", 1), ("A maldição do titã: Série Percy Jackson e os olimpianos 3 ","Rick Riordan","Ficção Infantil e Juvenil","Intrínseca", 1), ("A Batalha do Labirinto - Percy Jackson e os Olimpianos 4 ","Rick Riordan","Ficção Infantil e Juvenil","Intrínseca", 1), ("O último olimpiano - Percy Jackson e os Olimpianos 5 ","Rick Riordan","Ficção Infantil e Juvenil","Intrínseca", 1), ("O cálice dos Deuses: - Percy Jackson e os Olimpianos 6","Rick Riordan","Ficção Infantil e Juvenil","Intrínseca", 1), ("As vantagens de ser invisivel","Stephen Chbosky","Adolescente","Rocco", 1), ("As vantagens de ser invisivel","Stephen Chbosky","Adolescente","Rocco", 1), ("O Beijo das Sombras","Richelle Mead","Fantasia, Romance","HarperCollins", 1), ("A maldição do titã: Série Percy Jackson e os olimpianos 3 ","Rick Riordan","Ficção Infantil e Juvenil","Intrínseca", 1), ("A Culpa é das Estrelas"," John Green","Romance, Ficção","Intrínseca", 1),("Quem é você, Alasca?"," John Green","Romance, Ficção","Intrínseca", 1),("Cidades de papel"," John Green","Romance, Ficção","Intrínseca", 1)')
#cursor.execute('INSERT INTO emprestimos (id_usuario, id_livro, data_emprestimo, data_devolucao, FG_devolvido) VALUES (1,1,"2024-02-01", "2024-02-29",0)')
cursor.execute('UPDATE livros SET FG_disponivel = 0 where id_livro = 0')


#Simulação de empréstimos já devolvidos e ainda em curso para popular a tabela de Empréstimos (Primeiro há o cadastro do empréstimo, depois o Livro muda a Flag para indisponível)


#cursor.execute('UPDATE livro SET FG_disponivel = 0 where id_livro = 1')

conexao.commit()

conexao.close

