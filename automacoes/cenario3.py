"""
Cenário: Verificar cadastro de novo usuário no sistema

Condição: O Usuário não possui uma conta cadastrada

Dado que o usuário esteja na página de login do "Automation Practice".

Quando o usuário inserir um e-mail válido no campo "Create an account" e clicar no botão correspondente.

Então ele deve ser redirecionado para a página de registro, onde poderá preencher suas informações pessoais para criar uma nova conta.
"""
import time

from uteis.moduloConfiguracoes import inicia_servico
from uteis.moduloLogin import cadastrarUsuario
from classes.Usuario import Usuario, Date
from uteis.utilidadesLogin import gerar_email_unico

if __name__ == "__main__":

    # Criando uma instância da classe Usuario
    usuario = Usuario(
        title="Mrs",
        first_name="John",
        last_name="Doe",
        email="",
        password="1234567",
        date_of_birth=Date("15", "1", "1990")
    )
    usuario.email = gerar_email_unico()
    navegador = inicia_servico()
    try:
        cadastrarUsuario(navegador, usuario)
        print("Usuario Cadastrado com Sucesso")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    
    time.sleep(7)
    navegador.quit()
    



 



