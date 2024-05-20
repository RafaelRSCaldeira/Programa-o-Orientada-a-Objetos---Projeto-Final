from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import Image

class MainWindow:
    '''Janela principal do sistema de gestão'''
    def __init__(self, parent) -> None:
        #Criar Janela Principal
        self.window = Toplevel(parent)
        self.window.title("Menu - Sistema Integrado de Gestão Empresarial")
        #Definir geometria padrão
        self.width = 800
        self.height = 450
        self.window.geometry(f"{self.width}x{self.height}")


class StartScreen:
    '''Janela parente de todas as outras e também janela de login'''
    def __init__(self): 
        #Criando Janela Filha de login
        self.window = Tk("Login")
        self.window.iconbitmap("Icon.ico")
        self.window.title("Log In -  Sistema Integrado de Gestão Empresarial")
        #Definindo altura e largura
        self.width = 300
        self.height = 400
        self.window.geometry(f"{self.width}x{self.height}")
        #Impedindo a modificação do tamanho da janela
        self.window.resizable(False, False)
        self.__createComponents()

    def __createComponents(self): 
        self.logoImage = CTkLabel(self.window, 200, 200, 5, text="", image=CTkImage(Image.open("LoginImage.png"), size=(120,120)))
        self.logoImage.place(relx=0.5, rely=0.25, anchor=CENTER)
        #Criando Entrada de Login
        self.loginField = CTkEntry(self.window, 200, 28, 5)                                        
        self.loginField.place(relx=0.5, rely=0.5, anchor=CENTER)
        #Criando Entrada de Senha                       
        self.passwordField = CTkEntry(self.window, 200, 28, 5, show='*')
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
            MainWindow(self.window)
        else:
            #Criar mensagem de erro
            messagebox.showwarning('Inválido', "Usuário ou Senha Inválidos.")

    def initialize(self):
        '''Inicializar janela de login'''
        self.window.mainloop()

a = StartScreen()
a.initialize()