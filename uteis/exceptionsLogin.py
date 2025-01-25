#Excessao para email invalido(não segue o padrao nome@email.com)
class LoginInvalidEmailException(Exception):
    """Exceção para e-mail inválido."""
    def __init__(self, message="O e-mail fornecido é inválido."):
        self.message = message
        super().__init__(self.message)

# Exceção para senha invalida (menos de 6 caracteres)
class LoginInvalidPasswordException(Exception):
    """Exceção para senha inválida."""
    def __init__(self, message="A senha fornecida é inválida."):
        self.message = message
        super().__init__(self.message)

# Exceção para Senha ou email errado
class LoginAuthenticationFailedException(Exception):
    """Exceção para credenciais inválidas."""
    def __init__(self, message="Email ou senha incorretos."):
        self.message = message
        super().__init__(self.message)
