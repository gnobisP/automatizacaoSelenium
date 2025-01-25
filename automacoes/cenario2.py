"""
Cenário: O usuário já possui uma conta e deseja alterar a senha.

Dado que o usuário esteja na página de login do "Automation Practice".

Quando o usuário clicar na opção para alterar a senha e inserir um email válido.

Então, a página deve exibir uma mensagem informando que um e-mail foi enviado para a mudança de senha 
"""
import time
import sys

# Imports internos
from uteis.exceptionsLogin import (LoginInvalidEmailException)
from uteis.moduloLogin import alteraSenhaUsuario
from uteis.moduloConfiguracoes import inicia_servico

# Classes internas
from classes.Usuario import Usuario, Date

if __name__ == "__main__":

    usuario = Usuario(
        title="Mrs",
        first_name="John",
        last_name="Doe",
        email="john1234567foe@example.com",
        password="12345678",
        date_of_birth=Date("15", "1", "1990")
    )
    navegador = inicia_servico() #inicia o selenium na página inicial

    #Altera a senha de um usuario
    try:
        alteraSenhaUsuario(navegador, usuario)
        print("Email para mudança de senha enviado!")

    except LoginInvalidEmailException as e2:
        print(f"Erro: {e2}")
        
    except Exception as e:
        print(f"Erro Inesperado: {e}")
        navegador.quit()
        sys.exit(-1)

    time.sleep(7)
    navegador.quit()




