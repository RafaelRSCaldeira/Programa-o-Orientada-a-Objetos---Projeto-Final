from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import Image
from abc import ABC, abstractmethod

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
    # Essa janela deve conter as opções de:
    #     Adição/Remoção/Visualização/Alteração de:
    #         Usuários
    #         Clientes
    #         Categorias de problemas
    #         Chamados
    #     Listar Chamados Baseado em diferentes parametros:  
    #         Status
    #         Abertura
    #         Fechamento
    #         Máxima para atendimento

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
        self.openTimeLabel = CTkLabel(self.timeFrame, height=23, text=f"Data de abertura: {self.openingDate}", text_color='Black', font=("Arial", 16), justify='left')
        self.maxTimeLabel = CTkLabel(self.timeFrame, height=23, text=f"Data máxima: {self.maxDate}", text_color='Black', font=("Arial", 16), justify='left')
        self.closeTimeLabel = CTkLabel(self.timeFrame, height=23, text=f"Data de fechamento: {self.closingDate}", text_color='Black', font=("Arial", 16), justify='left')
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
        self.logoImage = CTkLabel(self.window, 200, 200, 5, text="", image=CTkImage(Image.open("assets/LoginImage.png"), size=(120,120)))
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
        #Pegar os textos das entradas Login e Senha
        login = self.loginField.get()
        password = self.passwordField.get()
        #Verificação de login e senha - placeholder
        a = True
        if(a == True): 
            #Ocultar janela de login e criar janela principal
            self.window.withdraw()
            self.windowSelector.createWindow("", self.window)
        else:
            #Criar mensagem de erro
            messagebox.showwarning('Inválido', "Usuário ou Senha Inválidos.")

    def initialize(self):
        '''Inicializar janela de login'''
        self.window.mainloop()

if __name__ == '__main__':
    a = StartScreen()
    a.initialize()