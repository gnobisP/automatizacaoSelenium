from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def compra_uma_camisa(navegador):
    """Realiza a compra de uma camisa no site."""
    print("Escolhendo uma camisa branca disponível")
    navegador.get("http://www.automationpractice.pl/index.php?id_product=2&controller=product#/1-size-s/8-color-white")
    print('sucess1 - Acessado camisa branca')

    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add_to_cart"]/button/span'))
    ).click()
    print('sucess2 - Adicionado ao carrinho')

    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span'))
    ).click()
    print('sucess3 - Ir para o carrinho')

    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/p[2]/a[1]/span'))
    ).click()
    print('sucess4 - CheckOut Login')

    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/form/p/button'))
    ).click()
    print('sucess5 - CheckOut Address')

    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="uniform-cgv"]/span'))
    ).click()

    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/p/button'))
    ).click()
    print('sucess5 - CheckOut Shipping')

    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a'))
    ).click()

    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="cart_navigation"]/button'))
    ).click()

    print('Pedido finalizado com sucesso!')
