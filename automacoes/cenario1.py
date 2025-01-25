"""
Cenário 1: Login bem-sucedido
Condição: O usuário já tem uma conta válida no sistema.
Dado que o usuário esteja na página de login do "Automation Practice".
Quando ele insere um e-mail válido e uma senha correta e clica no botão "Sign in".
Então a página deve redirecioná-lo para a área "my-account".
"""

from uteis.moduloLogin import realiza_login
from uteis.moduloConfiguracoes import inicia_servico
import time

if __name__ == "__main__":
    navegador = inicia_servico()
    try:
        realiza_login(navegador, "testeGustavoPimenta@teste.com", "testeGustavoPimenta")
        print("Login realizado com sucesso")
    except Exception as e:
        print("Erro ao realizar login")
    
    time.sleep(7)
    navegador.quit()


