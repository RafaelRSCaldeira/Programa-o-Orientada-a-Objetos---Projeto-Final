import datetime

class Ticket:
    def __init__(self, id, title, description, category, client_id, user_id, status, opening_date, max_date, closing_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.client_id = client_id
        self.user_id = user_id
        self.status = status
        self.opening_date = opening_date
        self.max_date = max_date
        self.closing_date = closing_date

    def open(self):
        # Simula a abertura de um chamado e salva no banco de dados
        print(f"Chamado '{self.title}' aberto.")
        # Aqui você iria interagir com o banco de dados

    def assignUser(self, user_id):
        self.user_id = user_id
        print(f"Usuário {user_id} atribuído ao chamado '{self.title}'.")
        # Aqui você iria atualizar o banco de dados

    def changeStatus(self, status):
        self.status = status
        print(f"Status do chamado '{self.title}' alterado para '{status}'.")
        # Aqui você iria atualizar o banco de dados

    def close(self):
        self.status = 'fechado'
        self.closing_date = datetime.datetime.now()
        print(f"Chamado '{self.title}' fechado.")
        # Aqui você iria atualizar o banco de dados

    def view(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'client_id': self.client_id,
            'user_id': self.user_id,
            'status': self.status,
            'opening_date': self.opening_date,
            'max_date': self.max_date,
            'closing_date': self.closing_date
        }

    def update(self, title=None, description=None, category=None, client_id=None, user_id=None, status=None, max_date=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if category:
            self.category = category
        if client_id:
            self.client_id = client_id
        if user_id:
            self.user_id = user_id
        if status:
            self.status = status
        if max_date:
            self.max_date = max_date
        print(f"Chamado '{self.title}' atualizado.")
        # Aqui você iria atualizar o banco de dados

    def delete(self):
        print(f"Chamado '{self.title}' deletado.")
        # Aqui você iria deletar o chamado do banco de dados

# Simulação de banco de dados
tickets_db = []

def list_tickets_by_status(status):
    result = [ticket.view() for ticket in tickets_db if ticket.status == status]
    for ticket in result:
        print(ticket)

# Exemplo de uso
ticket1 = Ticket(1, 'Problema de Rede', 'Internet não está funcionando', 'Rede', 101, None, 'aberto', datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=2))
ticket2 = Ticket(2, 'Problema na Impressora', 'Impressora não está funcionando', 'Hardware', 102, None, 'aberto', datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=2))
ticket3 = Ticket(3, 'Atualização de Software', 'Necessário atualizar software', 'Software', 103, None, 'fechado', datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=2), datetime.datetime.now())

# Adicionando chamados ao banco de dados simulado
tickets_db.extend([ticket1, ticket2, ticket3])

# Abrir um chamado
ticket1.open()

# Atribuir um usuário a um chamado
ticket1.assignUser(201)

# Alterar o status de um chamado
ticket1.changeStatus('em progresso')

# Fechar um chamado
ticket1.close()

# Atualizar um chamado
ticket1.update(description='Internet não está funcionando corretamente')

# Deletar um chamado
ticket1.delete()

# Listar chamados por status
print("Chamados abertos:")
list_tickets_by_status('aberto')

print("Chamados fechados:")
list_tickets_by_status('fechado')