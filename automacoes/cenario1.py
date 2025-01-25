"""
Cenário 1: Login bem-sucedido
Condição: O usuário já tem uma conta válida no sistema.
Dado que o usuário esteja na página de login do "Automation Practice".
Quando ele insere um e-mail válido e uma senha correta e clica no botão "Sign in".
Então a página deve redirecioná-lo para a área "my-account".
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
        email="john123456foe@example.com",
        password="1234567",
        date_of_birth=Date("15", "1", "1990")
    )

    navegador = inicia_servico()
    try:
        realiza_login(navegador, usuario)
        print("Login realizado com sucesso")
    except Exception as e:
        print("Erro ao realizar login")
    
    time.sleep(7)
    navegador.quit()


