import re

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from uteis.exceptionsLogin import InvalidPasswordException, InvalidEmailException, AuthenticationFailedException



def realiza_login(navegador, user, password):
    """Realiza login no site."""
    navegador.get('http://www.automationpractice.pl/index.php?controller=authentication&back=my-account')
    
    # Preenche o campo de e-mail
    email_field = WebDriverWait(navegador, 5).until(  # Espera reduzida para 5 segundos
        EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]'))
    )
    email_field.send_keys(user)
    
    # Preenche o campo de senha
    password_field = WebDriverWait(navegador, 5).until(  # Espera reduzida para 5 segundos
        EC.visibility_of_element_located((By.XPATH, '//*[@id="passwd"]'))
    )
    password_field.send_keys(password)
    
    # Clica no botão de login
    login_button = WebDriverWait(navegador, 5).until(  # Espera reduzida para 5 segundos
        EC.element_to_be_clickable((By.XPATH, '//*[@id="SubmitLogin"]/span'))
    )
    login_button.click()

    
    try:
        # Espera até que a URL seja a esperada
        WebDriverWait(navegador, 5).until(  
            EC.url_to_be('http://www.automationpractice.pl/index.php?controller=my-account')
        )
    except Exception as e:
        #TODO otimiza em tempo
        # Se login falhou, captura o erro
        try:
            captura_erros_login(navegador)
        except Exception as e:
            raise


def captura_erros_login(navegador):
    """Captura mensagens de erro exibidas na página e lança exceções conforme o erro."""
    # Aumentando o tempo de espera para garantir que o erro seja capturado
    erro_elemento = WebDriverWait(navegador, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'alert-danger'))
    )
    
    # Extrai o texto do erro
    mensagem_erro = erro_elemento.text
    # Remove quebras de linha e espaços extras
    mensagem_erro = re.sub(r'\s+', ' ', mensagem_erro).strip()
    
    # Verifica o tipo de erro e lança a exceção correspondente
    if "Invalid email address." in mensagem_erro:
        raise InvalidEmailException("O endereço de e-mail fornecido é inválido.")
    elif "Invalid password." in mensagem_erro:
        raise InvalidPasswordException("A senha fornecida é inválida.")
    elif "Authentication failed." in mensagem_erro:
        raise AuthenticationFailedException("Email ou senha incorretos.")
    else:
        raise RuntimeError(f"Erro desconhecido: {mensagem_erro}")  # Lançando exceção para erro desconhecido