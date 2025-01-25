# Exceção para quando o sobrenome não é fornecido
class CadastroLastNameRequiredException(Exception):
    """Exceção para sobrenome obrigatório."""
    def __init__(self, message="O sobrenome é obrigatório."):
        self.message = message
        super().__init__(self.message)

# Exceção para quando o primeiro nome não é fornecido
class CadastroFirstNameRequiredException(Exception):
    """Exceção para primeiro nome obrigatório."""
    def __init__(self, message="O primeiro nome é obrigatório."):
        self.message = message
        super().__init__(self.message)

# Exceção para quando a senha não é fornecida
class CadastroPasswordRequiredException(Exception):
    """Exceção para senha obrigatória."""
    def __init__(self, message="A senha é obrigatória."):
        self.message = message
        super().__init__(self.message)

# Exceção para data de nascimento inválida (Não preencheu todos campos)
class CadastroInvalidDateOfBirthException(Exception):
    """Exceção para data de nascimento inválida."""
    def __init__(self, message="Data de nascimento inválida."):
        self.message = message
        super().__init__(self.message)

# Exceção para credenciais inválidas no cadastro
class CadastroAuthenticationFailedException(Exception):
    """Exceção para credenciais inválidas."""
    def __init__(self, message="Credenciais inválidas (email ou senha)."):
        self.message = message
        super().__init__(self.message)

# Exceção para quando o e-mail já está registrado
class CadastroEmailAddressAlreadyRegistered(Exception):
    """Uma conta com esse email já existe."""
    def __init__(self, message="Uma conta com esse e-mail já está registrada."):
        self.message = message
        super().__init__(self.message)
