"""
Cenário 1: Login bem-sucedido após tentativa com senha incorreta

Dado que o usuário possui uma conta válida no sistema e está na página de login do "Automation Practice".

Quando o usuário inserir o e-mail correto e uma senha incorreta na primeira tentativa, e após isso inserir a senha correta em uma segunda tentativa.

Então a página, primeiramente, deve mostrar que as credenciais estão incorretas e, na segunda tentativa, redirecioná-lo para a área "my-account".
"""
import time

from uteis.moduloLogin import realiza_login
from uteis.moduloConfiguracoes import inicia_servico

from classes.Usuario import Usuario, Date
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

    navegador = inicia_servico()
    try:
        realiza_login(navegador, usuario)
        print("Login realizado com sucesso")
    except Exception as e:
        print(f"Erro ao realizar login: {e}")
    time.sleep(7)

    usuario.password = "1234567",
    try:
        realiza_login(navegador, usuario)
        print("Login realizado com sucesso")
    except Exception as e:
        print(f"Erro ao realizar login: {e}")
    time.sleep(7)


    navegador.quit()


