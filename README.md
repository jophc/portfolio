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
| **HTMX** | Carrossel de Depoimentos com troca assíncrona (sem recarga de página). | **Bônus (5 pts)** |
| **Imagens** | Upload e exibição de capa de projeto. | **Bônus (5 pts)** |

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

## 📝 Documentação Adicional

*(Insira capturas de tela aqui para o arquivo final)*