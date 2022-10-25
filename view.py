import sqlite3

con = sqlite3.connect('DataBase.db')

'''lista=['teste','teste@teste.com','3136245302','29/12/1991','MG','Urgente']'''

#incerir Dados
def inserir_Dados(i):
    with con:
        cursor = con.cursor()
        query = "INSERT INTO FORMULARIO (nome,email,telefone,dia_em,estado,assunto) values(?, ?, ?, ?, ?, ?) "
        cursor.execute(query,i)

# testando com a lista acima;
#inserir_Dados(lista)

#acessar informações
def mostrar_info():
    lista=[]
    with con:
        cursor = con.cursor()
        query = "select * from formulario"
        cursor.execute(query)
        info = cursor.fetchall()

        for i in info:
            lista.append(i)
        return lista

'''
#atualizar Informações
lista= ['teste',1]
with con:
    cursor = con.cursor()
    query = " update formulario set nome = ? where id = ? "
    cursor.execute(query,lista)

#Deletar Informações
lista= [1]
with con:
    cursor = con.cursor()
    query = " delete from formulario where id = ? "
    cursor.execute(query,lista)

'''