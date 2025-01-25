from classes.Date import Date

# Classe para representar um usuário
class Usuario:
    def __init__(self, title, first_name, last_name, email, password, date_of_birth):
        self.title = title  # Mr ou Mrs
        self.first_name = first_name  # Primeiro nome
        self.last_name = last_name  # Sobrenome
        self.email = email  # Email
        self.password = password  # Senha
        self.date_of_birth = date_of_birth  # Instância da classe Date para data de nascimento
    
    def exibir_info(self):
        # Exibe as informações do usuário
        print(f"Title: {self.title}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Date of Birth: {self.date_of_birth}")
