# Classe para representar uma data (Dia, Mês e Ano)
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        # Retorna a data no formato "DD/MM/YYYY"
        return f"{self.day:02d}/{self.month:02d}/{self.year}"