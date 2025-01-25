import random
import string
from datetime import datetime

def gerar_email_unico():
    # Gerando uma string aleatória para o e-mail
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"usuario_{timestamp}_{random_string}@example.com"