# ******************************************************************************
# Makefile - Guia de Uso
# 
# Este Makefile é compatível com Linux e Windows e gerencia a execução de 
# scripts de automação. Siga as instruções abaixo para utilizá-lo:
#
# --- Como Usar ---

# - Para executar o script run.sh (Linux):
#   make run-sh
#
# - Para executar o arquivo run.bat (Windows):
#   make run-bat
#
# - Para executar cenários específicos:
#   make cenario1  # Executa o cenário 1
#   make cenario2  # Executa o cenário 2
#   make cenario3  # Executa o cenário 3
#
# - Para limpar arquivos temporários:
#   make clean
#
# ******************************************************************************

# Defina o nome dos arquivos
RUN_SH = run.sh
RUN_BAT = run.bat

# Detecta o sistema operacional
ifeq ($(OS),Windows_NT)
    # Comandos específicos para Windows
    DEL = del
    CHMOD = echo "No need for chmod on Windows"
    PYTHON = python
else
    # Comandos específicos para Linux
    DEL = rm -f
    CHMOD = chmod +x
    PYTHON = python3
endif

# Tarefas principais
.PHONY: all run-sh run-bat cenario1 cenario2 cenario3 clean

# Tarefa padrão que executa tudo
all: run-sh run-bat cenario1 cenario2 cenario3

# Executa o script run.sh (no Linux)
run-sh:
	@echo "Executando o script $(RUN_SH)..."
	$(CHMOD) $(RUN_SH) 
	@if [ "$(OS)" != "Windows_NT" ]; then \
		bash $(RUN_SH); \
	else \
		echo "No Windows, o script run.sh não será executado utilize run.bat."; \
	fi

# Executa o arquivo run.bat (somente no Windows)
run-bat:
	@echo "Executando o arquivo $(RUN_BAT)..."
	@if [ "$(OS)" = "Windows_NT" ]; then \
		$(PYTHON) $(RUN_BAT); \
	else \
		echo "No Linux, o arquivo run.bat não será executado utilize run.sh."; \
	fi

# Executa o primeiro cenário de automação
cenario1:
	@echo "Iniciando o cenário 1..."
	$(PYTHON) -m automacoes.cenario1

# Executa o segundo cenário de automação
cenario2:
	@echo "Iniciando o cenário 2..."
	$(PYTHON) -m automacoes.cenario2

# Executa o terceiro cenário de automação
cenario3:
	@echo "Iniciando o cenário 3..."
	$(PYTHON) -m automacoes.cenario3

# Limpeza (caso queira limpar arquivos gerados ou desnecessários)
clean:
	@echo "Limpando arquivos temporários..."
	$(DEL) *.o *.log
