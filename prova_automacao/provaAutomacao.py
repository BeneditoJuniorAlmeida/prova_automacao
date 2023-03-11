from abc import ABC
from selenium.webdriver.common.by import By
import time

class PageElement(ABC):
    def __init__(self, webdriver):
        self.webdriver = webdriver
           

#Classe de login com modelo page object
class Login(PageElement):
    username = (By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input')
    password = (By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input')
    submit = (By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/input')
       
    def dados_login(self, username, password):
        self.webdriver.find_element(*self.username).send_keys(username)
        self.webdriver.find_element(*self.password).send_keys(password)
        self.webdriver.find_element(*self.submit).click()


class Produto(PageElement):
    produto1 = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
    produto2 = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button')
    produto3 = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button')
    produto4 = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/button')
    produto5 = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[2]/button')
    produto6 = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[2]/button')
    abrirCarrinho = (By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a')

    def dados_produto(self):
        self.webdriver.find_element(*self.produto1).click()
        time.sleep(2)
        self.webdriver.find_element(*self.produto3).click()
        time.sleep(2)
        self.webdriver.find_element(*self.abrirCarrinho).click()
        
class Carrinho(PageElement):
    checkout = (By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/button[2]')

    def dados_carrinho(self):
        self.webdriver.find_element(*self.checkout).click()
        
class FinalizarCompra(PageElement):
    fistName = (By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input')
    lastName = (By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input')
    zipCode = (By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input')
    submit = (By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[2]/input')
       
    def dados_compra(self, fistName, lastName, zipCode):
        self.webdriver.find_element(*self.fistName).send_keys(fistName)
        time.sleep(1)
        self.webdriver.find_element(*self.lastName).send_keys(lastName)
        time.sleep(1)
        self.webdriver.find_element(*self.zipCode).send_keys(zipCode)
        time.sleep(1)
        self.webdriver.find_element(*self.submit).click()

class Finalizar(PageElement):
    finalizar = (By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]')

    def dados_finaliza(self):
        self.webdriver.find_element(*self.finalizar).click()

class VoltarHome(PageElement):
    home = (By.XPATH, '/html/body/div/div/div/div[2]/button')

    def dados_home(self):
        self.webdriver.find_element(*self.home).click()

