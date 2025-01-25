# Exceção para quando o sobrenome não é fornecido
class LastNameRequiredException(Exception):
    """Exceção para sobrenome obrigatório.""" 
    pass  

class FirstNameRequiredException(Exception):
    """Exceção para primeiro nome obrigatório.""" 
    pass 

class PasswordRequiredException(Exception):
    """Exceção para senha obrigatória."""  
    pass 

class InvalidDateOfBirthException(Exception):
    """Exceção para data de nascimento inválida.""" 
    pass  

class AuthenticationFailedException(Exception):
    """Exceção para credenciais inválidas.""" 
    pass  

class emailEddressAlreadyRegistered(Exception):
    """Uma conta com esse email já existe""" 
    pass  
