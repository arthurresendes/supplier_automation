import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from schemas import Envio
import time

def executar_selenium(dados: Envio):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://arthurresendes.github.io/supplier_automation/chamado.html")

        nome_admin = driver.find_element(By.ID, "nomeAdmin")
        nome_admin.send_keys(dados.Admin)

        nome_col = driver.find_element(By.ID, "nomeCol")
        nome_col.send_keys(dados.Colaborador)

        matricula = driver.find_element(By.ID, "ma")
        matricula.send_keys(str(dados.Matricula))

        valor = driver.find_element(By.ID, "val")
        valor.send_keys(str(dados.Valor))

        mensagem = driver.find_element(By.ID, "msg")
        mensagem.send_keys(
            f"Abertura de chamado para colaborador "
            f"{dados.Colaborador} no valor de {dados.Valor} "
            f"com a matricula {dados.Matricula}"
        )

        submeter = driver.find_element(By.ID, "sub")
        submeter.click()

        time.sleep(5)

        requisicao = driver.find_element(By.ID, "ritmId")
        ritm = requisicao.text

        return ritm

    finally:
        driver.quit()