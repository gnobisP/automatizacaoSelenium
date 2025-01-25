class InvalidEmailException(Exception):
    """Exceção para e-mail inválido."""
    pass

class InvalidPasswordException(Exception):
    """Exceção para senha inválida."""
    pass

class AuthenticationFailedException(Exception):
    """Exceção para credenciais inválida."""
    pass
