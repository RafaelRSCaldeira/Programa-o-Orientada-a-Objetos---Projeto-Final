from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import Image
from abc import ABC
from Users import *

class MainWindow(ABC):
    '''Janela principal do sistema de gestão'''
    def __init__(self, parent, user) -> None:
        #Criar Janela Principal
        self.window = Toplevel(parent)
        self.window.title("Menu - Sistema Integrado de Gestão Empresarial")
        #Definir geometria padrão
        self.width = 800
        self.height = 450
        self.window.geometry(f"{self.width}x{self.height}")

class MainWindowSpecial(MainWindow):
    ''''Janela para Atendentes/Técnicos'''
    def __init__(self, parent, user) -> None:
        super().__init__(parent, user)
        self.CategorySelectorFrame = Frame(self.window)
        self.CategorySelectorFrame.pack(side = 'top', anchor = 'w', ipady = 10)
        #Criar o Menu para seleção de item
        self.selectedCategory = StringVar()
        self.usersSelectorButton = Radiobutton(self.CategorySelectorFrame, indicatoron = False, text = 'Usuários', variable = self.selectedCategory, value = 'users', command = self.listUsers)
        self.clientsSelectorButton = Radiobutton(self.CategorySelectorFrame, indicatoron = False, text = 'Clientes', variable = self.selectedCategory, value = 'clients', command = self.listClients)
        self.problemsSelectorButton = Radiobutton(self.CategorySelectorFrame, indicatoron = False, text = 'Problemas', variable = self.selectedCategory, value = 'problems', command = self.listProblems)
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

    #Mostrar a lista de usuários
    def listUsers(self):
        self.filterButtonFrame.pack_forget()
        self.listbox.delete(0, 'end')
        for i in range(0,100):
            self.listbox.insert("end", "Usuário #%s" % i)

    #Mostrar a lista de clientes
    def listClients(self):
        self.filterButtonFrame.pack_forget()
        self.listbox.delete(0, 'end')
        for i in range(0,100):
            self.listbox.insert("end", "Cliente #%s" % i)

    #Mostrar a lista de problemas
    def listProblems(self):
        self.filterButtonFrame.pack_forget()
        self.listbox.delete(0, 'end')
        for i in range(0,100):
            self.listbox.insert("end", "Problema #%s" % i)

    #Mostrar a lista de todos os chamados
    def listAllCalls(self):
        self.filterButtonFrame.pack(before = self.listFrame, side = 'top', anchor = 'w')  
        self.listbox.delete(0, 'end') 
        for i in range(0,100):
            self.listbox.insert("end", "Chamado #%s" % i)

    #Mostrar a lista de chamados abertos
    def listOpenCalls(self):
        self.filterButtonFrame.pack(before = self.listFrame, side = 'top', anchor = 'w')  
        self.listbox.delete(0, 'end') 
        for i in range(0, 33):
            self.listbox.insert("end", "Chamado #%s" % i)

    #Mostrar a lista de chamados fechados
    def listClosedCalls(self):
        self.filterButtonFrame.pack(before = self.listFrame, side = 'top', anchor = 'w')  
        self.listbox.delete(0, 'end') 
        for i in range(33,66):
            self.listbox.insert("end", "Chamado #%s" % i)

    #Mostrar a lista de chamados em atendimento
    def listInServiceCalls(self):
        self.filterButtonFrame.pack(before = self.listFrame, side = 'top', anchor = 'w')  
        self.listbox.delete(0, 'end') 
        for i in range(66,100):
            self.listbox.insert("end", "Chamado #%s" % i)
    
    def addItem(self):
        if self.selectedCategory.get() == 'users':
            pass
        elif self.selectedCategory.get() == 'clients':
            pass
        elif self.selectedCategory.get() == 'problems':
            pass
        elif self.selectedCategory.get() == 'calls':
            pass

    def removeItem(self):
        if self.selectedCategory.get() == 'users':
            pass
        elif self.selectedCategory.get() == 'clients':
            pass
        elif self.selectedCategory.get() == 'problems':
            pass
        elif self.selectedCategory.get() == 'calls':
            pass

    def visualizeItem(self):
        if self.selectedCategory.get() == 'users':
            pass
        elif self.selectedCategory.get() == 'clients':
            pass
        elif self.selectedCategory.get() == 'problems':
            pass
        elif self.selectedCategory.get() == 'calls':
            CallVisualizer(self.window, 'Nada')

    def editItem(self):
        if self.selectedCategory.get() == 'users':
            pass
        elif self.selectedCategory.get() == 'clients':
            pass
        elif self.selectedCategory.get() == 'problems':
            pass
        elif self.selectedCategory.get() == 'calls':
            pass


