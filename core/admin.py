from django.contrib import admin
from .models import Testimonial, ContactMessage, SiteConfig, Projeto

# ----------------------------------------------------
# 1. ADMIN PARA PROJETOS
# ----------------------------------------------------
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    # list_display atualizado: removido 'user'
    list_display = ('nome_album', 'status', 'prazo_estimado', 'created_at')
    search_fields = ('nome_album', 'status')
    list_filter = ('status', 'created_at')
    # exclude vazio, pois não há 'user'
    exclude = ()

# ----------------------------------------------------
# 2. ADMIN PARA DEPOIMENTOS
# ----------------------------------------------------
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at')
    search_fields = ('author', 'message')
    list_filter = ('created_at',)

# ----------------------------------------------------
# 3. ADMIN PARA MENSAGENS DE CONTATO
# ----------------------------------------------------
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city', 'state', 'subject', 'created_at')
    search_fields = ('name', 'email', 'city', 'state', 'subject', 'message')
    list_filter = ('state', 'created_at')
    readonly_fields = ('name', 'email', 'city', 'state', 'subject', 'message', 'created_at')

    def has_add_permission(self, request):
        # Impede adicionar mensagens manualmente no painel
        return False

# ----------------------------------------------------
# 4. ADMIN PARA CONFIGURAÇÃO GERAL (Singleton)
# ----------------------------------------------------
@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    # Permite apenas 1 registro
    def has_add_permission(self, request):
        return not SiteConfig.objects.exists()

    fieldsets = (
        ('PÁGINA INICIAL - SEÇÃO HERO', {
            'fields': ('hero_title', 'hero_lead', 'hero_image'),
        }),
        ('PÁGINA INICIAL - SEÇÃO SOBRE MIM', {
            'fields': ('about_title', 'about_text_p1', 'about_text_p2', 'about_image'),
        }),
        ('INFORMAÇÕES DE CONTATO', {
            'fields': ('whatsapp_number', 'email_address'),
        }),
    )