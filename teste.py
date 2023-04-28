from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

nome_do_arquivo = "challenge.xlsx"
url_do_forms = "https://www.rpachallenge.com/"

df = pd.read_excel(nome_do_arquivo)

#print(df.info())

for index,row in df.iterrows():
    #print("index: " + str(index) + "E o nome do fulano é " + row["First Name"])
    chrome = webdriver.Chrome()
    chrome.get(url_do_forms)

    time.sleep(0.5)

    chrome.find_element(By.XPATH, '//button[@class="waves-effect col s12 m12 l12 btn-large uiColorButton"]').click()
    elemento_texto_First_Name = chrome.find_element(By.XPATH,'//input[@ng-reflect-name="labelFirstName"]')
    elemento_texto_Role_in_company = chrome.find_element(By.XPATH,'//input[@ng-reflect-name="labelRole"]')
    elemento_texto_Address = chrome.find_element(By.XPATH,'//input[@ng-reflect-name="labelAddress"]')
    elemento_texto_Phone_Number = chrome.find_element(By.XPATH,'//input[@ng-reflect-name="labelPhone"]')
    elemento_texto_Company_Name= chrome.find_element(By.XPATH,'//input[@ng-reflect-name="labelCompanyName"]')
    elemento_texto_Email = chrome.find_element(By.XPATH,'//input[@ng-reflect-name="labelEmail"]')
    elemento_texto_Last_Name= chrome.find_element(By.XPATH,'//input[@ng-reflect-name="labelLastName"]')

    elemento_texto_First_Name.send_keys(row["First Name"])
    elemento_texto_Role_in_company.send_keys(row["Role in Company"])
    elemento_texto_Address.send_keys(row["Address"])
    elemento_texto_Phone_Number.send_keys(row["Phone Number"])
    elemento_texto_Company_Name.send_keys(row["Company Name"])
    elemento_texto_Email.send_keys(row["Email"])
    elemento_texto_Last_Name.send_keys(row["Last Name "])

    chrome.find_element(By.XPATH, '//input[@value="Submit"]').click()
    #chrome.quit