class CallVisualizer():
    '''Janela para visualizar um Chamado'''
    def __init__(self, parent, call) -> None:
        #Salvar dados do Call
        self.callID = 0
        self.title = 'Placeholder title'
        self.category = 'Placeholder category'
        self.description = 'Placeholder description'
        self.status = 'Open'
        self.clientID = 0
        self.attendantID = 0
        self.openingDate = 0
        self.maxDate = 0
        self.closingDate = 0
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
        self.titleLabel = CTkLabel(self.titleCategoryFrame, height=23, text=self.title, text_color='Black', font=("Arial", 20), justify='center')
        self.categoryLabel = CTkLabel(self.titleCategoryFrame, height=23, text=self.category, text_color='Black', font=("Arial", 12), justify='center')
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

        #Criar Texto de descrição
        self.descriptionText = Text(self.window, borderwidth=5, height=9)
        #Inserir Texto
        self.descriptionText.insert(END, self.description)
        #Bloquear modificação
        self.descriptionText.config(state=DISABLED)
        #Colocar Texto
        self.descriptionText.pack(fill='x', pady=10)
        
        #Criar Frames para os ids
        self.idsFrame = CTkFrame(self.window, bg_color= 'transparent', fg_color='transparent')
        self.textFrame = CTkFrame(self.idsFrame, bg_color= 'transparent', fg_color='transparent')
        #Criar IDs de atendente e cliente
        self.clientIDLabel = CTkLabel(self.textFrame, height=23, text=f"ID do Cliente: {self.clientID}", text_color='Black', font=("Arial", 16), justify='left')
        self.attendantIDLabel = CTkLabel(self.textFrame, height=23, text=f"ID do Atendente: {self.attendantID}", text_color='Black', font=("Arial", 16), justify='left')
        #Posicionar IDs
        self.clientIDLabel.grid(row=0, column=0, sticky='W')
        self.attendantIDLabel.grid(row=1, column=0)
        #Posicionar textframe
        self.textFrame.pack(side=LEFT, padx=5)
        self.idsFrame.pack(fill='x')

        #Criar frame para os tempos
        self.timeFrame = CTkFrame(self.window, bg_color= 'transparent', fg_color='transparent')
        #Criar os labels para os tempos
        self.openTimeLabel = CTkLabel(self.timeFrame, height=23, text=f"Data de abertura: {self.openingDate}", text_color='Black', font=("Arial", 12), justify='left')
        self.maxTimeLabel = CTkLabel(self.timeFrame, height=23, text=f"Data máxima: {self.maxDate}", text_color='Black', font=("Arial", 12), justify='left')
        self.closeTimeLabel = CTkLabel(self.timeFrame, height=23, text=f"Data de fechamento: {self.closingDate}", text_color='Black', font=("Arial", 12), justify='left')
        #posicionar os tempos
        self.openTimeLabel.grid(row=0, column=0, sticky='WE', padx = 5)
        self.maxTimeLabel.grid(row=0, column=1, sticky='WE', padx = 5)
        self.closeTimeLabel.grid(row=0, column=2, sticky='WE', padx = 5)
        #Posicionar o timeFrame
        self.timeFrame.pack(fill='x')

    def _getStatusColor(self) -> str:
        if(self.status == 'Closed'):
            return 'red'
        elif(self.status == 'Open'):
            return 'green'
        else:
            return 'yellow'
    #ID, Título, Descrição, Categoria, ID do Cliente, ID do Atendente, Status (Aberto, Em atendimento, Fechado)
    #Data de Abertura, Data Máxima para Atendimento, 
    #Data de Fechamento

class MainWindowRegular(MainWindow):#
    '''Janela para usuários normais'''
    def __init__(self, parent, user) -> None:
        super().__init__(parent, user)
        #Menu acima da janela para botão
        self.menubar = Menu(self.window)
        self.window.config(menu=self.menubar)
        self.menubar.add_command(label="Criar Chamado", command=self.openCreateCall)
        self.menubar.add_command(label="Visualizar Chamado", command=self.visualizeCall)
        #Criar e configurar Scroll e Lista
        self.scrollbar = Scrollbar(self.window, orient="vertical")
        self.listbox = Listbox(self.window, width=50, height=20, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        #Posicionar Scroll e Lista
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.pack(side="left",fill="both", expand=True)

        for i in range(0,100):
            self.listbox.insert("end", "item #%s" % i)

    def openCreateCall(self):
        pass

    def visualizeCall(self):
        CallVisualizer(self.window, "Nada")
    # Essa janela só deve conter as opções de:
        # criar chamados
        # visualizar chamados
        # (Obviamente somente os chamados próprios)

class MainWindowSelector():
    def createWindow(self, user, parent):
        #Verificar qual tipo de usuário é e criar janela adequada
        if(True):
            return MainWindowRegular(parent, user)
        elif(True):
            return MainWindowSpecial(parent, user)

class StartScreen:
    '''Janela parente de todas as outras e também janela de login'''
    def __init__(self): 
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

    def __createComponents(self): 
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
    
    def _logIn(self):
        usersManager = UsersManager("users.db")
        #Pegar os textos das entradas Login e Senha
        login = self.loginField.get()
        password = self.passwordField.get()
        #Verificação de login e senha - placeholder
        print(login, password)
        if(usersManager.isValid(login, password)): 
            #Ocultar janela de login e criar janela principal
            self.window.withdraw()
            self.windowSelector.createWindow("", self.window)
        else:
            #Criar mensagem de erro
            messagebox.showwarning('Inválido', "Usuário ou Senha Inválidos.")

    def initialize(self):
        '''Inicializar janela de login'''
        self.window.mainloop()