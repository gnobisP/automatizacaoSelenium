"""
Cenário: O usuário já possui uma conta e deseja alterar a senha.

Dado que o usuário esteja na página de login do "Automation Practice".

Quando o usuário clicar na opção para alterar a senha e inserir um email válido.

Então, a página deve exibir uma mensagem informando que um e-mail foi enviado para a mudança de senha 
"""
import time


from uteis.exceptionsLogin import InvalidPasswordException, InvalidEmailException, AuthenticationFailedException
from uteis.moduloLogin import alteraSenhaUsuario
from uteis.moduloConfiguracoes import inicia_servico

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
    navegador = inicia_servico()

    try:
        alteraSenhaUsuario(navegador, usuario)
        print("Email para mudança de senha enviado!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    time.sleep(7)
    navegador.quit()




