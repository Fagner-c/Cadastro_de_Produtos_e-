from tkinter import *
contas_existentes = [{'user': 'Fagner Cardoso', 'senha': 'abacate', 'cargo': 'Gerente'}, {'user': 'Luiz Carlos', 'senha': 'cid', 'cargo': 'Atendente'}]
produtos = [{'nome': 'Abacate', 'preco': 8.00, 'quantidade': 120}, {'nome': 'Abacate', 'preco': 8.00, 'quantidade': 110}]
user_log = user_cargo =''
def caracteristicas_janela():
    janela_largura= 800
    janela_altura= 600
    tela_largura = janela.winfo_screenwidth()
    tela_altura= janela.winfo_screenheight()
    posx= tela_largura / 2 - janela_largura/2 
    posy= tela_altura/2 - janela_altura/2
    janela.title("Pro Estoque")
    janela.geometry('%dx%d+%d+%d' %(janela_largura, janela_altura, posx,posy))
    janela.resizable(False, False)
    #janela.iconbitmap('')
    janela.config(background="#000000")

def front_login():
    def validar_senha(senha_digitada, user_digitado, contas_existentes):
        global user_log, user_cargo
        for us in contas_existentes:
            if user_digitado == us['user']:
                if us['senha'] == senha_digitada:
                    user_log = user_digitado
                    user_cargo = us['cargo']
                    frame_login.destroy()
                    return lobby()
                else:
                    erro_label = Label(frame_login, text='Senha invalida!',foreground='#FF0000', bg='#000000' )
                    erro_label.place(relx= 0.43, rely= 0.49)
                    return False
    def validar_login(user, senha, conta):
        for us in contas_existentes:
            if user == us['user']:
                    return validar_senha(senha, user, conta)
            else:
                erro_label = Label(frame_login, text='Usuario invalido!',foreground='#FF0000', bg='#000000' )
                erro_label.place(relx= 0.43, rely= 0.49)

    frame_login = Frame(janela, bg="#000000", width=800, height=600)
    frame_login.place(relx=0)
    title_label = Label(frame_login, text='Campo de Login ', font='Arial, 38', foreground='#FFFAFA', background='#000000')
    title_label.place(relx= 0.25,  rely = 0.20)

    user_label = Label(frame_login, text='Usuario', font='Arial, 12', foreground='#FFFAFA', background='#000000')
    user_label.place(relx= 0.31,  rely = 0.38)
    user_entry = Entry(frame_login, width= 30)
    user_entry.place(relx= 0.4, rely=0.38)
    
    senha_label = Label(frame_login, text='Senha', font='Arial, 12', foreground='#FFFAFA', background='#000000')
    senha_label.place(relx= 0.32,  rely = 0.44)
    senha_entry = Entry(frame_login, width= 30)
    senha_entry.place(relx= 0.4, rely=0.44)
    def bnt_login_code():
        user = user_entry.get()
        senha =  senha_entry.get()
        if validar_login(user, senha, contas_existentes) == False:
            senha_entry.delete(0, END)
        else:
            return True
    bnt_login = Button(frame_login, text='Login', width= 20, command=bnt_login_code)
    bnt_login.place(relx= 0.398, rely= 0.55)
    
