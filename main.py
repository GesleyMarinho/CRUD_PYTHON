from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkcalendar import Calendar, DateEntry
from tkinter import font
from tkinter import ttk

#importando arquivos View;
from view import *

#cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

janela = Tk()
janela.title("Tela Consula")
janela.geometry("1043x453")
janela.configure(background=co9)
janela.resizable(height=FALSE, width=FALSE)
janela.attributes("-alpha",0.9)

#divisão das janelas
frameCima = Frame(janela,width=310, height=50, bg=co2,relief='flat')
frameCima.grid(row=0,column=0)

frameBaixo = Frame(janela,width=310, height=403, bg=co1,relief='flat')
frameBaixo.grid(row=1,column=0,sticky=NSEW,padx=0,pady=1)

frameDireita = Frame(janela,width=588, height=403, bg=co1,relief='flat')
frameDireita.grid(row=0,column=1,rowspan=2,padx=1,pady=0,sticky=NSEW)

# Label Cima 
app_nome= Label (frameCima,text='Formulário de Consultória',bg=co2,relief='flat',anchor=NW,font="ivy 13 bold",fg=co1)
app_nome.place(x=10,y=20)

#função para inserir dados
def inserir():
    nome = E_nome.get()
    email = E_email.get()
    telefone = E_telefone.get()
    data = E_dataConsulta.get()
    estado = E_estadoConsulta.get()
    assunto = E_assunto.get()

    lista=[nome,email,telefone,data,estado,assunto]
    
    if nome == '':
        messagebox.showerror('Erro','Nome não pode ser null ou vazio')
    else:
        inserir_Dados(lista)
        messagebox.showinfo('OK','Dados cadastrados com Sucesso !!!')

        E_nome.delete(0,'end')
        E_email.delete(0,'end')
        E_telefone.delete(0,'end')
        E_dataConsulta.delete(0,'end')
        E_estadoConsulta.delete(0,'end')
        E_assunto.delete(0,'end')

    for widget in frameDireita.winfo_children():
        widget.destroy()
    
    mostrar()





# Label Baixo 
#Nome
L_nome = Label (frameBaixo,text='Nome *',bg=co1,relief='flat',anchor=NW,font="ivy 13 bold",fg=co4)
L_nome.place(x=15,y=10)
E_nome = Entry(frameBaixo, width=45,justify='left',relief='solid')
E_nome.place(x=15,y=50)

#email
L_email = Label (frameBaixo,text='E-mail *',bg=co1,relief='flat',anchor=NW,font="ivy 13 bold",fg=co4)
L_email.place(x=15,y=70)
E_email = Entry(frameBaixo, width=45,justify='left',relief='solid')
E_email.place(x=15,y=100)

#Telefone
T_telefone = Label (frameBaixo,text='Telefone *',bg=co1,relief='flat',anchor=NW,font="ivy 13 bold",fg=co4)
T_telefone.place(x=15,y=130)
E_telefone = Entry(frameBaixo, width=45,justify='left',relief='solid')
E_telefone.place(x=15,y=160)

#Data da Consulta
D_dataConsulta = Label (frameBaixo,text='Data *',bg=co1,relief='flat',anchor=NW,font="ivy 13 bold",fg=co4)
D_dataConsulta.place(x=15,y=190)
E_dataConsulta = DateEntry(frameBaixo, width=12,bg="DarkBlue",foreground='white',borderwidth=2)
E_dataConsulta.place(x=15,y=220)

#Estado 
E_estadoConsulta = Label (frameBaixo,text='Estado da Consulta *',bg=co1,relief='flat',anchor=NW,font="ivy 13 bold",fg=co4)
E_estadoConsulta.place(x=160,y=190)
E_estadoConsulta = Entry(frameBaixo, width=20,justify='left',relief='solid')
E_estadoConsulta.place(x=160,y=220)

#Assunto da consulta
C_assunto = Label (frameBaixo,text='Assunto *',bg=co1,relief='flat',anchor=NW,font="ivy 13 bold",fg=co4)
C_assunto.place(x=15,y=260)
E_assunto = Entry(frameBaixo, width=45,justify='left',relief='solid')
E_assunto.place(x=15,y=290)

#Botão Inserir
B_buttonInserir = Button (frameBaixo,text='Inserir', width = 9,bg=co6,fg=co1,relief='raised',anchor=NW,font="ivy 9 bold",overrelief='ridge', command=inserir)
B_buttonInserir.place(x=15,y=340)

#Botão Atualizar
B_buttonAtualizar = Button (frameBaixo,text='Atualizar', width = 9,bg=co2,fg=co1,relief='raised',anchor=NW,font="ivy 9 bold",overrelief='ridge')
B_buttonAtualizar.place(x=110,y=340)

#Botão Deletar
B_buttonDeletar = Button (frameBaixo,text='Deletar', width = 9,bg=co7,fg=co1,relief='raised',anchor=NW,font="ivy 9 bold",overrelief='ridge')
B_buttonDeletar.place(x=210,y=340)


def mostrar(): 
    lista = mostrar_info()

    # lista para cabecario
    tabela_head = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']
    # criando a tabela
    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frameDireita.grid_rowconfigure(0, weight=12)
    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0
    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

mostrar()


janela.mainloop()





    

