# 🗄️ CRUD de Usuários com SQLite e Python

Este projeto é uma aplicação de **CRUD (Create, Read, Update, Delete)** desenvolvida em **Python**, utilizando o banco de dados **SQLite**. A aplicação é executada via terminal, permitindo gerenciar usuários de forma simples e eficiente, com persistência de dados em um banco local.

## 📋 Funcionalidades

- ✅ Criar usuários com nome e idade  
- ✅ Listar todos os usuários cadastrados no banco  
- ✅ Buscar usuário por ID  
- ✅ Atualizar informações do usuário  
- ✅ Deletar usuários pelo ID  
- ✅ Menu interativo em terminal

## 🧰 Tecnologias Utilizadas

- **Python 3.x**
- **SQLite3** (banco de dados relacional embutido)

## 🛠️ Como Executar

1. Certifique-se de ter o **Python 3.x** instalado.
2. Salve o código em um arquivo chamado `crud_sqlite.py`.
3. Execute o script no terminal:

```bash
python crud_sqlite.py 
```
O banco de dados será criado automaticamente como crud_usuarios.bd no mesmo diretório.

# 🗃️ Estrutura da Tabela
O projeto cria automaticamente a tabela usuarios com os seguintes campos:

CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
);

Cada usuário possui:

id: Identificador único (gerado automaticamente)

nome: Nome do usuário

idade: Idade do usuário

# 🎯 Objetivo
Este projeto tem fins educacionais e demonstra como utilizar SQLite com Python para construir aplicações com persistência de dados. É uma ótima base para quem deseja evoluir para aplicações mais robustas com interfaces gráficas ou APIs.
