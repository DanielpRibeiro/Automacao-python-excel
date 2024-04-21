# instalar selenium > pip install
# instalar playwright > pip install
#instalar pandas


# 0 ler arquivo excel
# 1 loopar arquivos 
# 2 preencher os dados lidos em cada linha no navegador
 


# importacoes para ler o arquivo excel

import pandas as pd

# definir tempo de preenchimento
import time


#importacoes para automatizar a web

from selenium import webdriver # o navegador
from selenium.webdriver.common.by import By # achar os elementos
from selenium.webdriver.common.keys import Keys # para digitar o teclado na web


nome_do_arquivo = "automacao.xlsx"

df = pd.read_excel(nome_do_arquivo)

# print(df)
# Acima exibe os dados da tabela
# print('Passou aqui!')

url_do_forms = "http://127.0.0.1/php/Automacao%20python/form.php"

for index,row in df.iterrows():
    print("index: " + str(index) + " E o nome do fulano é " + row["nome"])
    
    # fazer download do chrome driver versao atual e jogar na pasta
    
    chrome = webdriver.Chrome()
    chrome.get(url_do_forms)
    
    time.sleep(4)
    
    elemento_texto_nome = chrome.find_element(By.XPATH, '//*[@id="nome"]')
    elemento_texto_numero = chrome.find_element(By.XPATH, '//*[@id="numero"]')
    elemento_texto_email = chrome.find_element(By.XPATH, '//*[@id="email"]')
    elemento_texto_nota = chrome.find_element(By.XPATH, '//*[@id="nota"]')
    
    elemento_texto_nome.send_keys(row["nome"])
    elemento_texto_numero.send_keys(row["numero"])
    elemento_texto_email.send_keys(row["email"])
    elemento_texto_nota.send_keys(row["nota"])

    
    chrome.find_element(By.XPATH, '/html/body/form/input[5]').click()
    
    
    chrome.quit
    
    # print(selenium.__version__)
