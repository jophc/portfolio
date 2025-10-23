# 🛠️ Sistema de Gerenciamento de Portfólio de Design (CRUD Completo)

Este projeto Django implementa um sistema de gerenciamento interno para um portfólio profissional de design de álbuns, atendendo aos requisitos da Atividade Avaliativa.

---

## 🎯 Funcionalidades e Requisitos Cumpridos

| Funcionalidade | Detalhes da Implementação | Requisito Principal |
| :--- | :--- | :--- |
| **Modelagem Relacional (5 Classes)** | Implementado com 5 modelos centrais (`Projeto`, `Servico`, `Testimonial`, `ContactMessage`, `SiteConfig`) com relação **Muitos-para-Muitos** (`Projeto` <-> `Servico`). | **Concluído** |
| **CRUD Completo** | Implementação de Criar, Ler, Atualizar e Excluir registros para as classes `Projeto`, `Servico` e `Testimonial`. | **Concluído** |
| **Paginação** | Implementada nas listas de Projetos e Mensagens. | **Concluído** |
| **Autenticação Personalizada** | Login/Logout e todas as áreas administrativas (`/dashboard/`) protegidas. | **Concluído** |
| **HTMX** | Carrossel de Depoimentos com troca assíncrona (sem recarga de página). | **Bônus** |
| **Imagens** | Upload e exibição de capa de projeto. | **Bônus** |

---

## ⚙️ Instruções para Rodar o Projeto (Para o Professor)

Este sistema utiliza Python 3 e SQLite (banco de dados padrão do Django).

### 1. Configuração Inicial

1.  **Clone o Repositório:**
    ```bash
    git clone [LINK DO SEU REPOSITÓRIO AQUI]
    cd [nome da sua pasta principal]
    ```

2.  **Ative o Ambiente Virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # (Windows)
    # source venv/bin/activate # (Linux/Mac)
    ```

3.  **Instalar Dependências:**
    ```bash
    # Instala o Django e a biblioteca Pillow (necessária para ImageField)
    pip install django Pillow
    ```

### 2. Preparação do Banco de Dados

Se o arquivo `db.sqlite3` não foi incluído (prática recomendada), você precisa criar o banco de dados e aplicar a estrutura:

1.  **Aplicar Migrações:**
    ```bash
    python manage.py makemigrations core
    python manage.py migrate
    ```

2.  **Criar o Superusuário:**
    ```bash
    python manage.py createsuperuser
    ```

### 3. Execução

1.  **Iniciar o Servidor de Desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
2.  **Acessar:**
    * **Página Inicial:** `http://127.0.0.1:8000/`
    * **Área Administrativa:** `http://127.0.0.1:8000/login/`

---

## 📸 Rotas Importantes

| Funcionalidade | Rota | Nome da URL |
| :--- | :--- | :--- |
| Dashboard Principal | `/dashboard/` | `core:dashboard` |
| Criar Novo Projeto | `/projetos/novo/` | `core:projeto_criar` |
| Gerenciar Serviços | `/servicos/` | `core:servico_lista` |
| Editar Config. Global | `/config/editar/` | `core:siteconfig_editar` |

---
## 📝 Modelo Relacional
<img width="885" height="839" alt="fLJ1ZjCm4Br7oZ-CUjaKr42Hk4IbsgefgABjLcqvHxFED35AuiXsbaM84mU-W0z0Uq2SLtn1VWmdRQ2f5bHA3eap7hytVfxdIwLHwY9DR4jpdH3CHKY9W91WHGaoBZ9CATC2dCdAxq8FbaBgRNcVS04-AHvbjcLR5p0MAMQXW1mbGi8Zb80Wyl9RUITWpJ0XpxPKzOM--zosOcue69SieHt0Ytz-gb" src="https://github.com/user-attachments/assets/48912548-5e07-45d4-83e4-5ffd36c26361" />


## 📝 Documentação Adicional (captura de telas)

**home**
<img width="780" height="2013" alt="home-dashboard" src="https://github.com/user-attachments/assets/44cfd472-a1f3-450a-8cfc-6ddd53a5bb2d" />


**Login**
<img width="780" height="488" alt="login" src="https://github.com/user-attachments/assets/151b9958-faca-44cc-9873-9fc2f51503fb" />


**Dashboard**
<img width="780" height="656" alt="Dashboard" src="https://github.com/user-attachments/assets/f7948811-04e0-4005-a727-6f26f8c0349b" />


**Gerenciamento de Projetos** 
<img width="780" height="488" alt="Gerenciamento de Projetos" src="https://github.com/user-attachments/assets/a64fbe8a-5516-4a34-bbe5-2ae848bb9dc0" />


**Gerenciar Depoimentos**
<img width="780" height="605" alt="Gerenciar Depoimentos" src="https://github.com/user-attachments/assets/fdceefc6-7fbb-4af7-bb35-d20ed98240de" />


**Mensagens de Contato**
<img width="780" height="488" alt="Mensagens de Contato" src="https://github.com/user-attachments/assets/6c6dd982-1276-47e0-b69a-f4034e294449" />


**Configurações do Site**
<img width="780" height="798" alt="Configurações do Site" src="https://github.com/user-attachments/assets/4d58eed0-b9a3-4608-99f1-18af3d67ef0b" />
