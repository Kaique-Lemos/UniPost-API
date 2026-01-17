# 🧑‍🎓 UniPost_Api – Backend do Sistema UniPost

## 📖 Descrição
UniPost_Api é o backend do sistema **UniPost**, desenvolvido em **Django** com **Django REST Framework**.  
Ele fornece uma API RESTful completa para gerenciamento de alunos, que é consumida pelo [UniPost (Frontend)](https://github.com/Crystian-Paz/UniPost). A API permite cadastrar, listar, editar e excluir registros, garantindo persistência de dados em **SQLite**.

---

## 🚀 Funcionalidades
- ✅ Autenticação de usuários (login/logout, registro)  
- ✅ Gerenciamento de alunos (CRUD)  
- ✅ Exposição de API RESTful para consumo pelo frontend  
- ✅ Persistência de dados em SQLite  
- ✅ Permissões e validações de acesso  

---

## 🧩 Tecnologias Utilizadas
- Django  
- Django REST Framework (DRF)  
- SQLite (banco de dados)  

---

## ⚙️ Estrutura do Projeto

```text
UniPost_Api/
├── manage.py
├── db.sqlite3
├── UniPost_Api/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── api/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── ...
```
---

## 🧠 Endpoints Principais

```text
Método   URL                     Função
GET      /api/alunos/            Listar todos os alunos
POST     /api/alunos/            Criar novo aluno
PUT      /api/alunos/{id}/       Editar dados de um aluno
DELETE   /api/alunos/{id}/       Excluir um aluno
```

---

## 🧠 Arquitetura do Sistema

```text
[Usuário] 
    |
    v
[Frontend React] <--Axios--> [API Django REST] <--SQLite--> [Banco de Dados]
```
- O React envia requisições HTTP (GET, POST, PUT, DELETE) para a API Django.
- A API Django processa os dados, aplica regras de negócio e persiste informações no SQLite.
- As respostas da API são exibidas pelo frontend para o usuário.

---

## 🧠 Como Executar o Backend Localmente

Este repositório contém apenas o backend. Para a interface de usuário, acesse o repositório do [UniPost (Frontend)](https://github.com/Kaique-Lemos/UniPost.git).

1️⃣ **Clonar o repositório:**

```bash

git clone https://github.com/Crystian-Paz/UniPost_Api.git

```

2️⃣ **Criar o ambiente virtual:**

```bash

# Cria a pasta 'venv'
python -m venv venv

```

3️⃣ **Ativar o ambiente virtual (Escolha UM):**

Em Linux / macOS (Terminal Bash/Zsh):

```Bash

source venv/bin/activate

```


Em Windows (PowerShell):

```PowerShell

venv\Scripts\Activate.ps1

```

Em Windows **(Git Bash - Recomendado)**:

```Bash

source venv/Scripts/activate

```

4️⃣ **Instalar dependências e aplicar migrações:**

(Após ativar, seu terminal deve mostrar (venv) no início da linha)

```Bash

# (Opcional, mas recomendado) Atualizar o pip
pip install --upgrade pip

# Instalar TODAS as dependências do projeto
pip install -r requirements.txt

# Aplicar as migrações (criar o banco de dados db.sqlite3)
python manage.py migrate

```

5️⃣ **Rodar o servidor:**

```Bash

python manage.py runserver

```

O backend estará rodando em: ``http://127.0.0.1:8000/``

---
## 🧱 Banco de Dados

O projeto utiliza **SQLite**, que salva os dados localmente no arquivo `db.sqlite3`.  
Todos os dados inseridos via frontend são persistidos automaticamente.

---

## 🧾 Histórias de Usuário

- **Cadastrar Aluno** – Como usuário, quero adicionar um novo aluno com nome, curso e matrícula.  
- **Listar Alunos** – Como usuário, quero visualizar todos os alunos cadastrados.  
- **Editar Aluno** – Como usuário, quero alterar os dados de um aluno existente.  
- **Excluir Aluno** – Como usuário, quero remover um aluno cadastrado.  

---

## 👨‍💻 Desenvolvido por

- **Crystian da Paz Silva**  
- **Bruno Nogueira da Rocha**  
- **Kaique Lemos da Silva**  
- **Pedro Vinícius de Arruda Barbosa**
- **Matheus Felipe Vilas Boas de Araujo Silva**
- **Gustavo Teixeira Bione**
- **Thiago de Lima Freire**
- **Lucas Ferraz Valença Parente**

  
💼 Projeto de aplicação web (Django + React)  
📚 Persistência de dados com SQLite  
🗓️ 2025  

---

## 🔗 Links
- **Backend (UniPost_Api)**: [https://github.com/Crystian-Paz/UniPost_Api](https://github.com/Kaique-Lemos/UniPost-API.git)  
- **Frontend (UniPost)**: [https://github.com/Crystian-Paz/UniPost](https://github.com/Kaique-Lemos/UniPost.git)
