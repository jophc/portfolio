from pathlib import Path
import os # Importa o módulo os para manipulação de caminhos de arquivo

# Define o diretório base do projeto.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configurações de desenvolvimento rápido - não adequadas para produção
# Veja https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# AVISO DE SEGURANÇA: mantenha a chave secreta usada em produção em segredo!
SECRET_KEY = 'django-insecure-!y3n-w%b!@*v&^y!&j*m25@c+@t!z2^r(8(i&p95b0t1g(1r6'

# AVISO DE SEGURANÇA: não execute com o debug ativado em produção!
DEBUG = True

ALLOWED_HOSTS = []


# Definição dos aplicativos.
# Define os aplicativos instalados no seu projeto Django.
# 'core' é o seu aplicativo personalizado.
# Outros são aplicativos padrão do Django.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core', # Seu aplicativo 'core'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolioblog.urls'

# Configuração dos templates.
# DIRS: Lista de diretórios onde o Django deve procurar por templates.
# Adicionamos 'BASE_DIR / "templates"' para que o Django encontre o 'base.html' na raiz do projeto.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")], # Usar os.path.join para compatibilidade de OS
        'APP_DIRS': True, # Permite que o Django procure templates dentro das pastas 'templates' de cada app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolioblog.wsgi.application'


# Configuração do banco de dados
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validação de senha
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internacionalização
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br' # Define o idioma para Português (Brasil)

TIME_ZONE = 'America/Bahia' # Define o fuso horário para São Paulo

USE_I18N = True

USE_TZ = True


# Arquivos estáticos (CSS, JavaScript, Imagens)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/' # URL base para servir arquivos estáticos

# Define diretórios adicionais onde o Django deve procurar por arquivos estáticos.
# Adicionamos a pasta 'static' na raiz do projeto.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"), # Usar os.path.join para compatibilidade de OS
]

# Configurações para arquivos de MÍDIA (uploads de usuários, etc.)
# MEDIA_URL: URL base para servir arquivos de mídia.
# MEDIA_ROOT: Caminho absoluto no sistema de arquivos onde os arquivos de mídia serão armazenados.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Tipo de campo de chave primária padrão
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações de Redirecionamento (Melhoria: Usa nomes de URL em vez de paths fixos)
# Após o login, usuário vai para o dashboard
LOGIN_REDIRECT_URL = 'core:dashboard' # Usar o nome da rota
# Se o usuário tentar acessar uma página restrita, ele é redirecionado para esta rota de login.
LOGIN_URL = 'login' # Usar o nome da rota
# Para onde vai ao sair (logout)
LOGOUT_REDIRECT_URL = '/' # Usar o nome da rota (consistente com urls.py)

# CONFIGURAÇÃO ADICIONAL PARA SERVIR ARQUIVOS DE MÍDIA NO DEBUG MODE
# Esta linha é apenas para referência. A implementação real deve estar no urls.py
# STATIC_SERVING = True