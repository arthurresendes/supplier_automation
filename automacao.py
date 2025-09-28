import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
#https://arthurresendes.github.io/supplier_automation/chamado.html

def stream():
    st.title("Bem vindos ao Supplier Automation")
    st.subheader("Nele será possivel ver um exemplo de preenchimento de formulario pegando dados de uma planilha e pegando a requisição gerada direto para a sua planilha!!")
    upload = st.file_uploader("Escolha seu arquivo XLSX: ", type=['xlsx','xls'])