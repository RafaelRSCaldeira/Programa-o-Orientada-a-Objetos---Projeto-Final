from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import Image
from abc import ABC
from Users import *
from Clients import *
from Problems import *
from Calls import *

class MainWindow(ABC):
    '''Janela principal do sistema de gestão'''
    def __init__(self, parent : Widget, user) -> None:
        #Criar Janela Principal
        self.window = Toplevel(parent)
        self.window.title("Menu - Sistema Integrado de Gestão Empresarial")
        #Definir geometria padrão
        self.width = 800
        self.height = 450
        self.window.geometry(f"{self.width}x{self.height}")

class MainWindowSpecial(MainWindow):
    ''''Janela para Atendentes/Técnicos'''
    def __init__(self, parent : Widget, user : Users) -> None:
        super().__init__(parent, user)
        self.CategorySelectorFrame = Frame(self.window)
        self.CategorySelectorFrame.pack(side = 'top', anchor = 'w', ipady = 10)
        #Criar o Menu para seleção de item
        self.selectedCategory = StringVar(value = 'users')
        self.usersSelectorButton = Radiobutton(self.CategorySelectorFrame, indicatoron = False, text = 'Usuários', variable = self.selectedCategory, value = 'users', command = self.listUsers)
        self.clientsSelectorButton = Radiobutton(self.CategorySelectorFrame, indicatoron = False, text = 'Clientes', variable = self.selectedCategory, value = 'clients', command = self.listClients)
        self.problemsSelectorButton = Radiobutton(self.CategorySelectorFrame, indicatoron = False, text = 'Categorias de problemas', variable = self.selectedCategory, value = 'problems', command = self.listProblems)
        self.callsSelectorButton = Radiobutton(self.CategorySelectorFrame, indicatoron = False, text = 'Chamados', variable = self.selectedCategory, value = 'calls', command = self.listAllCalls)
        #Posicionar o Menu para seleção de itme
        self.usersSelectorButton.grid(row = 0, column = 0)
        self.clientsSelectorButton.grid(row = 0, column = 1)
        self.problemsSelectorButton.grid(row = 0, column = 2)
        self.callsSelectorButton.grid(row = 0, column = 3)
        #Criar o Frame para colocar a Lista e o Scroll
        self.listFrame = Frame(self.window)
        self.listFrame.pack(fill = 'both', expand = True)
        #Criar e configurar Scroll e Lista
        self.scrollbar = Scrollbar(self.listFrame, orient="vertical")
        self.listbox = Listbox(self.listFrame, width=50, height=1, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        #Posicionar Scroll e Lista
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.pack(side="left",fill="both", expand=True)
        #Criar Frame para os botões de adicionar, remover, visualizar e editar
        self.buttonsFrame = Frame(self.window)
        self.buttonsFrame.pack(side = 'left', ipady = 5)
        #Criar os botões de adicionar, remover, visualizar e editar
        self.addButton = Button(self.buttonsFrame, text = 'Adicionar', command = self.addItem)
        self.removeButton = Button(self.buttonsFrame, text = 'Remover', command = self.removeItem)
        self.visualizeButton = Button(self.buttonsFrame, text = 'Visualizar', command = self.visualizeItem)
        self.editButton = Button(self.buttonsFrame, text = 'Editar', command = self.editItem)
        #Posicionar os botões de adicionar, remover, visualizar e editar
        self.addButton.grid(column = 0, row = 0)
        self.removeButton.grid(column = 1, row = 0)
        self.visualizeButton.grid(column = 2, row = 0)
        self.editButton.grid(column = 3, row = 0)
        #Criar o frame para colocar os botões de filtro de chamados
        self.filterButtonFrame = Frame(self.window)
        #Criar os botões de filtro de chamados
        self.statusFilter = StringVar()
        self.statusFilter.set('all')
        self.filterButtonAll = Radiobutton(self.filterButtonFrame, variable = self.statusFilter, value = 'all', text = 'Todos', command = self.listAllCalls)
        self.filterButtonOpen = Radiobutton(self.filterButtonFrame, variable = self.statusFilter, value = 'open', text = 'Abertos', command = self.listOpenCalls)
        self.filterButtonClosed = Radiobutton(self.filterButtonFrame, variable = self.statusFilter, value = 'closed', text = 'Fechados', command = self.listClosedCalls)
        self.filterButtonInService = Radiobutton(self.filterButtonFrame, variable = self.statusFilter, value = 'in service', text = 'Em atendimento', command = self.listInServiceCalls)
        #Posicionar os botões de filtros de chamados dentro do frame
        self.filterButtonAll.grid(row = 0, column = 0)
        self.filterButtonOpen.grid(row = 0, column = 1)
        self.filterButtonClosed.grid(row = 0, column = 2)
        self.filterButtonInService.grid(row = 0, column = 3)
        #Criar manager
        self.usersManager = UsersManager('manager.db')
        self.clientsManager = ClientsManager('manager.db')
        self.callsManager = CallsManager('manager.db')
        self.problemsManager = ProblemsManager('manager.db')
        #Mostrar usuários como padrão quando iniciar a janela
        self.listUsers()
    #Mostrar a lista de usuários
    def listUsers(self) -> None:
        self.filterButtonFrame.pack_forget()
        self.listbox.delete(0, 'end')
        self.usersIdList = self.usersManager.getAllIds()
        for userId in self.usersIdList:
            userInfo = self.usersManager.getByID(userId)
            self.listbox.insert('end', f"{userInfo.id} - {userInfo.name}")

    #Mostrar a lista de clientes
    def listClients(self) -> None:
        self.filterButtonFrame.pack_forget()
        self.listbox.delete(0, 'end')
        self.clientsIdList = self.clientsManager.getAllIds()
        for clientId in self.clientsIdList:
            clientInfo = self.clientsManager.getByID(clientId)
            self.listbox.insert('end', f"{clientInfo.id} - {clientInfo.name}")

    #Mostrar a lista de Categorias de problemas
    def listProblems(self) -> None:
        self.filterButtonFrame.pack_forget()
        self.listbox.delete(0, 'end')
        self.problemsIdList = self.problemsManager.getAllIds()
        for problemId in self.problemsIdList:
            problemInfo = self.problemsManager.getByID(problemId)
            self.listbox.insert('end', f"{problemInfo.id} - {problemInfo.sla}")

    #Mostrar a lista de todos os chamados
    def listAllCalls(self) -> None:
        self.filterButtonFrame.pack(before = self.listFrame, side = 'top', anchor = 'w')  
        self.listbox.delete(0, 'end') 
        self.callsIdList = self.callsManager.getAllIds()
        for callId in self.callsIdList:
            callInfo = self.callsManager.getByID(callId)
            self.listbox.insert('end', f"{callInfo.id} - {callInfo.title}")

    #Mostrar a lista de chamados abertos
    def listOpenCalls(self) -> None:
        self.filterButtonFrame.pack(before = self.listFrame, side = 'top', anchor = 'w')  
        self.listbox.delete(0, 'end') 
        self.callsIdList = self.callsManager.getAllIds()
        for callId in self.callsIdList:
            callInfo = self.callsManager.getByID(callId)
            if callInfo.status == 'open':
                self.listbox.insert('end', f"{callInfo.id} - {callInfo.title}")

    #Mostrar a lista de chamados fechados
    def listClosedCalls(self) -> None:
        self.filterButtonFrame.pack(before = self.listFrame, side = 'top', anchor = 'w')  
        self.listbox.delete(0, 'end') 
        self.callsIdList = self.callsManager.getAllIds()
        for callId in self.callsIdList:
            callInfo = self.callsManager.getByID(callId)
            if callInfo.status == 'closed':
                self.listbox.insert('end', f"{callInfo.id} - {callInfo.title}")

    #Mostrar a lista de chamados em atendimento
    def listInServiceCalls(self) -> None:
        self.filterButtonFrame.pack(before = self.listFrame, side = 'top', anchor = 'w')  
        self.listbox.delete(0, 'end') 
        self.callsIdList = self.callsManager.getAllIds()
        for callId in self.callsIdList:
            callInfo = self.callsManager.getByID(callId)
            if callInfo.status == 'ongoing':
                self.listbox.insert('end', f"{callInfo.id} - {callInfo.title}")
    
    def addItem(self) -> None:
        if self.selectedCategory.get() == 'users':
            UserAdder(self.window, self.refresh)
        elif self.selectedCategory.get() == 'clients':
            ClientAdder(self.window, self.refresh)
        elif self.selectedCategory.get() == 'problems':
            ProblemsAdder(self.window, self.refresh)
        elif self.selectedCategory.get() == 'calls':
            CallsAdder(self.window, self.refresh)

    def removeItem(self) -> None:
        self.itemInfo = self.listbox.get(ANCHOR).split()
        if(len(self.itemInfo) == 0):
            return
        self.itemId = self.itemInfo[0]
        if self.selectedCategory.get() == 'users':
            listBoxAnchor = self.listbox.get(ANCHOR)
            self.listbox.delete(ANCHOR)
            self.usersManager.delete(self.itemId)
            print(f'{listBoxAnchor} removido')
        elif self.selectedCategory.get() == 'clients':
            listBoxAnchor = self.listbox.get(ANCHOR)
            self.listbox.delete(ANCHOR)
            self.clientsManager.delete(self.itemId)
            print(f'{listBoxAnchor} removido')
        elif self.selectedCategory.get() == 'problems':
            listBoxAnchor = self.listbox.get(ANCHOR)
            self.listbox.delete(ANCHOR)
            self.problemsManager.delete(self.itemId)
            print(f'{listBoxAnchor} removido')
        elif self.selectedCategory.get() == 'calls':
            listBoxAnchor = self.listbox.get(ANCHOR)
            self.listbox.delete(ANCHOR)
            self.callsManager.delete(self.itemId)
            print(f'{listBoxAnchor} removido')

    def visualizeItem(self) -> None:
        self.itemInfo = self.listbox.get(ANCHOR).split()
        if(len(self.itemInfo) == 0):
            return
        self.itemId = self.itemInfo[0]
        if self.selectedCategory.get() == 'users':
            UserVisualizer(self.window, self.itemId)
        elif self.selectedCategory.get() == 'clients':
            ClientVisualizer(self.window, self.itemId)
        elif self.selectedCategory.get() == 'problems':
            ProblemVisualizer(self.window, self.itemId)
        elif self.selectedCategory.get() == 'calls':
            CallVisualizer(self.window, self.itemId)

    def editItem(self) -> None:
        self.itemInfo = self.listbox.get(ANCHOR).split()
        if(len(self.itemInfo) == 0):
            return
        self.itemId = self.itemInfo[0]
        if self.selectedCategory.get() == 'users':
            UserEditer(self.window, self.itemId, self.refresh)
        elif self.selectedCategory.get() == 'clients':
            ClientEditer(self.window, self.itemId, self.refresh)
        elif self.selectedCategory.get() == 'problems':
            ProblemsEditer(self.window, self.itemId, self.refresh)
        elif self.selectedCategory.get() == 'calls':
            CallsEditer(self.window, self.itemId, self.refresh)
    
    def refresh(self) -> None:
        print
        if self.selectedCategory.get() == 'users':
            self.listUsers()
        elif self.selectedCategory.get() == 'clients':
            self.listClients()
        elif self.selectedCategory.get() == 'problems':
            self.listProblems()
        elif self.selectedCategory.get() == 'calls':
            if self.statusFilter.get() == 'all':
                self.listAllCalls()
            elif self.statusFilter.get() == 'closed':
                self.listClosedCalls()
            elif self.statusFilter.get() == 'open':
                self.listOpenCalls()
            elif self.statusFilter.get() == 'in service':
                self.listInServiceCalls()
            


class UserAdder():
    def __init__(self, parent : Widget, callback = ()) -> None:
        self.callback = callback
        #Criar a janela
        self.window = Toplevel(parent)
        #Definir geometria padrão
        self.width = 200
        self.height = 330
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)      
        self.window.title("Adicionar usuário")
        #Criar as entradas
        self.nameEntry = CTkEntry(self.window, placeholder_text='Nome', width = 160, fg_color = "White", text_color = "Black")
        self.emailEntry = CTkEntry(self.window, placeholder_text='Email', width = 160, fg_color = "White", text_color = "Black")
        self.passwordEntry = CTkEntry(self.window, placeholder_text='Senha', width = 160, fg_color = "White", text_color = "Black", show = '*')
        self.positionEntry = CTkEntry(self.window, placeholder_text='Cargo', width = 160, fg_color = "White", text_color = "Black")
        #Posicionar as entradas
        self.nameEntry.grid(column = 0, row = 1, pady = 20, padx = 20)
        self.emailEntry.grid(column = 0, row = 2, pady = 0, padx = 20)
        self.passwordEntry.grid(column = 0, row = 3, pady = 20, padx = 20)
        self.positionEntry.grid(column = 0, row = 4, pady = 0, padx = 20)
        #Criar e posicionar o botão
        self.addButton = CTkButton(self.window, text = 'Adicionar', command = self.add)
        self.addButton.grid(column = 0, row = 5, pady = 40)
    
    def add(self) -> None:
        #Criar um objeto usuário à partir dos dados fornecidos
        user = Users('self.idEntry.get()',
                     self.nameEntry.get(),
                     self.emailEntry.get(),
                     self.passwordEntry.get(), 
                     self.positionEntry.get())
        usersManager = UsersManager("manager.db")
        #Registrar o usuário no banco de dados se todos os campos foram preenchidos
        if user.id != '' and user.name != '' and user.email != '' and user.password != '' and user.position != '':
            usersManager.register(user)
            self.window.withdraw()
            self.callback()
        else:
            #Criar mensagem de erro
            messagebox.showwarning('Inválido', "Todos os campos devem ser preenchidos.")           