def lobby():
    def ver_produto():
        def excluir(event):
            btn = event.widget
            pos = btn.id
            del produtos[pos]
            frame_produto.destroy()
            return ver_produto()
        def editar(event):
            frame_edit = Frame(janela, width=800, height=600, bg='#000000')
            frame_edit.pack()
            btn = event.widget
            pos = btn.id
            frame_produto.destroy()
            edt_label = Label(frame_edit,text= 'Edição de Produto', background='#000000', foreground='#FFFAFA', font='Arial, 17')
            edt_label.place(relx=0.38, rely=0.05)
            text = f' Produto: {produtos[pos]["nome"]} | Preço: {produtos[pos]["preco"]} |  Quantidade: {produtos[pos]["quantidade"]}'
            edt_label = Label(frame_edit,text= text, background='#000000', foreground='#FFFAFA', font='Arial, 17')
            edt_label.place(relx=0.2, rely=0.2)
            name_label_edit = Label(frame_edit, text='Nome', font='Arial, 12', foreground='#FFFAFA', background='#000000')
            name_label_edit.place(relx= 0.11,  rely = 0.3)
            name_entry_edit = Entry(frame_edit, width= 30)
            name_entry_edit.place(relx= 0.24, rely=0.3)

            preco_label_edit = Label(frame_edit, text='Preço', font='Arial, 12', foreground='#FFFAFA', background='#000000')
            preco_label_edit.place(relx= 0.11,  rely = 0.4)
            preco_entry_edit = Entry(frame_edit, width= 30)
            preco_entry_edit.place(relx= 0.24, rely=0.4)

            qt_label_edit = Label(frame_edit, text='Quantidade', font='Arial, 12', foreground='#FFFAFA', background='#000000')
            qt_label_edit.place(relx= 0.11,  rely = 0.5)
            qt_entry_edit = Entry(frame_edit, width= 30)
            qt_entry_edit.place(relx= 0.24, rely=0.5)

            def atl_list():
                new_nome = name_entry_edit.get()
                new_preco=preco_entry_edit.get()
                new_qt= qt_entry_edit.get()
                produtos[pos]['nome'] = new_nome
                produtos[pos]['preco']  = new_preco
                produtos[pos]['quantidade'] = new_qt
                frame_edit.destroy()
                return lobby()
            
            btn_edit = Button(frame_edit, width= 25,text='Atualizar', command=atl_list)
            btn_edit.place(relx=0.63, rely=0.4)
            def back_lobby():
                frame_edit.destroy()
                return lobby()
            btn_lobby = Button(frame_edit, text='Voltar', command=back_lobby, width=25)
            btn_lobby.place(relx=0.63, rely=0.5)

        frame_lobby.destroy()
        frame_produto = Frame(janela, width=800, height=600, bg='#000000')
        frame_produto.pack()
        if user_cargo == 'Atendente':
            for i in range(0, len(produtos)):
                text = f'{i}- Produto: {produtos[i]["nome"]} | Preço: {produtos[i]["preco"]} |  Quantidade: {produtos[i]["quantidade"]}'
                lb= Label(frame_produto, text=text, background='#000000', foreground='#FFFAFA', font='Arial, 17')
                lb.pack()
            def back_lobby():
                frame_produto.destroy()
                return lobby()
            btn_lobby = Button(frame_produto, text='Voltar', command=back_lobby)
            btn_lobby.pack()
        else:
            a = 0
            for t in range(0, len(produtos)):
                text = f'{t+1}- Produto: {produtos[t]["nome"]} | Preço: {produtos[t]["preco"]} |  Quantidade: {produtos[t]["quantidade"]} '
                lb1= Label(frame_produto, text=text, background='#000000', foreground='#FFFAFA', font='Arial, 17')
                lb1.place(relx=0, rely=a +0.05)
                btn = Button(frame_produto, text='excluir', width=15)
                btn.place(relx=0.7, rely=a+0.05)
                btn.id = t
                btn.bind('<Button-1>', excluir)
                btn2 = Button(frame_produto, text='editar', width=15)
                btn2.place(relx=0.85, rely=a+0.05)
                btn2.id = t
                btn2.bind('<Button-1>', editar)
                a += 0.05
            def back_lobby():
                frame_produto.destroy()
                return lobby()
            btn_lobby = Button(frame_produto, text='Voltar', command=back_lobby, width=25)
            btn_lobby.place(relx=0.38, rely=a+0.8)
    frame_lobby = Frame(janela, width=800 , height=600, bg='#000000')
    frame_lobby.place(relx=0) 
    img_user = PhotoImage(file="eu.png")
    img = Label(frame_lobby, image=img_user, width=200, height=200)
    img.place(relx = 0.35, rely=0.1)
    name_user = Label(frame_lobby, text=user_log, foreground='#FFFAFA', background="#000000", font='Arial, 20')
    name_user.place(relx= 0.36, rely=0.5)
    cargo_label = Label(frame_lobby, text='Cargo:', foreground='#FFFAFA', background="#000000", font='Arial, 10')
    cargo_label.place(relx= 0.4, rely=0.6)
    cargo_user = Label(frame_lobby, text= user_cargo, foreground='#FFFAFA', background="#000000", font='Arial, 10')
    cargo_user.place(relx= 0.46, rely=0.6)
    if user_cargo == 'Atendente':
        bnt_produtos = Button(frame_lobby, text='Ver Produtos',  width=20, command=ver_produto)
        bnt_produtos.place(relx = 0.4, rely = 0.65)
    else:
        bnt_cadastro = Button(frame_lobby, text='Cadastrar usuario',  width=15)
        bnt_cadastro.place(relx = 0.32, rely = 0.65)
        bnt_adicionar = Button(frame_lobby, text='Adicionar produto',  width=15)
        bnt_adicionar.place(relx = 0.48, rely = 0.65)
        bnt_produtos = Button(frame_lobby, text='Ver Produtos',  width=20, command=ver_produto)
        bnt_produtos.place(relx = 0.38, rely = 0.7)
janela = Tk()
caracteristicas_janela()
front_login()
janela.mainloop()