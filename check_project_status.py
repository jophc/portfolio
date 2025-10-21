# check_project_status.py
import os
from pathlib import Path
import django
from importlib import import_module
from django.conf import settings
from django.urls import get_resolver
from django.views import View
from django.shortcuts import render
from django.template.loader import get_template

# Inicializa Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolioblog.settings')
django.setup()

print("===== STATUS FINAL DO PROJETO =====\n")

# 1️⃣ Apps e modelos
print("1️⃣ Apps instalados e modelos:\n")
for app_config in django.apps.apps.get_app_configs():
    print(f"App: {app_config.name}")
    models = list(app_config.get_models())
    if models:
        for m in models:
            print(f"  - {m.__name__}")
    else:
        print("  (Sem modelos)")
    print()

# 2️⃣ Rotas disponíveis
print("2️⃣ Rotas disponíveis no projeto:")
resolver = get_resolver()
all_urls = []

def list_urls(urlpatterns, prefix=''):
    for p in urlpatterns:
        if hasattr(p, 'url_patterns'):
            list_urls(p.url_patterns, prefix + (p.pattern.regex.pattern if hasattr(p.pattern, 'regex') else str(p.pattern)))
        else:
            try:
                pattern = p.pattern.regex.pattern
            except:
                pattern = str(p.pattern)
            all_urls.append(prefix + pattern)

list_urls(resolver.url_patterns)
for u in all_urls:
    print(f" - {u}")
print()

# 3️⃣ Templates encontrados
print("3️⃣ Templates e arquivos encontrados:")
template_dirs = settings.TEMPLATES[0]['DIRS']
for t_dir in template_dirs:
    t_path = Path(t_dir)
    for root, dirs, files in os.walk(t_path):
        rel_root = Path(root).relative_to(t_path)
        if files:
            print(f"Diretório: {rel_root}")
            for f in files:
                print(f" - {f}")
print()

# 4️⃣ Arquivos estáticos encontrados
print("4️⃣ Arquivos estáticos encontrados:")
for static_dir in settings.STATICFILES_DIRS:
    s_path = Path(static_dir)
    for root, dirs, files in os.walk(s_path):
        rel_root = Path(root).relative_to(s_path)
        if files:
            print(f"Diretório: {rel_root}")
            for f in files:
                print(f" - {f}")
print()

# 5️⃣ Templates referenciados nas views do app core
print("5️⃣ Templates referenciados nas views do app core:")
core_views = import_module('core.views')
for attr_name in dir(core_views):
    attr = getattr(core_views, attr_name)
    template = None
    # CBV (herda de View)
    if isinstance(attr, type) and issubclass(attr, View):
        template = getattr(attr, 'template_name', None)
    # FBV (função)
    elif callable(attr):
        try:
            code = attr.__code__.co_consts
            for c in code:
                if isinstance(c, str) and c.endswith('.html'):
                    template = c
                    break
        except AttributeError:
            pass
    if template:
        # Verifica se o template existe
        found = any((Path(t_dir)/template).exists() for t_dir in template_dirs)
        status = "OK" if found else "FALTA!"
        print(f" - {attr_name}: {template} ({status})")
    else:
        # Ignora funções auxiliares não relacionadas a templates
        continue

print("\n✅ Verificação final concluída!")