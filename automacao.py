import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from io import BytesIO

def executar_automacao_para_todos(df):
    driver = webdriver.Chrome()
    
    try:
        for index, row in df.iterrows():
            if pd.isna(row.get('RITM')) or row['RITM'] == '':
                driver.get("https://arthurresendes.github.io/supplier_automation/chamado.html")
                
                nome_admin = driver.find_element(By.ID, "nomeAdmin")
                nome_admin.clear()
                nome_admin.send_keys(str(row['Admin']))
                
                nome_col = driver.find_element(By.ID, "nomeCol")
                nome_col.clear()
                nome_col.send_keys(str(row['Colaborador']))
                
                matricula = driver.find_element(By.ID, "ma")
                matricula.clear()
                matricula.send_keys(str(row['Matricula']))
                
                valor = driver.find_element(By.ID, "val")
                valor.clear()
                valor.send_keys(str(row['Valor']))
                
                mensagem = driver.find_element(By.ID, "msg")
                mensagem.clear()
                mensagem.send_keys(f"Abertura de chamado para colaborador {row['Colaborador']} no valor de {row['Valor']} com a matricula {row['Matricula']}")
                
                submeter = driver.find_element(By.ID, "sub")
                submeter.click()
                time.sleep(3)
                
                requisicao = driver.find_element(By.ID, "ritmId")
                ritm = requisicao.text
                
                # Atualizar DataFrame
                df.at[index, 'RITM'] = ritm
                st.success(f"RITM {ritm} gerado para {row['Colaborador']}")
                
    except Exception as e:
        st.error(f"Erro durante a automação: {e}")
    finally:
        driver.close()
    return df

def pagina():
    st.title("Bem vindos ao Supplier Automation")
    st.write("Nele será possivel ver um exemplo de preenchimento de formulario pegando dados de uma planilha e pegando a requisição gerada direto para a sua planilha!!")
    
    upload = st.file_uploader("Escolha seu arquivo XLSX: ", type=['xlsx','xls'])
    
    if upload is not None:
        df = pd.read_excel(upload)
        if 'RITM' not in df.columns:
            df['RITM'] = ''
        
        st.dataframe(df)
        
        opcoes = ['-- TODOS OS COLABORADORES --'] + df['Colaborador'].tolist()
        opcao_selecionada = st.selectbox("Selecione um colaborador: ", opcoes)
        
        if opcao_selecionada != '-- TODOS OS COLABORADORES --':
            dados_selecionados = df[df['Colaborador'] == opcao_selecionada].iloc[0]
            st.write(f"**Colaborador:** {dados_selecionados['Colaborador']}")
            st.write(f"**Matrícula:** {dados_selecionados['Matricula']}")
            st.write(f"**Valor:** {dados_selecionados['Valor']}")
            st.write(f"**RITM:** {dados_selecionados['RITM'] if dados_selecionados['RITM'] else 'Não gerado'}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            executar_um = st.button("Executar para UM colaborador")
            
        with col2:
            executar_todos = st.button("Executar para TODOS os colaboradores")
        
        if executar_um and opcao_selecionada != '-- TODOS OS COLABORADORES --':
            driver = webdriver.Chrome()
            driver.get("https://arthurresendes.github.io/supplier_automation/chamado.html")
            
            nome_admin = driver.find_element(By.ID, "nomeAdmin")
            nome_admin.send_keys(str(dados_selecionados['Admin']))
            
            nome_col = driver.find_element(By.ID, "nomeCol")
            nome_col.send_keys(str(dados_selecionados['Colaborador']))
            
            matricula = driver.find_element(By.ID, "ma")
            matricula.send_keys(str(dados_selecionados['Matricula']))
            
            valor = driver.find_element(By.ID, "val")
            valor.send_keys(str(dados_selecionados['Valor']))
            
            mensagem = driver.find_element(By.ID, "msg")
            mensagem.send_keys(f"Abertura de chamado para colaborador {dados_selecionados['Colaborador']} no valor de {dados_selecionados['Valor']} com a matricula {dados_selecionados['Matricula']}")
            
            submeter = driver.find_element(By.ID, "sub")
            submeter.click()
            time.sleep(3)
            
            requisicao = driver.find_element(By.ID, "ritmId")
            ritm = requisicao.text
            
            df.loc[df['Colaborador'] == opcao_selecionada, 'RITM'] = ritm
            
            st.success(f"RITM {ritm} gerado para {opcao_selecionada}")
            driver.close()
        
        elif executar_todos:
            st.info("Executando automação para todos os colaboradores...")
            df = executar_automacao_para_todos(df)
            st.success("Automação concluída para todos os colaboradores!")
        
        st.subheader("Planilha Atualizada")
        st.dataframe(df)
        
        # Botão de download
        output = BytesIO()
        df.to_excel(output, index=False)
        
        st.download_button(
            label="Baixar Planilha Completa em XLSX",
            data=output.getvalue(),
            file_name="planilha_com_todos_ritms.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == "__main__":
    pagina()