class ClientAdder():
    def __init__(self, parent : Widget, callback = ()) -> None:
        self.callback = callback
        #Criar a janela
        self.window = Toplevel(parent)
        #Definir geometria padrão
        self.width = 200
        self.height = 330
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)      
        self.window.title("Adicionar cliente")
        #Criar as entradas
        self.nameEntry = CTkEntry(self.window, placeholder_text='Nome', width = 160, fg_color = "White", text_color = "Black")
        self.emailEntry = CTkEntry(self.window, placeholder_text='Email', width = 160, fg_color = "White", text_color = "Black")
        self.passwordEntry = CTkEntry(self.window, placeholder_text='Senha', width = 160, fg_color = "White", text_color = "Black", show = '*')
        self.companyEntry = CTkEntry(self.window, placeholder_text='Empresa', width = 160, fg_color = "White", text_color = "Black")
        self.phoneEntry = CTkEntry(self.window, placeholder_text='Telefone', width = 160, fg_color = "White", text_color = "Black")
        #Posicionar as entradas
        self.nameEntry.grid(column = 0, row = 0, pady = 20, padx = 20)
        self.emailEntry.grid(column = 0, row = 1, pady = 0, padx = 20)
        self.passwordEntry.grid(column = 0, row = 2, pady = 20, padx = 20)
        self.companyEntry.grid(column = 0, row = 3, pady = 0, padx = 20)
        self.phoneEntry.grid(column = 0, row = 4, pady = 20, padx = 20)
        #Criar e posicionar o botão
        self.addButton = CTkButton(self.window, text = 'Adicionar', command = self.add)
        self.addButton.grid(column = 0, row = 5, pady = 20)
    
    def add(self) -> None:
        #Criar um objeto cliente à partir dos dados fornecidos
        client = Clients('self.idEntry.get()',
                     self.nameEntry.get(),
                     self.emailEntry.get(),
                     self.passwordEntry.get(),
                     self.companyEntry.get(), 
                     self.phoneEntry.get())
        clientsManager = ClientsManager('manager.db')
        #Registrar o cliente no banco de dados se todos os campos foram preenchidos
        if client.id != '' and client.name != '' and client.email != '' and client.password != '' and client.company != '' and client.phone != '':
            clientsManager.register(client)
            self.window.withdraw()
            self.callback()
        else:
            #Criar mensagem de erro
            messagebox.showwarning('Inválido', "Todos os campos devem ser preenchidos.")           

