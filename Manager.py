from abc import ABC, abstractmethod
import sqlite3

class Manager(ABC):
    def __init__(self, nome_banco):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def view(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    def close_connection(self):
        self.conexao.close()

class GerenciadorCategorias(Manager):
    def register(self, descricao, sla):
        self.cursor.execute("INSERT INTO CategoriasProblema (Descricao, SLA) VALUES (?, ?)", (descricao, sla))
        self.conexao.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM CategoriasProblema")
        return self.cursor.fetchall()

    def update(self, id_categoria, nova_descricao, novo_sla):
        self.cursor.execute("UPDATE CategoriasProblema SET Descricao = ?, SLA = ? WHERE ID = ?", (nova_descricao, novo_sla, id_categoria))
        self.conexao.commit()

    def delete(self, id_categoria):
        self.cursor.execute("DELETE FROM CategoriasProblema WHERE ID = ?", (id_categoria,))
        self.conexao.commit()

    def associate_sla(self, id_categoria, tempo_sla):
        self.cursor.execute("INSERT INTO SLA (CategoriaID, Tempo) VALUES (?, ?)", (id_categoria, tempo_sla))
        self.conexao.commit()

    def get_sla(self, id_categoria):
        self.cursor.execute("SELECT Tempo FROM SLA WHERE CategoriaID = ?", (id_categoria,))
        return self.cursor.fetchone()

