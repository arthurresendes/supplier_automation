import sqlite3

def criacao():
    conexao = sqlite3.connect("supplier.db")
    
    cursor = conexao.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS CHAMADO (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(200),
                    admin VARCHAR(200),
                    matricula VARCHAR(10),
                    valor REAL,
                    RITM VARCHAR(15)
                );
    ''')
    conexao.commit()
    conexao.close()

'''
Antes a tabela estava sendo chamada de USER mas acredito que CHAMADO faria mais sentido , sendo assim foi atualizado o nome.

def renomeando_tabela():
    conexao = sqlite3.connect("supplier.db")
    
    cursor = conexao.cursor()
    cursor.execute("ALTER TABLE USER RENAME TO CHAMADO")
    conexao.commit()
    conexao.close()
'''

if __name__ == "__main__":
    criacao()
