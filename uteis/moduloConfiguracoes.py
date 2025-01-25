from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def inicia_servico(): 
    """Inicia o navegador e acessa o site principal."""
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get("http://www.automationpractice.pl/index.php?id_category=3&controller=category")
    return navegador