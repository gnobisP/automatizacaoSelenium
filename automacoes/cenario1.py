from uteis.modulo1 import inicia_servico, realiza_login, compra_uma_camisa

if __name__ == "__main__":
    navegador = inicia_servico()
    realiza_login(navegador, 'testeGustavoPimenta@teste.com', 'testeGustavoPimenta')
    compra_uma_camisa(navegador)
