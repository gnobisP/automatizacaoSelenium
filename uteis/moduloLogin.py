import re
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


from uteis.exceptionsLogin import InvalidPasswordException, InvalidEmailException, AuthenticationFailedException
from uteis.exceptionsCadastro import LastNameRequiredException, FirstNameRequiredException, PasswordRequiredException, InvalidDateOfBirthException, AuthenticationFailedException 


def realiza_login(navegador, usuario):
    """Realiza login no site."""
    navegador.get('http://www.automationpractice.pl/index.php?controller=authentication&back=my-account')
    
    # Preenche o campo de e-mail
    email_field = WebDriverWait(navegador, 5).until(  # Espera reduzida para 5 segundos
        EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]'))
    )
    email_field.send_keys(usuario.email)
    
    # Preenche o campo de senha
    password_field = WebDriverWait(navegador, 5).until(  # Espera reduzida para 5 segundos
        EC.visibility_of_element_located((By.XPATH, '//*[@id="passwd"]'))
    )
    password_field.send_keys(usuario.password)
    
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


def captura_erros_cadastro(navegador):
    """Captura mensagens de erro exibidas na página e lança exceções conforme o erro."""
    try:
        # Aguarda até que o alerta de erro esteja visível
        alert_box = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'alert-danger'))
        )

        # Captura todas as mensagens dentro da lista <ol>
        error_list = alert_box.find_elements(By.TAG_NAME, 'li')

        error_message = "" 
        for index, error in enumerate(error_list, start=1):
            error_message += f"Erro {index}: {error.text.strip().lower()} "  # Concatenar com um separador claro, como um espaço ou uma quebra de linha

    except Exception as e:
        raise
    finally:
        # Lançando exceções com base nas mensagens de erro
        if "lastname is required" in error_message:
            raise LastNameRequiredException("Last name is required.")
        elif "firstname is required" in error_message:
            raise FirstNameRequiredException("First name is required.")
        elif "passwd is required" in error_message:
            raise PasswordRequiredException("Password is required.")
        elif "invalid date of birth" in error_message:
            raise InvalidDateOfBirthException("Invalid date of birth.")
        elif "authentication failed" in error_message or "invalid credentials" in error_message:
            raise AuthenticationFailedException("Authentication failed.")

def cadastrarUsuario(navegador, usuario):
    """Cadastra usuario no site."""
    navegador.get('http://www.automationpractice.pl/index.php?controller=authentication&back=my-account')
    
    try:
        # Acessar a página de cadastro (redundante, pois já foi acessada acima)
        # navegador.get('http://www.automationpractice.pl/index.php?controller=authentication&back=my-account')

        # Preencher o campo de email
        email_field = WebDriverWait(navegador, 20).until(
            EC.visibility_of_element_located((By.ID, 'email_create'))
        )
        email_field.send_keys(usuario.email)

        # Clicar no botão para criar conta
        create_account_button = WebDriverWait(navegador, 20).until(
            EC.element_to_be_clickable((By.ID, 'SubmitCreate'))
        )
        create_account_button.click()

        # Aguarde o carregamento do elemento "days", elemento qualquer, o importante é a página carregar
        day_dropdown = WebDriverWait(navegador, 20).until(
            EC.presence_of_element_located((By.ID, 'days'))
        )

        #Roda Script para preencher um grande quantidade de dados (muito dor, sofrimento, mas deu certo :))
        preencheFormulario(navegador, usuario)
  
        # Clicar no botão de envio
        submit_button = WebDriverWait(navegador, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="submitAccount"]'))
        )
        submit_button.click()

    except Exception as e:
        raise e
    
    try:
        # Espera até que a URL seja a esperada
        WebDriverWait(navegador, 5).until(  
            EC.url_to_be('http://www.automationpractice.pl/index.php?controller=my-account')
        )
    except Exception as e:
        # Se o login falhou, captura o erro
        try:
            captura_erros_cadastro(navegador)
        except Exception as e:
            raise e        
   
def preencheFormulario(navegador, usuario):
    navegador.execute_script("""
        // Selecionar o radio button (Mr/Mrs)
        if(arguments[0] === 'Mr' || arguments[0] === 'Mrs')
            document.getElementById('id_gender' + (arguments[0] === 'Mr' ? '1' : '2')).click();
        
        // Preencher o primeiro nome
        document.getElementById('customer_firstname').value = arguments[1];

        // Preencher o sobrenome
        document.getElementById('customer_lastname').value = arguments[2];

        // Preencher a senha
        document.getElementById('passwd').value = arguments[3];

        // Selecionar o dia de nascimento
        let dayDropdown = document.getElementById('days');
        if (dayDropdown) {
            dayDropdown.value = arguments[4];
            dayDropdown.dispatchEvent(new Event('change'));
        }

        // Selecionar o mês de nascimento
        let monthDropdown = document.getElementById('months');
        if (monthDropdown) {
            monthDropdown.value = arguments[5];
            monthDropdown.dispatchEvent(new Event('change'));
        }

        // Selecionar o ano de nascimento
        let yearDropdown = document.getElementById('years');
        if (yearDropdown) {
            yearDropdown.value = arguments[6];
            yearDropdown.dispatchEvent(new Event('change'));
        }

        // Selecionar a opção de newsletter
        let newsletterCheckbox = document.getElementById('newsletter');
        if (newsletterCheckbox && !newsletterCheckbox.checked) {
            newsletterCheckbox.click();
        }
    """, usuario.title, 
        usuario.first_name, 
        usuario.last_name, 
        usuario.password, 
        usuario.date_of_birth.day, 
        usuario.date_of_birth.month, 
        usuario.date_of_birth.year)  # Ano de nascimento    