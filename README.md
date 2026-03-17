# 🧾 Mini ERP - Sistema de Gestão de Mercado

Sistema web desenvolvido com Django para gerenciamento de um mini ERP de mercado, contemplando controle de clientes, produtos, pedidos e estoque.

---

## 🚀 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de simular um sistema ERP real, aplicando boas práticas de desenvolvimento backend com Django e organização modular por domínio.

A aplicação permite:

* Gestão de clientes
* Cadastro e controle de produtos
* Criação e gerenciamento de pedidos
* Controle de estoque
* Estrutura preparada para evolução (dashboard, relatórios, autenticação, etc)

---

## 🧠 Arquitetura

O projeto segue uma arquitetura modular baseada em domínios:

```
apps/
├── core        # Configurações centrais e utilidades
├── customers   # Gestão de clientes
├── products    # Gestão de produtos
├── orders      # Gestão de pedidos
├── inventory   # Controle de estoque
```

Outras pastas:

```
config/     # Configurações do Django (settings, urls, wsgi, asgi)
templates/  # Templates HTML globais
static/     # Arquivos estáticos (CSS, JS, imagens)
media/      # Upload de arquivos
```

---

## 🛠️ Tecnologias Utilizadas

* Python 3.x
* Django
* SQLite (ambiente de desenvolvimento)
* HTML5 + Tailwind CSS (interface)
* Git & GitHub

---

## ⚙️ Instalação e Configuração

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/erp_project.git
cd erp_project
```

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Rodar migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Executar o servidor

```bash
python manage.py runserver
```

Acesse em:
👉 http://127.0.0.1:8000/

---

## 📦 Funcionalidades

### 👤 Clientes

* Cadastro de clientes
* Edição e exclusão
* Listagem com filtros

### 📦 Produtos

* Cadastro de produtos
* Controle de preço
* Associação com estoque

### 🧾 Pedidos

* Criação de pedidos
* Relacionamento com clientes
* Associação com múltiplos produtos

### 📊 Estoque

* Controle de entrada e saída
* Atualização automática baseada em pedidos

---

## 🔗 Relacionamentos do Sistema

* Um cliente pode ter vários pedidos
* Um pedido pode conter vários produtos
* Produtos possuem controle de estoque

---

## 📈 Roadmap (Próximas melhorias)

* [ ] Dashboard com métricas
* [ ] Autenticação de usuários
* [ ] Controle de permissões
* [ ] Relatórios financeiros
* [ ] API com Django REST Framework
* [ ] Integração com frontend (React ou HTMX)

---

## 🧪 Testes

(Em desenvolvimento)

---

## 📌 Boas práticas aplicadas

* Separação por domínio (apps)
* Código organizado e escalável
* Preparado para crescimento do projeto
* Uso de padrões do Django

---

## 👨‍💻 Autor

Desenvolvido por [Seu Nome]

---

## 📄 Licença

Este projeto está sob a licença MIT.
