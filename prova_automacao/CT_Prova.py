from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import provaAutomacao

#Cenário: Realizar compra de dois produtos 
webdriver = Firefox()
webdriver.get('https://www.saucedemo.com') #acessar e-commerce

login = provaAutomacao.Login(webdriver) #instanciar metodo de login
#passar dados de login para o metodo
login.dados_login('standard_user', 'secret_sauce')

addProduto = provaAutomacao.Produto(webdriver)
addProduto.dados_produto()

checkout = provaAutomacao.Carrinho(webdriver)
checkout.dados_carrinho()

validarDadosCompra = provaAutomacao.FinalizarCompra(webdriver)
validarDadosCompra.dados_compra('first name', 'last name','65400000')

finalizar = provaAutomacao.Finalizar(webdriver)
finalizar.dados_finaliza()

confimacaoTexto = webdriver.find_element(By.CSS_SELECTOR, "#checkout_complete_container > h2")
assert confimacaoTexto.text == 'Thank you for your order!'

voltarHome = provaAutomacao.VoltarHome(webdriver)
voltarHome.dados_home()

#encerrar teste
webdriver.close()
