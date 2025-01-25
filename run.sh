#!/bin/bash

# Inicia o primeiro cenário de automação
# Executa o módulo 'cenario1' do pacote 'automacoes'
echo "Executando o cenário 1..."
python3 -m automacoes.cenario1
echo "Cenário 1 concluído."

# Inicia o segundo cenário de automação
# Executa o módulo 'cenario2' do pacote 'automacoes'
echo "Executando o cenário 2..."
python3 -m automacoes.cenario2
echo "Cenário 2 concluído."

# Inicia o terceiro cenário de automação
# Executa o módulo 'cenario3' do pacote 'automacoes'
echo "Executando o cenário 3..."
python3 -m automacoes.cenario3
echo "Cenário 3 concluído."

