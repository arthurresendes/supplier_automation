import sqlite3

def inicializar():
    conexao = sqlite3.connect("supplier.db")
    cursor = conexao.cursor()
    
    return conexao,cursor

def dados(dados_selecionados):
    nome = str(dados_selecionados['Colaborador'])
    admin = str(dados_selecionados['Admin'])
    try:
        matricula = str(int(float(dados_selecionados['Matricula'])))
    except:
        matricula = str(dados_selecionados['Matricula'])
    
    try:
        valor = round(float(dados_selecionados['Valor']), 2)
    except:
        valor = 0.0
    
    return nome,admin,matricula,valor

def query(nome,admin,matricula,valor, ritm):
    _,cursor = inicializar()
    cursor.execute("INSERT INTO CHAMADO(nome,admin,matricula,valor,RITM) VALUES (?,?,?,?,?)", (nome,admin,matricula,valor, ritm))

def main_banco(dados_selecionados,ritm):
    conexao, _ = inicializar()
    nome, admin,matricula,valor = dados(dados_selecionados)
    query(nome,admin,matricula,valor, ritm)
    conexao.commit()
    conexao.close()
