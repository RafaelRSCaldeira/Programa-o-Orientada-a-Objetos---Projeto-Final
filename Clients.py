from Database import *
from Manager import Manager
from Person import Person

class Clients(Person):
    def __init__(self, company: str, phone: int) -> None:
        super().__init__(id, name, email)
        self.company = company
        self.phone = phone

    def register(self):
        try:
            self.cursor.execute("""
                INSERT INTO clientes (nome, email, empresa, telefone)
                VALUES (?, ?, ?, ?)
            """, (self.name, self.email, self.company, self.phone))
            self.connect.commit()
            print(f"Cliente '{self.name}' cadastrado com sucesso!")
        except sqlite3.Error as error:
            print(f"Erro ao cadastrar cliente: {error}")

    def view(self):
        pass 
    
    def update(self):
        if self.id:
            try:
                self.cursor.execute("""
                    UPDATE clientes SET nome = ?, email = ?, empresa = ?, telefone = ?
                    WHERE id = ?
                """, (self.name, self.email, self.company, self.phone, self.id))
                self.connect.commit()
                print(f"Cliente '{self.name}' atualizado com sucesso!")
            except sqlite3.Error as error:
                print(f"Erro ao atualizar cliente: {error}")
        else:
            print("Informe o ID do cliente para atualização.")

    def delete(self):
        """Exclui um cliente do banco de dados."""
        if self.id:
            try:
                confirmacao = input(f"Confirma a exclusão do cliente '{self.name}' (s/n)? ")
                if confirmacao.lower() == 's':
                    self.cursor.execute("DELETE FROM clientes WHERE id = ?", (self.id))
                    self.connect.commit()
                    print(f"Cliente '{self.name}' excluído com sucesso!")
            except sqlite3.Error as error:
                print(f"Erro ao excluir cliente: {error}")
        else:
            print("Informe o ID do cliente para exclusão.")



class ClientsManager(Manager):
    def __init__(self):
        self.DAO = UsersDBDAO()

    def createClient(self):
        pass
    
    def register(self, user: Users):
        pass

    def view(self):
        pass
    
    def update(self):
        pass

    def delete(self):
        pass

'''
As funções precisam:
    criar conexão com banco de dados;
    criar cursor da conexão;
    executar comando;
    fazer o "commit" da ação;
    encerrar conexão com o banco de dados.

As interações com o banco de dados ocorrerão 
através das classes DAO
'''
