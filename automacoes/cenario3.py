"""
Cenário: Verificar cadastro de novo usuário no sistema

Condição: O Usuário não possui uma conta cadastrada

Dado que o usuário esteja na página de login do "Automation Practice".

Quando o usuário inserir um e-mail válido no campo "Create an account" e clicar no botão correspondente.

Então ele deve ser redirecionado para a página de registro, onde poderá preencher suas informações pessoais para criar uma nova conta.
"""
import time
import sys

# Imports internos
from uteis.moduloConfiguracoes import inicia_servico
from uteis.moduloLogin import cadastrarUsuario
from uteis.utilidadesLogin import gerar_email_unico
from uteis.exceptionsCadastro import (
    CadastroLastNameRequiredException,
    CadastroFirstNameRequiredException,
    CadastroPasswordRequiredException,
    CadastroInvalidDateOfBirthException,
    CadastroAuthenticationFailedException
)
# Classes internas
from classes.Usuario import Usuario, Date

if __name__ == "__main__":

    # Criando uma instância da classe Usuario
    usuario = Usuario(
        title="",
        first_name="John",
        last_name="Doe",
        email="",
        password="1234567",
        date_of_birth=Date("15", "1", "1990")
    )
    usuario.email = gerar_email_unico() #gera um emailUnico para evitar duplicidade
    navegador = inicia_servico() #inicia o selenium na página inicial

    #cadastra um novo usuario
    try:
        cadastrarUsuario(navegador, usuario)
        print("Usuario Cadastrado com Sucesso")
    except CadastroLastNameRequiredException as e:
        print(f"Erro: {e}")

    except CadastroFirstNameRequiredException as e:
        print(f"Erro: {e}")

    except CadastroPasswordRequiredException as e:
        print(f"Erro: {e}")

    except CadastroInvalidDateOfBirthException as e:
        print(f"Erro: {e}")

    except CadastroAuthenticationFailedException as e:
        print(f"Erro: {e}")

    except Exception as e:
        print(f"Erro Inesperado: {e}")
        navegador.quit()
        sys.exit(-1)

    
    time.sleep(7)
    navegador.quit()
    



 