class ProblemsAdder():
    def __init__(self, parent : Widget, callback = ()) -> None:
        self.callback = callback
        #Criar a janela
        self.window = Toplevel(parent)
        #Definir geometria padrão
        self.width = 400
        self.height = 330
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)      
        self.window.title("Adicionar categoria de problema")
        #Criar as entradas
        self.slaEntry = CTkEntry(self.window, placeholder_text='SLA', width = 360, fg_color = "White", text_color = "Black")
        self.descriptionEntry = CTkTextbox(self.window, width = 360, fg_color = "White", text_color = "Black", height = 100)
        self.descriptionEntry.insert('insert', 'Descrição')
        #Posicionar as entradas
        self.slaEntry.grid(column = 0, row = 1, pady = 20, padx = 20)
        self.descriptionEntry.grid(column = 0, row = 2, pady = 0, padx = 20)
        #Criar e posicionar o botão
        self.addButton = CTkButton(self.window, text = 'Adicionar', command = self.add)
        self.addButton.grid(column = 0, row = 5, pady = 40)
    
    def add(self) -> None:
        #Criar um objeto problema à partir dos dados fornecidos
        problem = Problems('self.idEntry.get()',
                     self.descriptionEntry.get(0.0, 'end').strip('\n'),
                     self.slaEntry.get(),
                     )
        problemsManager = ProblemsManager('manager.db')
        #Registrar o problema no banco de dados se todos os campos foram preenchidos
        if problem.id != '' and problem.description != '' and problem.sla != '':
            problemsManager.register(problem)
            self.window.withdraw()
            self.callback()
        else:
            #Criar mensagem de erro
            messagebox.showwarning('Inválido', "Todos os campos devem ser preenchidos.")           

class UserEditer():
    def __init__(self, parent : Widget, userId : int, callback = ()) -> None:
        self.callback = callback
        #Criar a janela
        self.window = Toplevel(parent)
        #Definir geometria padrão
        self.width = 200
        self.height = 330
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)      
        self.window.title("Editar informações de usuário")
        #criar um manager
        self.usersManager = UsersManager("manager.db")
        self.user = self.usersManager.getByID(userId)
        #salvar os dados antigos
        self.userId = userId
        #Criar as entradas
        self.idLabel = CTkLabel(self.window, text = self.userId, width = 160, fg_color = "White", text_color = "Black")
        self.nameEntry = CTkEntry(self.window, placeholder_text="Nome", width = 160, fg_color = "White", text_color = "Black")
        self.emailEntry = CTkEntry(self.window, placeholder_text="Email", width = 160, fg_color = "White", text_color = "Black")
        self.passwordEntry = CTkEntry(self.window, placeholder_text="Senha", width = 160, fg_color = "White", text_color = "Black", show = '*')
        self.positionEntry = CTkEntry(self.window, placeholder_text="Posição", width = 160, fg_color = "White", text_color = "Black")
        self.nameEntry.insert(0, self.user.name)
        self.emailEntry.insert(0, self.user.email)
        self.passwordEntry.insert(0, self.user.password)
        self.positionEntry.insert(0, self.user.position)
        #Posicionar as entradas
        self.idLabel.grid(column = 0, row = 0, pady = 20, padx = 20)
        self.nameEntry.grid(column = 0, row = 1, pady = 0, padx = 20)
        self.emailEntry.grid(column = 0, row = 2, pady = 20, padx = 20)
        self.passwordEntry.grid(column = 0, row = 3, pady = 0, padx = 20)
        self.positionEntry.grid(column = 0, row = 4, pady = 20, padx = 20)
        #Criar e posicionar o botão
        self.editButton = CTkButton(self.window, text = 'Alterar', command = self.edit)
        self.editButton.grid(column = 0, row = 5, pady = 20)
    
    def edit(self) -> None:
        #Criar variáveis temporárias para armazenar as informações novas
        newName = self.nameEntry.get()
        newEmail = self.emailEntry.get()
        newPassword = self.passwordEntry.get()
        newPosition = self.positionEntry.get()
        newUserInfo = Users(self.userId, newName, newEmail, newPassword, newPosition)
        #Registrar o usuário no banco de dados se todos os campos foram preenchidos
        if newName != '' and newEmail != '' and newPassword != '' and newPosition != '':
            self.usersManager.update(newUserInfo)
            self.window.withdraw()
            self.callback()
        else:
            #Criar mensagem de erro
            messagebox.showwarning('Inválido', "Todos os campos devem ser preenchidos.")      

