import sqlite3

def conectar():
    return sqlite3.connect("database.db")

def criar_tabela_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS produtos (
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   produto TEXT NOT NULL,
                   categoria TEXT NOT NULL,
                   estoque_minimo INTEGER,
                   estoque_ideal INTEGER,
                   estoque_disponivel INTEGER,
                   estoque_pendente INTEGER,
                   status TEXT,
                   codigo1 INTEGER,
                   codigo2 INTEGER,
                   codigo3 INTEGER,
                   codigo4 INTEGER,
                   codigo5 INTEGER
                   )""")
    conexao.commit()
    conexao.close()