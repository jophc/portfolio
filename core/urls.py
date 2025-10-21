from django.urls import path
from . import views # MANTENHA ASSIM

app_name = 'core'

urlpatterns = [
    # Rotas Públicas
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    
    # ROTA HTMX
    path('testimonials/load/', views.load_testimonial, name='load_testimonial'), 
    
    # Rotas da Área Administrativa (Geral)
    path('dashboard/', views.dashboard, name='dashboard'),
    path('config/editar/', views.siteconfig_editar, name='siteconfig_editar'),
    
    # Rotas de CRUD de Projetos
    path('projetos/', views.projeto_lista, name='projeto_lista'),
    path('projetos/novo/', views.projeto_criar, name='projeto_criar'),
    path('projetos/editar/<int:pk>/', views.projeto_editar, name='projeto_editar'),
    path('projetos/excluir/<int:pk>/', views.projeto_excluir, name='projeto_excluir'),

    # Rotas de Gerenciamento de Mensagens
    path('mensagens/', views.lista_mensagens, name='lista_mensagens'),
    path('mensagens/detalhe/<int:pk>/', views.mensagem_detalhe, name='mensagem_detalhe'),
    path('mensagens/excluir/<int:pk>/', views.mensagem_excluir, name='mensagem_excluir'),
    
    # Rotas de CRUD de Depoimentos
    path('depoimentos/', views.depoimento_lista, name='depoimento_lista'),
    path('depoimentos/novo/', views.depoimento_criar, name='depoimento_criar'),
    path('depoimentos/editar/<int:pk>/', views.depoimento_editar, name='depoimento_editar'),
    path('depoimentos/excluir/<int:pk>/', views.depoimento_excluir, name='depoimento_excluir'),
    
    # ROTAS DE CRUD DE SERVIÇOS
    path('servicos/', views.servico_lista, name='servico_lista'),
    path('servicos/novo/', views.servico_criar, name='servico_criar'),
    path('servicos/editar/<int:pk>/', views.servico_editar, name='servico_editar'),
    path('servicos/excluir/<int:pk>/', views.servico_excluir, name='servico_excluir'),
]