class ClientEditer():
    def __init__(self, parent : Widget, clientId : int, callback = ()) -> None:
        self.callback = callback
        #Criar a janela
        self.window = Toplevel(parent)
        #Definir geometria padrão
        self.width = 200
        self.height = 360
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)      
        self.window.title("Editar cliente")
        #criar um manager
        self.clientsManager = ClientsManager("manager.db")
        self.client = self.clientsManager.getByID(clientId)
        #salvar os dados antigos
        self.clientId = clientId
        #Criar as entradas
        self.idLabel = CTkLabel(self.window, text = self.clientId, width = 160, fg_color = "White", text_color = "Black")
        self.nameEntry = CTkEntry(self.window, placeholder_text = "Nome", width = 160, fg_color = "White", text_color = "Black")
        self.emailEntry = CTkEntry(self.window, placeholder_text = "Email", width = 160, fg_color = "White", text_color = "Black")
        self.passwordEntry = CTkEntry(self.window, placeholder_text = "Senha", width = 160, fg_color = "White", text_color = "Black", show = '*')
        self.companyEntry = CTkEntry(self.window, placeholder_text = "Empresa", width = 160, fg_color = "White", text_color = "Black")
        self.phoneEntry = CTkEntry(self.window, placeholder_text =  "Telefone", width = 160, fg_color = "White", text_color = "Black")
        self.nameEntry.insert(0, self.client.name)
        self.emailEntry.insert(0, self.client.email)
        self.passwordEntry.insert(0, self.client.password)
        self.companyEntry.insert(0, self.client.company)
        self.phoneEntry.insert(0, self.client.phone)
        #Posicionar as entradas
        self.idLabel.grid(column = 0, row = 0, pady = 20, padx = 20)
        self.nameEntry.grid(column = 0, row = 1, pady = 0, padx = 20)
        self.emailEntry.grid(column = 0, row = 2, pady = 20, padx = 20)
        self.passwordEntry.grid(column = 0, row = 3, pady = 0, padx = 20)
        self.companyEntry.grid(column = 0, row = 4, pady = 20, padx = 20)
        self.phoneEntry.grid(column = 0, row = 5, pady = 0, padx = 20)
        #Criar e posicionar o botão
        self.editButton = CTkButton(self.window, text = 'Alterar', command = self.edit)
        self.editButton.grid(column = 0, row = 6, pady = 40)
    
    def edit(self) -> None:
        #Criar variáveis temporárias para armazenar as informações novas
        newName = self.nameEntry.get()
        newEmail = self.emailEntry.get()
        newPassword = self.passwordEntry.get()
        newCompany = self.companyEntry.get()
        newPhone = self.phoneEntry.get()
        newClientInfo = Clients(self.clientId, newName, newEmail, newPassword, newCompany, newPhone)
        #Registrar o cliente no banco de dados se todos os campos foram preenchidos
        if newName != '' and newEmail != '' and newPassword != '' and newCompany != '' and newPhone != '':
            self.clientsManager.update(newClientInfo)
            self.window.withdraw()
            self.callback()
        else:
            #Criar mensagem de erro
            messagebox.showwarning('Inválido', "Todos os campos devem ser preenchidos.")  

class ProblemsEditer():
    def __init__(self, parent : Widget, problemId : int, callback = ()) -> None:
        self.callback = callback
        #Criar a janela
        self.window = Toplevel(parent)
        #Definir geometria padrão
        self.width = 400
        self.height = 330
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)      
        self.window.title("Editar categoria de problema")
        #criar um manager
        self.problemsManager = ProblemsManager("manager.db")
        self.problem = self.problemsManager.getByID(problemId)
        #salvar os dados antigos
        self.problemId = problemId
        #Criar as entradas
        self.idLabel = CTkLabel(self.window, text=self.problemId, width = 360, fg_color = "White", text_color = "Black")
        self.slaEntry = CTkEntry(self.window, placeholder_text="SLA", width = 360, fg_color = "White", text_color = "Black")
        self.descriptionEntry = CTkTextbox(self.window, width = 360, fg_color = "White", text_color = "Black", height = 100)
        self.slaEntry.insert(0, self.problem.sla)
        self.descriptionEntry.insert('insert', self.problem.description)
        #Posicionar as entradas
        self.idLabel.grid(column = 0, row = 0, pady = 20, padx = 20)
        self.slaEntry.grid(column = 0, row = 1, pady = 0, padx = 20)
        self.descriptionEntry.grid(column = 0, row = 2, pady = 20, padx = 20)
        #Criar e posicionar o botão
        self.editButton = CTkButton(self.window, text = 'Alterar', command = self.edit)
        self.editButton.grid(column = 0, row = 5, pady = 20)
 
    def edit(self) -> None:
        #Criar variáveis temporárias para armazenar as informações novas
        newSla = self.slaEntry.get()
        newDescription = self.descriptionEntry.get(0.0, 'end').strip('\n')
        newProblemInfo = Problems(self.problemId, newDescription, newSla)
        #Registrar o cliente no banco de dados se todos os campos foram preenchidos
        if newSla != '' and newDescription != '':
            self.problemsManager.update(newProblemInfo)
            self.window.withdraw()
            self.callback()
        else:
            #Criar mensagem de erro
            messagebox.showwarning('Inválido', "Todos os campos devem ser preenchidos.")  

