import sqlite3

conexao = sqlite3.connect("supplier.db")

cursor = conexao.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS USER (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(200),
        RITM VARCHAR(15)
    );
''')

conexao.commit()

conexao.close()