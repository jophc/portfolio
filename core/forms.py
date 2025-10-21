from django import forms
from .models import ContactMessage, Projeto, Testimonial, SiteConfig, Servico


# ----------------------------------------------------
# 1. FORMULÁRIO DE CONTATO (COMPLETO)
# ----------------------------------------------------
class ContatoForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        # TODOS OS CAMPOS DO FORMULÁRIO COMPLETO
        fields = ['name', 'email', 'phone', 'city', 'state', 'subject', 'message'] 

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Seu nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Seu e-mail'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Seu número de WhatsApp (opcional)'}),
            'city': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Sua Cidade'}),
            'state': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Seu Estado'}),
            'subject': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Assunto da mensagem'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Escreva sua mensagem...', 'rows': 5}),
        }

# ----------------------------------------------------
# 2. MODELFORM PARA O CRUD DE PROJETOS 
# ----------------------------------------------------
class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome_album', 'descricao_curta', 'capa_imagem', 'servicos_incluidos'] # Adicionado servicos_incluidos
        
        widgets = {
            'nome_album': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Álbum Casamento Maria e João'}),
            'descricao_curta': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Linho creme, 40 lâminas, Layout clean...'}),
        }

# ----------------------------------------------------
# 3. MODELFORM PARA O CRUD DE DEPOIMENTOS
# ----------------------------------------------------
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['author', 'message']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nome do Cliente'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Escreva o depoimento aqui...', 'rows': 4}),
        }

# ----------------------------------------------------
# 4. MODELFORM PARA AS CONFIGURAÇÕES DO SITE
# ----------------------------------------------------
class SiteConfigForm(forms.ModelForm):
    class Meta:
        model = SiteConfig
        fields = '__all__'
        widgets = {
            'hero_title': forms.TextInput(attrs={'class': 'form-control'}),
            'hero_lead': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'about_title': forms.TextInput(attrs={'class': 'form-control'}),
            'about_text_p1': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'about_text_p2': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
        }

# ----------------------------------------------------
# 5. MODELFORM PARA O CRUD DE SERVIÇOS
# ----------------------------------------------------
class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['name', 'description'] 
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Design Premium'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Descreva o que o pacote inclui', 'rows': 3}),
            
        }