class CallsEditer():
    def __init__(self, parent : Widget, callId : int, callback = ()) -> None:
        self.callback = callback
        #Criar a janela
        self.window = Toplevel(parent)
        #Definir geometria padrão
        self.width = 400
        self.height = 735
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)      
        self.window.title("Editar chamado")
        #criar um manager
        self.callsManager = CallsManager("manager.db")
        self.call = self.callsManager.getByID(callId)
        #salvar os dados antigos
        self.callId = callId
        #Criar as entradas
        self.idLabel = CTkLabel(self.window, text=self.callId, width = 360, fg_color = "White", text_color = "Black")
        self.titleEntry = CTkEntry(self.window, placeholder_text="Titulo", width = 360, fg_color = "White", text_color = "Black")
        self.categoryEntry = CTkEntry(self.window, placeholder_text="Categoria", width = 360, fg_color = "White", text_color = "Black")
        self.statusEntry = CTkEntry(self.window, placeholder_text="Status", width = 360, fg_color = "White", text_color = "Black")
        self.clientIdEntry = CTkEntry(self.window, placeholder_text="Client ID", width = 360, fg_color = "White", text_color = "Black")
        self.userIdEntry = CTkEntry(self.window, placeholder_text="User ID", width = 360, fg_color = "White", text_color = "Black")
        self.openingDateEntry = CTkEntry(self.window, placeholder_text="Data de abertura", width = 360, fg_color = "White", text_color = "Black")
        self.maxDateEntry = CTkEntry(self.window, placeholder_text="Data máxima", width = 360, fg_color = "White", text_color = "Black")
        self.closingDateEntry = CTkEntry(self.window, placeholder_text="Data de fechamento", width = 360, fg_color = "White", text_color = "Black")
        self.descriptionEntry = CTkTextbox(self.window, width = 360, fg_color = "White", text_color = "Black", height = 100)
        self.feedbackEntry = CTkTextbox(self.window, width = 360, fg_color = "White", text_color = "Black", height = 100)
        self.titleEntry.insert(0, self.call.title)
        self.categoryEntry.insert(0, self.call.category)
        self.statusEntry.insert(0, self.call.status)
        self.clientIdEntry.insert(0, self.call.clientID)
        if(self.call.userID):
            self.userIdEntry.insert(0, self.call.userID)
        self.openingDateEntry.insert(0, self.call.openingDate)
        self.maxDateEntry.insert(0, self.call.maxDate)
        self.closingDateEntry.insert(0, self.call.closingDate)
        self.descriptionEntry.insert('insert', self.call.description)
        if(self.call.feedback == ''):
            self.feedbackEntry.insert('insert', 'Sem feedback')
        else:
            self.feedbackEntry.insert('insert', self.call.feedback)
        #Posicionar as entradas
        self.idLabel.grid(column = 0, row = 0, pady = 20, padx = 20)
        self.titleEntry.grid(column = 0, row = 1, pady = 0, padx = 20)
        self.categoryEntry.grid(column = 0, row = 2, pady = 20, padx = 20)
        self.statusEntry.grid(column = 0, row = 3, pady = 0, padx = 20)
        self.clientIdEntry.grid(column = 0, row = 4, pady = 20, padx = 20)
        self.userIdEntry.grid(column = 0, row = 5, pady = 0, padx = 20)
        self.openingDateEntry.grid(column = 0, row = 6, pady = 20, padx = 20)
        self.maxDateEntry.grid(column = 0, row = 7, pady = 0, padx = 20)
        self.closingDateEntry.grid(column = 0, row = 8, pady = 20, padx = 20)
        self.descriptionEntry.grid(column = 0, row = 9, pady = 0, padx = 20)
        self.feedbackEntry.grid(column = 0, row = 10, pady = 20, padx = 20)
        #Criar e posicionar o botão
        self.editButton = CTkButton(self.window, text = 'Alterar', command = self.edit)
        self.editButton.grid(column = 0, row = 11, pady = 10)
 
    def edit(self) -> None:
        #Criar variáveis temporárias para armazenar as informações novas
        newTitle = self.titleEntry.get()
        newCategory = self.categoryEntry.get()
        newStatus = self.statusEntry.get()
        newClientId = self.clientIdEntry.get()
        newUserId = self.userIdEntry.get()
        newOpeningDate = self.openingDateEntry.get()
        newMaxDate = self.maxDateEntry.get()
        newClosingDate = self.closingDateEntry.get()
        newDescription = self.descriptionEntry.get(0.0, 'end').strip('\n')
        newFeedback = self.feedbackEntry.get(0.0, 'end').strip('\n')
        newCallInfo = Calls(self.callId, newTitle, newDescription, newCategory, newClientId, newUserId, newStatus, newOpeningDate, newClosingDate, newMaxDate, newFeedback)
        #Registrar o cliente no banco de dados se todos os campos foram preenchidos
        if newTitle != '' and newDescription != ''and newCategory != ''and newStatus != ''and newClientId != '' and newOpeningDate != ''and newMaxDate != '':
            self.callsManager.update(newCallInfo)
            self.window.withdraw()
            self.callback()
        else:
            #Criar mensagem de erro
            messagebox.showwarning('Inválido', "Todos os campos exceto UserID e ClosingDate devem ser preenchidos.")  

class UserVisualizer():
    '''Janela para visualizar um Chamado'''
    def __init__(self, parent : Widget, userId : int) -> None:
        #criar um manager
        self.usersManager = UsersManager("manager.db")
        self.user = self.usersManager.getByID(userId)
        #Salvar dados do Usuário
        self.userId = userId
        self.name = self.user.name
        self.email = self.user.email
        self.password = self.user.password
        self.position = self.user.position
        #Criar Janela
        self.window = Toplevel(parent)
        self.window.title(f"{self.userId} - {self.name}")
        #Definir geometria padrão
        self.width = 600
        self.height = 300
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)       
        #Cria o frame para o nome
        self.nameFrame = Frame(self.window)
        #Criar Label para nome
        self.nameLabel = CTkLabel(self.nameFrame, height=23, text=self.name, text_color='Black', font=("Arial", 20), justify='center')
        #Posicionar nome no frame
        self.nameLabel.pack() 
        #Posicionar Frame
        self.nameFrame.pack(fill='x', pady=5)
        #Criar Frames para as informações
        self.infoFrame = CTkFrame(self.window, bg_color= 'transparent', fg_color='transparent')
        #Criar infromações
        self.emailLabel = CTkLabel(self.infoFrame, height=23, text=f"Email: {self.email}", text_color='Black', font=("Arial", 16), justify='left')
        self.passwordLabel = CTkLabel(self.infoFrame, height=23, text=f"Senha: {self.password}", text_color='Black', font=("Arial", 16), justify='left')
        self.positionLabel = CTkLabel(self.infoFrame, height=23, text=f"Cargo: {self.position}", text_color='Black', font=("Arial", 16), justify='left')
        #Posicionar informações
        self.emailLabel.grid(row=0, column=0, sticky='W', pady = 20)
        self.passwordLabel.grid(row=1, column=0, sticky='W', pady = 20)
        self.positionLabel.grid(row=2, column=0, sticky='W', pady = 20)
        #Posicionar textframe
        self.infoFrame.pack(fill='x', pady = 15, padx = 30)

