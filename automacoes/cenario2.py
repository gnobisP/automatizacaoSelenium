"""
Cenário: Verificar mensagem de erro para e-mail e senha inválidos
Dado que o usuário esteja na página de login do "Automation Practice".
Quando o usuário inserir um e-mail inválido ou uma senha inválida e clicar no botão "Sign in".
Então a página deve exibir uma mensagem de erro indicando que as credenciais fornecidas são inválidas
"""
import time


from uteis.exceptionsLogin import InvalidPasswordException, InvalidEmailException, AuthenticationFailedException
from uteis.moduloLogin import realiza_login
from uteis.moduloConfiguracoes import inicia_servico


if __name__ == "__main__":

    navegador = inicia_servico()

    #Email inválido
    try:
        realiza_login(navegador, "gmail.com", "1123456as")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    #Senha inválida
    try:
        realiza_login(navegador, "teste@gmail.com", "1")
    except Exception as e:
        print(f"Erro inesperado: {e}")

 



