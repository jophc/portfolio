from django.db import models 
from django.contrib.auth.models import User 

# ----------------------------------------------------
# MODELO 1: DEPOIMENTOS/TESTEMUNHOS
# ----------------------------------------------------
class Testimonial(models.Model): 
    author = models.CharField("Autor", max_length=100) 
    message = models.TextField("Mensagem") 
    created_at = models.DateTimeField("Data de criação", auto_now_add=True) 

    class Meta: 
        verbose_name = "Depoimento" 
        verbose_name_plural = "Depoimentos" 
        ordering = ['-created_at'] 

    def __str__(self): 
        return f"{self.author}: {self.message[:30]}..."

# ----------------------------------------------------
# MODELO 2: MENSAGENS DE CONTATO (Completo com todos os campos)
# ----------------------------------------------------
class ContactMessage(models.Model): 
    name = models.CharField("Nome", max_length=100) 
    email = models.EmailField("E-mail") 
    phone = models.CharField("Telefone / WhatsApp", max_length=20, blank=True, null=True)
    city = models.CharField("Cidade", max_length=100, blank=True, null=True)
    state = models.CharField("Estado", max_length=100, blank=True, null=True)
    subject = models.CharField("Assunto", max_length=200, blank=True, null=True) 
    message = models.TextField("Mensagem") 
    created_at = models.DateTimeField("Data de criação", auto_now_add=True) 

    class Meta: 
        verbose_name = "Mensagem de Contato" 
        verbose_name_plural = "Mensagens de Contato" 
        ordering = ['-created_at'] 

    def __str__(self): 
        return f"{self.name} - {self.subject or 'Sem Assunto'}"

# ----------------------------------------------------
# MODELO 3: CONFIGURAÇÃO GERAL DO SITE (Singleton)
# ----------------------------------------------------
class SiteConfig(models.Model):
    hero_title = models.CharField("Título Hero", max_length=255)
    hero_lead = models.TextField("Texto Hero", blank=True)
    about_title = models.CharField("Título Sobre", max_length=255)
    about_text_p1 = models.TextField("Parágrafo 1", blank=True)
    about_text_p2 = models.TextField("Parágrafo 2", blank=True)
    whatsapp_number = models.CharField("WhatsApp", max_length=20, blank=True)
    email_address = models.EmailField("E-mail", blank=True)
    
    def __str__(self):
        return "Configurações do Site"
    
    def save(self, *args, **kwargs):
        self.pk = 1
        return super(SiteConfig, self).save(*args, **kwargs)

# ----------------------------------------------------
# MODELO 4: SERVICO (5ª CLASSE)
# ----------------------------------------------------
class Servico(models.Model):
    name = models.CharField("Nome do Serviço", max_length=100)
    description = models.TextField("Descrição Detalhada", blank=True, null=True)
    # LINHA 'icon_class' FOI REMOVIDA
    
    class Meta:
        verbose_name = "Serviço/Pacote"
        verbose_name_plural = "Serviços/Pacotes"
        ordering = ['name']

    def __str__(self):
        return self.name

# ----------------------------------------------------
# MODELO 5: PROJETO (Com Descrição Curta e Relação M:M)
# ----------------------------------------------------
class Projeto(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('CONCLUIDO', 'Concluído'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Designer/Responsável") 
    
    nome_album = models.CharField("Nome do Álbum", max_length=200)
    descricao_curta = models.CharField("Descrição do Card", max_length=255, help_text="Texto curto que aparece logo abaixo do título na Home.")
    
    servicos_incluidos = models.ManyToManyField(Servico, related_name='projetos', verbose_name="Serviços Incluídos")
    
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    prazo_estimado = models.DateField("Prazo estimado", blank=True, null=True)
    capa_imagem = models.ImageField("Imagem de capa", upload_to='project_covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['-created_at']

    def __str__(self):
        return self.nome_album