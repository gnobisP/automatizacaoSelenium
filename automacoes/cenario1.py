"""
Cenário 1: Login bem-sucedido após tentativa com senha incorreta

Dado que o usuário possui uma conta válida no sistema e está na página de login do "Automation Practice".

Quando o usuário inserir o e-mail correto e uma senha incorreta na primeira tentativa, e após isso inserir a senha correta em uma segunda tentativa.

Então a página, primeiramente, deve mostrar que as credenciais estão incorretas e, na segunda tentativa, redirecioná-lo para a área "my-account".
"""
import time
import sys

# Imports internos
from uteis.moduloLogin import realiza_login
from uteis.moduloConfiguracoes import inicia_servico
from uteis.exceptionsLogin import LoginInvalidPasswordException, LoginInvalidEmailException, LoginAuthenticationFailedException

# Classes internas
from classes.Usuario import Usuario, Date

def testeCenario1(navegador, usuario):
    """Acessa a tela de login com usuario e senha"""
    try:
        realiza_login(navegador, usuario)
        print("Login realizado com sucesso")

    except LoginInvalidEmailException as e0:
        print(f"Erro: {e0}")

    except LoginInvalidPasswordException as e1:
        print(f"Erro: {e1}")

    except LoginAuthenticationFailedException as e2:
        print(f"Erro: {e2}")
        
    except Exception as e:
        print(f"Erro Inesperado: {e}")
        navegador.quit()
        sys.exit(-1)

    time.sleep(4) #tempo para mostrar a tela da aplicacao

    


if __name__ == "__main__":

    # Criando uma instância da classe Usuario
    usuario = Usuario(
        title="Mrs",
        first_name="John",
        last_name="Doe",
        email="john1234567foe@example.com",
        password="12345678",
        date_of_birth=Date("15", "1", "1990")
    )
    navegador = inicia_servico() #inicia o selenium na página inicial

    testeCenario1(navegador, usuario) #Acesso com credenciais incorretas

    usuario.password = "1234567" #modifica para a senha correta

    testeCenario1(navegador, usuario) #Acesso com credenciais corretas

    navegador.quit()


