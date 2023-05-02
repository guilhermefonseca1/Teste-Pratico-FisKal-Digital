#0 - Ler o arquivo Excel
#1 - Passar pelas linhas do arquivo Excel
  #1-1- Preencher o formulário do navegador com as informações do Excel
#(manipular o navegador com o selenium)

#O Selenium é uma biblioteca que auxilia na manipulação e interação com o navegador
from selenium import webdriver #Auxila na manipula do navegador
from selenium.webdriver.common.by import By #O By é utilizado para encontrar as tags dos input, por exemplo.
from selenium.webdriver.common.keys import Keys #O Keys é usado para inserir dados nos inputs
import pandas as pd #Lê o arquivo excel
import time

excel_file_path = "challenge.xlsx"
url_do_forms = "https://www.rpachallenge.com/"

data = pd.read_excel(excel_file_path) #Lendo o arquivo excel usando o pandas


for index,colunm in data.iterrows(): #O código pega o índice e a linha e retorna os elementos dentro dessa linha como um objeto
    chrome = webdriver.Chrome(executable_path='chromedriver.exe') #Cria uma instância do chrome. O chromedrive manipula o googlechrome
    chrome.get(url_do_forms) #Depois de Cria uma instância do chrome, navegue para essa url
#
    time.sleep(0.5)

    chrome.find_element(By.XPATH, '//button[@class="waves-effect col s12 m12 l12 btn-large uiColorButton"]').click()
    elemento_texto_First_Name = chrome.find_element(By.XPATH,'//input[@ng-reflect-name="labelFirstName"]')
    elemento_texto_Role_in_company = chrome.find_element(By.XPATH,'//input[@ng-reflect-name="labelRole"]')
    elemento_texto_Address = chrome.find_element(By.XPATH,'//input[@ng-reflect-name="labelAddress"]')
    elemento_texto_Phone_Number = chrome.find_element(By.XPATH,'//input[@ng-reflect-name="labelPhone"]')
    elemento_texto_Company_Name= chrome.find_element(By.XPATH,'//input[@ng-reflect-name="labelCompanyName"]')
    elemento_texto_Email = chrome.find_element(By.XPATH,'//input[@ng-reflect-name="labelEmail"]')
    elemento_texto_Last_Name= chrome.find_element(By.XPATH,'//input[@ng-reflect-name="labelLastName"]')

    elemento_texto_First_Name.send_keys(colunm["First Name"]) #No elemento_text... insira o elemento da linha chamado First Name
    elemento_texto_Role_in_company.send_keys(colunm["Role in Company"])
    elemento_texto_Address.send_keys(colunm["Address"])
    elemento_texto_Phone_Number.send_keys(colunm["Phone Number"])
    elemento_texto_Company_Name.send_keys(colunm["Company Name"])
    elemento_texto_Email.send_keys(colunm["Email"])
    elemento_texto_Last_Name.send_keys(colunm["Last Name "])

    chrome.find_element(By.XPATH, '//input[@value="Submit"]').click()
    