import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from io import BytesIO
import sqlite3

def pagina():
    conexao = sqlite3.connect("supplier.db")
    cursor = conexao.cursor()
    
    st.title("Bem vindos ao Supplier Automation")
    st.write("Nele será possivel ver um exemplo de preenchimento de formulario pegando dados de uma planilha e pegando a requisição gerada direto para a sua planilha!!")
    
    upload = st.file_uploader("Escolha seu arquivo XLSX: ", type=['xlsx','xls'])
    if upload is not None:
        df = pd.read_excel(upload)
        st.dataframe(df)
        opcoes = df['Colaborador'].tolist()  
        opcao_selecionada = st.selectbox("Selecione um colaborador: ", opcoes)
        dados_selecionados = df[df['Colaborador'] == opcao_selecionada].iloc[0]
        st.write(dados_selecionados['Colaborador'], dados_selecionados['Matricula'], dados_selecionados['Valor'])
        
        executar = st.button("Executar automação: ")
        if executar:
            driver = webdriver.Chrome()
            driver.get("https://arthurresendes.github.io/supplier_automation/chamado.html")
            nome_admin = driver.find_element(By.ID, "nomeAdmin")
            nome_admin.send_keys(dados_selecionados['Admin'])
        
            nome_col = driver.find_element(By.ID, "nomeCol")
            nome_col.send_keys(dados_selecionados['Colaborador'])
            
            matricula = driver.find_element(By.ID, "ma")
            matricula.send_keys(str(dados_selecionados['Matricula']))
            
            valor = driver.find_element(By.ID, "val")
            valor.send_keys(str(dados_selecionados['Valor']))
            
            mensagem = driver.find_element(By.ID, "msg")
            mensagem.send_keys(f"Abertura de chamado para colaborador {dados_selecionados['Colaborador']} no valor de {dados_selecionados['Valor']} com a matricula {dados_selecionados['Matricula']}")
            
            submeter = driver.find_element(By.ID, "sub")
            submeter.click()
            time.sleep(5)
            
            requisicao = driver.find_element(By.ID, "ritmId")
            ritm = requisicao.text
            
            # Adicionar RITM ao DataFrame
            if 'RITM' not in df.columns:
                df['RITM'] = ''  # Criar coluna como string
            else:
                df['RITM'] = df['RITM'].astype(str)
            
            df.loc[df['Colaborador'] == opcao_selecionada, 'RITM'] = ritm
            
            df.to_excel("planilha_atualizada.xlsx", index=False)
            output = BytesIO()
            df.to_excel(output, index=False)
            
            st.success(f"RITM {ritm} salvo na planilha")
            st.dataframe(df)
            
            st.download_button(
                label="Baixar Planilha em XLSX",
                data=output.getvalue(),
                file_name="planilha_atualizada.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            
            cursor.execute("INSERT INTO USER(nome,RITM) VALUES (?,?)", (dados_selecionados['Colaborador'], ritm))
            
            driver.close()
    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    pagina()