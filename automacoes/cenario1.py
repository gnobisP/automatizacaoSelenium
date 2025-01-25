from uteis.modulo1 import inicia_servico, realiza_login, compra_uma_camisa
import time

"""
Cenário 1: Login bem-sucedido
Condição: O usuário já tem uma conta válida no sistema.
Dado que o usuário esteja na página de login do "Automation Practice".
Quando ele insere um e-mail válido e uma senha correta e clica no botão "Sign in".
Então a página deve redirecioná-lo para a área "my-account".
"""

if __name__ == "__main__":
    navegador = inicia_servico()
    if(realiza_login(navegador, 'testeGustavoPimenta@teste.com', 'testeGustavoPimenta')):
        print("sucess - login successful")
    else:
        print("fail - login unsuccessful")
    time.sleep(7)
    navegador.quit()


