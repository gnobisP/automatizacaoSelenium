# Desafio Técnico - Quality Assurance Automation Engineer
Este repositório contém a implementação de três cenários de teste automatizados utilizando o site [Automation Practice](http://automationpractice.pl/index.php?controller=authentication&back=my-account). O desafio foi desenvolvido para avaliar habilidades de automação e cobertura de casos de teste.

## 🛠 Tecnologias Utilizadas (Windows)
- **Framework de Automação**: [Selenium - 4.28.1] 
- **Linguagem de Programação**: [Python - 3.13.1]
- **Biblioteca Python**: [webdriver_manager - 3.8.5]
- **IDE**: [VSCode]
- **Navegador**: [Google Chrome]

## 🛠 Tecnologias Utilizadas (Linux)
- **Framework de Automação**: [Selenium - 4.28.1] 
- **Linguagem de Programação**: [Python3 - 3.12.3] 
- **Biblioteca Python**: [webdriver_manager - 3.8.5]
- **IDE**: [VSCode]
- **Navegador**: [Google Chrome]

## 🚀 Como rodar o Projeto
  - **Clone o repositório:**
```sh
  git clone https://github.com/gnobisP/automatizacaoSelenium.git
  cd AUTOMATIZACAOSELENIUM
```


### Windows:
  - **Instalando dependências:**
    - Instale o [Google Chrome](https://www.google.com/intl/pt-BR/chrome/)
    - Instale o [Python](https://www.python.org/downloads/release/python-3123/)
    - instale o Selenium: 
      ```sh
      pip install selenium
      ```
    - instale o webdriver_manager 
      ```sh
      pip install webdriver_manager
      ```

  - **Executando cenârios:**
    - **Cenário 1**: 
      ```sh
      python -m automacoes.cenario1
      ```
    - **Cenário 2**: 
      ```sh
      python -m automacoes.cenario2
      ```
    - **Cenário 3**: 
      ```sh
      python -m automacoes.cenario3
      ```

### Linux:
  - **Instalando dependências:**
    - Instale o [Google Chrome](https://www.google.com/chrome/?platform=linux/)
    - Instale as dependências:
      ```sh
      make install
      ```

  - **Executando cenârios:**
    - **Cenário 1**: 
      ```sh
      make cenario1
      ```
    - **Cenário 2**: 
      ```sh
      make cenario2
      ```
    - **Cenário 3**: 
      ```sh
      make cenario3
      ```

## 📑 Cenários de Teste

### 1️⃣ **Login bem-sucedido após tentativa com senha incorreta**
- **Dado** que o usuário possui uma conta válida e está na página de login do "Automation Practice".
- **Quando** o usuário inserir:
  - Na **primeira tentativa**: um e-mail correto e uma senha incorreta.
  - Na **segunda tentativa**: o e-mail correto e a senha correta.
- **Então**:
  - Primeiramente, a página exibirá uma mensagem de erro sobre credenciais incorretas.
  - Após o segundo login bem-sucedido, o usuário será redirecionado para a página "my-account".

- **Excessões tratadas**: LoginInvalidPasswordException, LoginInvalidEmailException, LoginAuthenticationFailedException
---

### 2️⃣ **Alteração de senha por e-mail**
- **Dado** que o usuário já possui uma conta e está na página de login do "Automation Practice".
- **Quando** o usuário clicar na opção de "Alterar Senha" e inserir um e-mail válido.
- **Então** a página exibirá uma mensagem informando que um e-mail foi enviado para a alteração da senha.

- **Excessões tratadas**: InvalidEmailException
---

### 3️⃣ **Cadastro de novo usuário**
- **Condição**: O usuário não possui uma conta cadastrada.
- **Dado** que o usuário está na página de login do "Automation Practice".
- **Quando** o usuário inserir um e-mail válido no campo "Create an account" e clicar no botão correspondente.
- **Então** o sistema redirecionará o usuário para a página de registro, onde ele poderá preencher suas informações pessoais para criar uma nova conta.

- **Excessões tratadas**: CadastroLastNameRequiredException, CadastroFirstNameRequiredException, CadastroPasswordRequiredException, CadastroInvalidDateOfBirthException, CadastroAuthenticationFailedException.
---

# Estrutura de Arquivos do Projeto

Este repositório contém a automação de cenários relacionados à funcionalidade de login do site "Automation Practice". Abaixo está a descrição detalhada da estrutura de pastas e arquivos do projeto:

## 📁 Estrutura do Projeto

### 📂 `automacoes`
Contém os arquivos responsáveis pela automação dos cenários de teste relacionados à funcionalidade de login. 
Cada arquivo neste diretório representa um cenário de teste automatizado:

- **`cenario1.py`**: Automação para o cenário de login bem-sucedido após tentativa com senha incorreta.
- **`cenario2.py`**: Automação para o cenário de alteração de senha por e-mail.
- **`cenario3.py`**: Automação para o cenário de cadastro de novo usuário.

---

### 📂 `classes`
Armazena as classes utilizadas no projeto relacionadas à funcionalidade de login. Estas classes são usadas para modelar as entidades e comportamentos necessários:

- **`Usuario.py`**: Classe para manipulação e armazenamento de informações do usuário.
- **`Date.py`**: Classe para lidar com operações relacionadas a datas (se aplicável).

---

### 📂 `uteis`
Contém funcionalidades e módulos auxiliares que suportam o projeto, especificamente voltados para as operações de login:

- **`exceptionsCadastro.py`**: Gerencia exceções relacionadas ao cadastro de novos usuários.
- **`exceptionsLogin.py`**: Trata exceções específicas do processo de login.
- **`moduloLogin.py`**: Funções que implementam operações fundamentais de login.
- **`moduloRealizaCompra.py`**:  Modulo de teste de compra do cenário
- **`moduloConfiguracoes.py`**: Configurações gerais relacionadas à automação e login.
- **`utilidadesLogin.py`**: Métodos utilitários para suporte ao login, como validações e formatações.

---

### Outros Arquivos
- **`LICENSE`**: Arquivo contendo a licença do projeto.
- **`pyproject.toml`**: Configuração do ambiente Python e dependências do projeto.
- **`run.bat`** e **`run.sh`**: Scripts para execução automatizada dos testes em ambientes Windows e Linux/Mac, respectivamente.
- **`TODO.md`**: Lista de pendências e melhorias futuras para o projeto.
- **`README.md`**: Documentação principal do projeto.

---

## 🛠 Como Navegar no Projeto
Cada pasta possui um papel específico e organiza o código para facilitar a manutenção e expansão do projeto. Caso deseje adicionar novos cenários, utilize a pasta `automacoes`. Para alterações nas funcionalidades principais, edite os arquivos em `uteis`. Novas classes de suporte devem ser adicionadas em `classes`.