class ClientVisualizer():
    '''Janela para visualizar um Chamado'''
    def __init__(self, parent : Widget, clientId : int) -> None:
        #criar um manager
        self.clientsManager = ClientsManager("manager.db")
        self.client = self.clientsManager.getByID(clientId)
        #salvar os dados do usuário
        self.clientId = clientId
        self.name = self.client.name
        self.email = self.client.email
        self.password = self.client.password
        self.company = self.client.company
        self.phone = self.client.phone
        #Criar Janela
        self.window = Toplevel(parent)
        self.window.title(f"{self.clientId} - {self.name}")
        #Definir geometria padrão
        self.width = 600
        self.height = 300
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)
        
        #Cria o frame para o nome
        self.nameFrame = Frame(self.window)
        #Criar Label para nome
        self.nameLabel = CTkLabel(self.nameFrame, height=23, text=self.name, text_color='Black', font=("Arial", 20), justify='center')
        #Posicionar nome no frame
        self.nameLabel.pack() 
        #Posicionar Frame
        self.nameFrame.pack(fill='x', pady=5)
   
        #Criar Frames para as informações
        self.infoFrame = CTkFrame(self.window, bg_color= 'transparent', fg_color='transparent')
        #Criar infromações
        self.emailLabel = CTkLabel(self.infoFrame, height=23, text=f"Email: {self.email}", text_color='Black', font=("Arial", 16), justify='left')
        self.passwordLabel = CTkLabel(self.infoFrame, height=23, text=f"Senha: {self.password}", text_color='Black', font=("Arial", 16), justify='left')
        self.companyLabel = CTkLabel(self.infoFrame, height=23, text=f"Empresa: {self.company}", text_color='Black', font=("Arial", 16), justify='left')
        self.phoneLabel = CTkLabel(self.infoFrame, height=23, text=f"Telefone: {self.phone}", text_color='Black', font=("Arial", 16), justify='left')

        #Posicionar informações
        self.emailLabel.grid(row=0, column=0, sticky='W', pady = 15)
        self.passwordLabel.grid(row=1, column=0, sticky='W', pady = 15)
        self.companyLabel.grid(row=2, column=0, sticky='W', pady = 15)
        self.phoneLabel.grid(row=3, column=0, sticky='W', pady = 15)
        #Posicionar textframe
        self.infoFrame.pack(fill='x', pady = 15, padx = 30)

class ProblemVisualizer():
     def __init__(self, parent : Widget, problemId : int) -> None:
        #criar um manager
        self.problemsManager = ProblemsManager("manager.db")
        self.problem = self.problemsManager.getByID(problemId)
        #salvar os dados antigos
        self.problemId = problemId
        self.sla = self.problem.sla
        self.description = self.problem.description
        #Criar Janela
        self.window = Toplevel(parent)
        self.window.title(f"{self.problemId}")
        #Definir geometria padrão
        self.width = 600
        self.height = 300
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)
        #Criar Texto de descrição
        self.descriptionText = Text(self.window, borderwidth=5, height=9)
        #Inserir Texto
        self.descriptionText.insert(END, self.description)
        #Bloquear modificação
        self.descriptionText.config(state=DISABLED)
        #Colocar Texto
        self.descriptionText.pack(fill='x', pady=30)

        self.slaLabel = CTkLabel(self.window, justify = 'center', text = f'SLA: {self.sla}', text_color='Black', font=("Arial", 16))
        self.slaLabel.pack()

class CallsAdder():
    def __init__(self, parent : Widget, callback = (), client : Clients = None) -> None:
        self.client = client
        self.callback = callback
        #Criar a janela
        self.window = Toplevel(parent)
        #Definir geometria padrão
        self.width = 400
        self.height = 535
        if(not self.client):
            self.height = 535
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)      
        self.window.title("Criar chamado")
        #Criar as entradas
        self.titleEntry = CTkEntry(self.window, placeholder_text="Titulo", width = 360, fg_color = "White", text_color = "Black")
        self.categoryEntry = CTkEntry(self.window, placeholder_text="Categoria", width = 360, fg_color = "White", text_color = "Black")
        self.clientIdEntry = CTkEntry(self.window, placeholder_text="ID Cliente", width = 360, fg_color = "White", text_color = "Black")
        self.maxDateEntry = CTkEntry(self.window, placeholder_text="Data Máxima", width = 360, fg_color = "White", text_color = "Black")
        self.descriptionEntry = CTkTextbox(self.window, width = 360, fg_color = "White", text_color = "Black", height = 100)
        self.descriptionEntry.insert('insert', "Descrição")
        self.editButton = CTkButton(self.window, text = 'Criar', command = self.add)
        #Posicionar as entradas
        self.titleEntry.grid(column = 0, row = 1, pady = 20, padx = 20)
        self.categoryEntry.grid(column = 0, row = 2, pady = 20, padx = 20)
        if(not self.client):
            self.clientIdEntry.grid(column = 0, row = 4, pady = 20, padx = 20)
            self.maxDateEntry.grid(column = 0, row = 5, pady = 20, padx = 20)
            self.descriptionEntry.grid(column = 0, row = 6, pady = 20, padx = 20)
            #Criar e posicionar o botão
            self.editButton.grid(column = 0, row = 7, pady = 40)
        else:
            self.maxDateEntry.grid(column = 0, row = 4, pady = 20, padx = 20)
            self.descriptionEntry.grid(column = 0, row = 5, pady = 20, padx = 20)
            #Criar e posicionar o botão
            self.editButton.grid(column = 0, row = 6, pady = 40)

    def add(self) -> None:
        #Criar um objeto usuário à partir dos dados fornecidos
        user = Calls(0,
                     self.titleEntry.get(),
                     self.descriptionEntry.get(0.0, 'end').strip('\n'),
                     self.categoryEntry.get(),
                     self.clientIdEntry.get(),
                     None,
                     "open",
                     str(datetime.datetime.now()),
                     "",
                     self.maxDateEntry.get(),
                     "")
        callsManager = CallsManager("manager.db")
        #Registrar o usuário no banco de dados se todos os campos foram preenchidos
        if user.title != '' and user.description != '' and user.category != '' and user.clientID != '' and user.maxDate != '':
            callsManager.open(user)
            self.window.withdraw()
            self.callback()
        else:
            #Criar mensagem de erro
            messagebox.showwarning('Inválido', "Todos os campos devem ser preenchidos.")     

