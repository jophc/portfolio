from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. ROTAS DE AUTENTICAÇÃO PERSONALIZADA
    # Login, Logout e Páginas Personalizadas
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # CORREÇÃO DO 405/GET: Define next_page para a página inicial (LOGOUT_REDIRECT_URL no settings)
    # Quando o POST do botão "Sair" for recebido, ele redireciona para a home ('/')
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), 
    
    # NOVAS ROTAS PARA ALTERAÇÃO DE SENHA (CORREÇÃO DO NoReverseMatch)
    path('password_change/', 
         auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'), 
         name='password_change'),
    path('password_change/done/', 
         auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), 
         name='password_change_done'),
    
    # 2. ROTAS PRINCIPAIS DO APP (CORE)
    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)