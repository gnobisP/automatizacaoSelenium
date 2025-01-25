# Desafio Técnico - Quality Assurance Automation Engineer
Este repositório contém a implementação de três cenários de teste automatizados utilizando o site [Automation Practice](http://automationpractice.pl/index.php?controller=authentication&back=my-account). O desafio foi desenvolvido para avaliar habilidades de automação e cobertura de casos de teste.

## 📑 Cenários de Teste

### 1️⃣ **Login bem-sucedido após tentativa com senha incorreta**
- **Dado** que o usuário possui uma conta válida e está na página de login do "Automation Practice".
- **Quando** o usuário inserir:
  - Na **primeira tentativa**: um e-mail correto e uma senha incorreta.
  - Na **segunda tentativa**: o e-mail correto e a senha correta.
- **Então**:
  - Primeiramente, a página exibirá uma mensagem de erro sobre credenciais incorretas.
  - Após o segundo login bem-sucedido, o usuário será redirecionado para a página "my-account".

---

### 2️⃣ **Alteração de senha por e-mail**
- **Dado** que o usuário já possui uma conta e está na página de login do "Automation Practice".
- **Quando** o usuário clicar na opção de "Alterar Senha" e inserir um e-mail válido.
- **Então** a página exibirá uma mensagem informando que um e-mail foi enviado para a alteração da senha.

---

### 3️⃣ **Cadastro de novo usuário**
- **Condição**: O usuário não possui uma conta cadastrada.
- **Dado** que o usuário está na página de login do "Automation Practice".
- **Quando** o usuário inserir um e-mail válido no campo "Create an account" e clicar no botão correspondente.
- **Então** o sistema redirecionará o usuário para a página de registro, onde ele poderá preencher suas informações pessoais para criar uma nova conta.

---

## 🛠 Tecnologias Utilizadas
- **Framework de Automação**: [Selenium] 
- **Linguagem de Programação**: [Python]
- **IDE**: [VSCode]

## 🚀 Como Executar os Testes