class CallVisualizer():
    '''Janela para visualizar um Chamado'''
    def __init__(self, parent : Widget, call : str) -> None:
        #Salvar dados do Call
        self.callsManager = CallsManager('manager.db')
        self.callID = int(call.split(" - ")[0])
        self.call = self.callsManager.getByID(self.callID)
        #Criar Janela
        self.window = Toplevel(parent)
        self.window.title("ID - Titulo")
        #Definir geometria padrão
        self.width = 600
        self.height = 300
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)
        
        #Cria o frame para o titulo/cagoria e status
        self.titleFrame = Frame(self.window)
        #Frame para o titulo e categoria somente
        self.titleCategoryFrame = Frame(self.titleFrame)
        #Criar Label para titulo e categoria
        self.titleLabel = CTkLabel(self.titleCategoryFrame, height=23, text=self.call.title, text_color='Black', font=("Arial", 20), justify='center')
        self.categoryLabel = CTkLabel(self.titleCategoryFrame, height=23, text=self.call.category, text_color='Black', font=("Arial", 12), justify='center')
        #Posicionar titulo e categoria no frame
        self.titleLabel.pack() 
        self.categoryLabel.pack()
        #Criar Icone de status
        self.statusIcon = CTkFrame(self.titleFrame, 46, 46, 23, fg_color=self._getStatusColor())
        #Colocar Icone de status no frame
        self.statusIcon.pack(side=RIGHT, padx=5)
        #Colocar Frame no outro frame
        self.titleCategoryFrame.pack() 
        #Criar Frame Final
        self.titleFrame.pack(fill='x', pady=5)

        self.descFeedFrame = CTkFrame(self.window, bg_color= 'transparent', fg_color='transparent')
        #Criar Texto de descrição
        self.descriptionText = Text(self.descFeedFrame, borderwidth=5, height=9, width=32)
        self.feedbackText = Text(self.descFeedFrame, borderwidth=5, height=9, width=32)
        #Inserir Texto
        self.descriptionText.insert(END, self.call.description)
        self.feedbackText.insert(END, self.call.feedback)
        #Bloquear modificação
        self.descriptionText.config(state=DISABLED)
        self.feedbackText.config(state=DISABLED)
        #Colocar Texto
        self.descriptionText.pack(fill='x', side=LEFT, expand=True, padx=5)
        self.feedbackText.pack(fill='x', side=RIGHT, expand=True,padx=5)
        self.descFeedFrame.pack(fill='x', pady=10)
        
        #Criar Frames para os ids
        self.idsFrame = CTkFrame(self.window, bg_color= 'transparent', fg_color='transparent')
        self.textFrame = CTkFrame(self.idsFrame, bg_color= 'transparent', fg_color='transparent')
        #Criar IDs de atendente e cliente
        self.clientIDLabel = CTkLabel(self.textFrame, height=23, text=f"ID do Cliente: {self.call.clientID}", text_color='Black', font=("Arial", 16), justify='left')
        self.attendantIDLabel = CTkLabel(self.textFrame, height=23, text=f"ID do Atendente: {self.call.userID}", text_color='Black', font=("Arial", 16), justify='left')
        #Posicionar IDs
        self.clientIDLabel.grid(row=0, column=0, sticky='W')
        self.attendantIDLabel.grid(row=1, column=0)
        #Posicionar textframe
        self.textFrame.pack(side=LEFT, padx=5)
        self.idsFrame.pack(fill='x')

        #Criar frame para os tempos
        self.timeFrame = CTkFrame(self.window, bg_color= 'transparent', fg_color='transparent')
        #Criar os labels para os tempos
        self.openTimeLabel = CTkLabel(self.timeFrame, height=23, text=f"Data de abertura: {self.call.openingDate}", text_color='Black', font=("Arial", 12), justify='left')
        self.maxTimeLabel = CTkLabel(self.timeFrame, height=23, text=f"Data máxima: {self.call.maxDate}", text_color='Black', font=("Arial", 12), justify='left')
        self.closeTimeLabel = CTkLabel(self.timeFrame, height=23, text=f"Data de fechamento: {self.call.closingDate}", text_color='Black', font=("Arial", 12), justify='left')
        #posicionar os tempos
        self.openTimeLabel.grid(row=0, column=0, sticky='WE', padx = 5)
        self.maxTimeLabel.grid(row=0, column=1, sticky='WE', padx = 5)
        self.closeTimeLabel.grid(row=0, column=2, sticky='WE', padx = 5)
        #Posicionar o timeFrame
        self.timeFrame.pack(fill='x')

    def _getStatusColor(self) -> str:
        if(self.call.status == 'closed'):
            return 'red'
        elif(self.call.status == 'open'):
            return 'green'
        else:
            return 'yellow'
    #ID, Título, Descrição, Categoria, ID do Cliente, ID do Atendente, Status (Aberto, Em atendimento, Fechado)
    #Data de Abertura, Data Máxima para Atendimento, 
    #Data de Fechamento

