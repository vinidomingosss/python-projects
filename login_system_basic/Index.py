from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#Criação da janela
window = Tk() #Criar janela
window.title('VDA Systems - Acess Panel') #Nome da janela
window.geometry('600x300') #Tamanho da janela
window.configure(background='white') #Cor da janela
window.resizable(width=False, height=False) #Não pode ser modificado altura e largura
window.attributes('-alpha', 0.9) #Deixar janela transparente
window.iconbitmap(default='Icons/LogoIcon.ico')

#Carregando imagens
logo = PhotoImage(file='Icons/logo.png')

#Widgets da janela
LeftFrame = Frame(window, width=200, height=300, bg='MIDNIGHTBLUE', relief='raise')
LeftFrame.pack(side=LEFT)

RightFrame = Frame(window, width=395, height=300, bg='MIDNIGHTBLUE', relief='raise')
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg='MIDNIGHTBLUE')
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text='Username:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='White')
UserLabel.place(x=5,y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text='Password:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='White')
PassLabel.place(x=5,y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show='•')
PassEntry.place(x=150, y=160)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? AND Password = ?)
    """, (User, Pass))
    print('Deu boa malandro')
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title='Login Info', message='Acesso Permitido!')
    except:
        messagebox.showwarning(title='Login Info', message='Acesso Negado!')

#Botoes
LoginButton = ttk.Button(RightFrame, text='Login', width=30, command=Login)
LoginButton.place(x=100,y=225)

def Register():
    #Removendo widgets de login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Inserindo widgets de cadastro
    NameLabel = Label(RightFrame, text='Name:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='White')
    NameLabel.place(x=5, y=5)

    NameEntry = ttk.Entry(RightFrame, width=39)
    NameEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text='Email:', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='White')
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=65)

    def RegisterToDataBase():
        Name = NameEntry.get() #Variavel recebe o que foi digitado na entry
        Email = EmailEntry.get() #Variavel recebe o que foi digitado na entry
        User = UserEntry.get() #Variavel recebe o que foi digitado na entry
        Pass = PassEntry.get() #Variavel recebe o que foi digitado na entry

        if (Name == '' or Email == '' or User == '' or Pass == ''):
            messagebox.showerror(title='Register Error', message='Preencha todos os campos!')
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass)) #inserindo valores na tabela e relacionando com as variavels
            DataBaser.conn.commit() #Salvar alteração
            messagebox.showinfo(title='Register Info', message='Conta criada com sucesso!')

    Register = ttk.Button(RightFrame, text='Register', width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)

    def BackToLogin():
        #Removendo widgets de cadastro
        NameLabel.place(x=5000)
        NameEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #Trazendo os widgets de login
        LoginButton.place(x=100, y=225)
        RegisterButton.place(x=125,y=260)

    Back = ttk.Button(RightFrame, text='Back', width=20, command=BackToLogin)
    Back.place(x=125, y=260)

RegisterButton = ttk.Button(RightFrame, text='Register', width=20, command=Register)
RegisterButton.place(x=125,y=260)



window.mainloop() #Diz que acabaram aqui as propriedades da janela