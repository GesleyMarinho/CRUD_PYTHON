import sqlite3

con = sqlite3.connect('DataBase.db')


with con:
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS FORMULARIO (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    NOME TEXT NOT NULL,
    EMAIL TEXT,
    TELEFONE INTEGER,
    DIA_EM DATE, ESTADO TEXT,
    ASSUNTO TEXT )
       """)

print("Conectado ao banco de dados")