class MainWindowRegular(MainWindow):
    ''''Janela para Atendentes/Técnicos'''
    def __init__(self, parent : Widget, user : Clients) -> None:
        super().__init__(parent, user)
        self.user = user
        self.callsManager = CallsManager("manager.db")

        self.CategorySelectorFrame = Frame(self.window)
        self.CategorySelectorFrame.pack(side = 'top', anchor = 'w', ipady = 10)
        #Criar o Menu para seleção de item
        self.callsSelectorButton = Radiobutton(self.CategorySelectorFrame, indicatoron = False, text = 'Chamados', value = 'calls', command = self.listAllCalls)
        #Posicionar o Menu para seleção de itme
        self.callsSelectorButton.grid(row = 0, column = 3)
        #Criar o Frame para colocar a Lista e o Scroll
        self.listFrame = Frame(self.window)
        self.listFrame.pack(fill = 'both', expand = True)
        #Criar e configurar Scroll e Lista
        self.scrollbar = Scrollbar(self.listFrame, orient="vertical")
        self.listbox = Listbox(self.listFrame, width=50, height=1, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        #Posicionar Scroll e Lista
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.pack(side="left",fill="both", expand=True)
        #Criar Frame para os botões de adicionar, remover, visualizar e editar
        self.buttonsFrame = Frame(self.window)
        self.buttonsFrame.pack(side = 'left', ipady = 5)
        #Criar os botões de adicionar, remover, visualizar e editar
        self.addButton = Button(self.buttonsFrame, text = 'Adicionar', command = self.addItem)
        self.visualizeButton = Button(self.buttonsFrame, text = 'Visualizar', command = self.visualizeItem)
        #Posicionar os botões de adicionar, remover, visualizar e editar
        self.addButton.grid(column = 0, row = 0)
        self.visualizeButton.grid(column = 2, row = 0)
        #Criar o frame para colocar os botões de filtro de chamados
        self.filterButtonFrame = Frame(self.window)
        #Criar os botões de filtro de chamados
        self.statusFilter = StringVar()
        self.statusFilter.set('all')
        self.filterButtonAll = Radiobutton(self.filterButtonFrame, variable = self.statusFilter, value = 'all', text = 'Todos', command = self.listAllCalls)
        self.filterButtonOpen = Radiobutton(self.filterButtonFrame, variable = self.statusFilter, value = 'open', text = 'Abertos', command = self.listOpenCalls)
        self.filterButtonClosed = Radiobutton(self.filterButtonFrame, variable = self.statusFilter, value = 'closed', text = 'Fechados', command = self.listClosedCalls)
        self.filterButtonInService = Radiobutton(self.filterButtonFrame, variable = self.statusFilter, value = 'in service', text = 'Em atendimento', command = self.listInServiceCalls)
        #Posicionar os botões de filtros de chamados dentro do frame
        self.filterButtonAll.grid(row = 0, column = 0)
        self.filterButtonOpen.grid(row = 0, column = 1)
        self.filterButtonClosed.grid(row = 0, column = 2)
        self.filterButtonInService.grid(row = 0, column = 3)
        #Mostrar usuários como padrão quando iniciar a janela
        self.listAllCalls()

    #Mostrar a lista de todos os chamados
    def listAllCalls(self) -> None:
        self.filterButtonFrame.pack(before = self.listFrame, side = 'top', anchor = 'w')  
        self.listbox.delete(0, 'end') 
        for id in self.callsManager.getAllIds():
            call = self.callsManager.getByID(id)
            if(call.clientID == self.user.id):
                self.listbox.insert("end", f"{id} - {call.title}")

    #Mostrar a lista de chamados abertos
    def listOpenCalls(self) -> None:
        self.filterButtonFrame.pack(before = self.listFrame, side = 'top', anchor = 'w')  
        self.listbox.delete(0, 'end') 
        for id in self.callsManager.getAllIds():
            call = self.callsManager.getByID(id)
            if(call.clientID == self.user.id and call.status == 'open'):
                self.listbox.insert("end", f"{id} - {call.title}")

    #Mostrar a lista de chamados fechados
    def listClosedCalls(self) -> None:
        self.filterButtonFrame.pack(before = self.listFrame, side = 'top', anchor = 'w')  
        self.listbox.delete(0, 'end') 
        for id in self.callsManager.getAllIds():
            call = self.callsManager.getByID(id)
            if(call.clientID == self.user.id and call.status == 'closed'):
                self.listbox.insert("end", f"{id} - {call.title}")

    #Mostrar a lista de chamados em atendimento
    def listInServiceCalls(self) -> None:
        self.filterButtonFrame.pack(before = self.listFrame, side = 'top', anchor = 'w')  
        self.listbox.delete(0, 'end') 
        for id in self.callsManager.getAllIds():
            call = self.callsManager.getByID(id)
            if(call.clientID == self.user.id and call.status == 'ongoing'):
                self.listbox.insert("end", f"{id} - {call.title}")
    
    def _getFunction(self):
        if(self.statusFilter == 'in service'):
            return self.listInServiceCalls
        if(self.statusFilter == 'open'):
            return self.listOpenCalls
        elif(self.statusFilter == 'closed'):
            return self.listInServiceCalls
        else:
            return self.listAllCalls

    def addItem(self) -> None:
        CallsAdder(self.window, self._getFunction(), self.user)

    def visualizeItem(self) -> None:
        selected = self.listbox.get(ANCHOR)
        if(selected):
            CallVisualizer(self.window, self.listbox.get(ANCHOR))

class InvalidUser(BaseException):
    pass

class MainWindowSelector():
    def createWindow(self, user : Clients|Users, parent : Widget) -> None:
        #Verificar qual tipo de usuário é e criar janela adequada
        
        if(type(user) == Clients):
            return MainWindowRegular(parent, user)
        elif(type(user) == Users):
            return MainWindowSpecial(parent, user)
        else:
            raise InvalidUser("Erro usuário Inválido")

class StartScreen:
    '''Janela parente de todas as outras e também janela de login'''
    def __init__(self) -> None: 
        #Criando Janela Filha de login
        self.window = Tk("Login")
        self.window.iconbitmap("assets/Icon.ico")
        self.window.title("Log In -  Sistema Integrado de Gestão Empresarial")
        #Definindo altura e largura
        self.width = 300
        self.height = 400
        self.window.geometry(f"{self.width}x{self.height}")
        #Impedindo a modificação do tamanho da janela
        self.window.resizable(False, False)
        #criação do seletor de janela
        self.windowSelector = MainWindowSelector()
        self.__createComponents()

    def __createComponents(self) -> None: 
        self.logoImage = CTkLabel(self.window, 200, 200, 5, text="", image=CTkImage(Image.open("assets/LoginImage.jpg"), size=(120,120)))
        self.logoImage.place(relx=0.5, rely=0.25, anchor=CENTER)
        #Criando Entrada de Login
        self.loginField = CTkEntry(self.window, 200, 28, 5, placeholder_text='Email', placeholder_text_color='White', text_color='white', fg_color='black')                                        
        self.loginField.place(relx=0.5, rely=0.5, anchor=CENTER)
        #Criando Entrada de Senha                       
        self.passwordField = CTkEntry(self.window, 200, 28, 5, show='*', placeholder_text='Senha', placeholder_text_color="White", text_color='white', fg_color='black')
        self.passwordField.place(relx=0.5, rely=0.6, anchor=CENTER)         
        #Criando Botão de Login                    
        self.logInButton = CTkButton(self.window, 100, 28, 5, text="Log In", command=self._logIn)
        self.logInButton.place(relx=0.5, rely=0.7, anchor=CENTER)
    
    def _logIn(self) -> None:
        usersManager = UsersManager("manager.db")
        clientsManager = ClientsManager("manager.db")
        #Pegar os textos das entradas Login e Senha
        login = self.loginField.get()
        password = self.passwordField.get()
        #Verificação de login e senha - placeholder
        if(usersManager.isValid(login, password)): 
            # Ocultar janela de login e criar janela principal 
            user = usersManager.getByEmailAndPassword(login, password)
            self.window.withdraw()
            self.windowSelector.createWindow(user, self.window)
        elif(clientsManager.isValid(login, password)):
            # Ocultar janela de login e criar janela principal
            client = clientsManager.getByEmailAndPassword(login, password)
            self.window.withdraw()
            self.windowSelector.createWindow(client, self.window)
        else:
            #Criar mensagem de erro
            messagebox.showwarning('Inválido', "Usuário ou Senha Inválidos.")

    def initialize(self) -> None:
        '''Inicializar janela de login'''
        self.window.mainloop()