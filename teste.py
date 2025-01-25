import time

#def use testeGustavoPimenta@teste.com
#def password testeGustavoPimenta

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def iniciaServico(): 
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get("http://www.automationpractice.pl/index.php?id_category=3&controller=category")

def realizaLogin(navegador, user, password):
    # Acessa a página de login
    navegador.get('http://www.automationpractice.pl/index.php?controller=authentication&back=my-account')
    
    # Aguarda o campo de e-mail ser visível e insere o e-mail
    email_field = WebDriverWait(navegador, 10).until(
        EC.visibility_of_element_located(('xpath', '//*[@id="email"]'))
    )
    email_field.send_keys(user)
    
    # Aguarda o campo de senha ser visível e insere a senha
    password_field = WebDriverWait(navegador, 10).until(
        EC.visibility_of_element_located(('xpath', '//*[@id="passwd"]'))
    )
    password_field.send_keys(password)
    
    # Clica no botão de login
    login_button = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable(('xpath', '//*[@id="SubmitLogin"]/span'))
    )
    login_button.click()
    print('sucess - loginEfetuado')

def compraUmaCamisa(navegador):
    print("Escolhendo uma camisa branca disponível")
    navegador.get("http://www.automationpractice.pl/index.php?id_product=2&controller=product#/1-size-s/8-color-white")
    print('sucess1 - AcessadoCamisaBranca')

    # Espera o botão de adicionar ao carrinho estar clicável e clica nele
    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add_to_cart"]/button/span'))
    ).click()
    print('sucess2 - AdicionadoAoCarrinho')

    # Espera o botão "Ir para o carrinho" estar clicável e clica nele
    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span'))
    ).click()
    print('sucess3 - IrParaOCarrinho')

    # Espera o botão "CheckOut Login" estar clicável e clica nele
    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/p[2]/a[1]/span'))
    ).click()
    print('sucess4 - CheckOut Login')

    # Espera o botão "CheckOut Address" estar clicável e clica nele
    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/form/p/button'))
    ).click()
    print('sucess5 - CheckOut Address')

    # Marca a checkbox dos termos e condições e clica no botão "CheckOut Shipping"
    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="uniform-cgv"]/span'))
    ).click()

    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/p/button'))
    ).click()
    print('sucess5 - CheckOut Shipping')

    # Seleciona o método de pagamento e finaliza o pedido
    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a'))
    ).click()

    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="cart_navigation"]/button'))
    ).click()

    print('Pedido finalizado com sucesso!')

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get("http://www.automationpractice.pl/index.php?id_category=3&controller=category")
print('sucess0 - Site acessado')

realizaLogin(navegador, 'testeGustavoPimenta@teste.com', 'testeGustavoPimenta')
print('sucess - login Efetuado')

compraUmaCamisa(navegador)
print('sucess - Camisa comprada')

