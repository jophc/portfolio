from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse 
from django.template.loader import render_to_string 

from .forms import ContatoForm, ProjetoForm, TestimonialForm, SiteConfigForm, ServicoForm
from .models import ContactMessage, Testimonial, Projeto, SiteConfig, Servico 


# ----------------------------------------------------------------------
# VIEWS ADMINISTRATIVAS (CORRIGIDO: Sem @login_required duplicado)
# ----------------------------------------------------------------------

@login_required
def dashboard(request):
    """
    Renderiza o painel de controle principal da área administrativa.
    """
    total_projetos = Projeto.objects.filter(user=request.user).count()
    total_mensagens = ContactMessage.objects.count()
    
    context = {
        'total_projetos': total_projetos,
        'total_mensagens': total_mensagens,
        'page_title': 'Dashboard'
    }
    return render(request, 'dashboard.html', context)


# ----------------------------------------------------------------------
# VIEWS PÚBLICAS
# ----------------------------------------------------------------------

def home(request):
    """
    Renderiza a página inicial e carrega os depoimentos, projetos e configurações.
    """
    testimonials = Testimonial.objects.all().order_by('pk') # Ordenado por PK para garantir índice estável
    config, created = SiteConfig.objects.get_or_create(pk=1)
    recent_projects = Projeto.objects.all().order_by('-created_at')[:3]
    
    form = ContatoForm() 

    # HTMX INTEGRATION: Define o depoimento inicial para o carrossel
    # 1. Tenta obter o índice atual, se houver
    current_index = request.session.get('testimonial_index', 0)
    
    # 2. Garante que o depoimento inicial seja o que o usuário parou de ver
    first_testimonial = testimonials[current_index] if testimonials else None

    # NOVO: Se a lista estiver vazia, define como None
    if not testimonials:
        first_testimonial = None

    return render(request, 'home.html', {
        'testimonials': testimonials,
        'config': config,
        'recent_projects': recent_projects,
        'form': form, 
        'first_testimonial': first_testimonial, 
    })

def contato(request):
    """
    Processa o formulário de contato e salva a mensagem no banco de dados.
    """
    config, created = SiteConfig.objects.get_or_create(pk=1)
    
    if request.method == 'POST':
        form = ContatoForm(request.POST) 
        
        if form.is_valid():
            form.save() 
            messages.success(request, 'Mensagem enviada com sucesso! Em breve entraremos em contato.')
            return redirect(reverse('core:home') + '#contato') 
        else:
            messages.error(request, 'Houve um erro no envio. Por favor, verifique os campos.')
    else:
        form = ContatoForm()
    
    return render(request, 'contato.html', {
        'form': form,
        'config': config
    })

# ----------------------------------------------------------------------
# VIEW HTMX PARA TROCA DE DEPOIMENTOS
# ----------------------------------------------------------------------

def load_testimonial(request):
    """
    Carrega o depoimento anterior ou próximo e atualiza o card via HTMX (server-side rendering).
    """
    testimonials = list(Testimonial.objects.all().order_by('pk')) 
    
    if not testimonials:
        return HttpResponse('<div id="current-testimonial-card" class="text-center">Nenhum depoimento disponível.</div>')

    max_index = len(testimonials)
    current_index = request.session.get('testimonial_index', 0)
    direction = request.GET.get('direction')

    if direction == 'next':
        new_index = (current_index + 1) % max_index
    elif direction == 'prev':
        new_index = (current_index - 1 + max_index) % max_index
    else:
        new_index = current_index
        
    request.session['testimonial_index'] = new_index
    new_testimonial = testimonials[new_index]

    html = render_to_string('testimonial_card.html', 
                            {'testimonial': new_testimonial}, 
                            request=request)
                            
    return HttpResponse(html)


# ----------------------------------------------------------------------
# VIEWS DE GERENCIAMENTO (CRUDS)
# ----------------------------------------------------------------------

# --- CRUD de Projetos ---

@login_required
def projeto_lista(request):
    """ Lista os projetos do usuário logado com paginação. """
    projeto_list = Projeto.objects.filter(user=request.user).order_by('-created_at')
    
    paginator = Paginator(projeto_list, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'page_obj': page_obj, 'page_title': 'Gerenciamento de Projetos'}
    return render(request, 'projeto_lista.html', context)


@login_required
def projeto_criar(request):
    """ Permite criar um novo projeto (CREATE). """
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.user = request.user 
            projeto.save()
            form.save_m2m() # Salva a relação M:M para Servicos
            
            messages.success(request, 'Novo projeto criado com sucesso!')
            return redirect('core:projeto_lista')
        else:
            messages.error(request, 'Erro ao criar o projeto. Verifique os campos.')
    else:
        form = ProjetoForm()
    return render(request, 'projeto_form.html', {'form': form, 'page_title': 'Criar Novo Projeto'})

@login_required
def projeto_editar(request, pk):
    """ Permite editar um projeto existente (UPDATE). """
    projeto = get_object_or_404(Projeto, pk=pk, user=request.user) 
    
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        
        if form.is_valid():
            form.save()
            form.save_m2m() # Salva a relação M:M
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('core:projeto_lista')
        else:
            messages.error(request, 'Erro ao atualizar o projeto. Verifique os campos.')
    else:
        form = ProjetoForm(instance=projeto)
    
    return render(request, 'projeto_form.html', {'form': form, 'page_title': f'Editar: {projeto.nome_album}'})


@login_required
def projeto_excluir(request, pk):
    """ Permite excluir um projeto existente (DELETE). """
    projeto = get_object_or_404(Projeto, pk=pk, user=request.user)
    
    if request.method == 'POST':
        projeto.delete()
        messages.success(request, f'Projeto "{projeto.nome_album}" excluído com sucesso.')
        return redirect('core:projeto_lista')
    
    return render(request, 'projeto_confirm_delete.html', {'projeto': projeto, 'page_title': 'Excluir Projeto'})


# --- Views de Mensagens ---

@login_required
def lista_mensagens(request):
    """ Lista todas as mensagens de contato recebidas com paginação. """
    message_list = ContactMessage.objects.all().order_by('-created_at')
    paginator = Paginator(message_list, 15) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'page_title': 'Mensagens Recebidas'}
    return render(request, 'mensagens_lista.html', context)


@login_required
def mensagem_detalhe(request, pk):
    """ Exibe o conteúdo completo de uma mensagem. """
    mensagem = get_object_or_404(ContactMessage, pk=pk)
    return render(request, 'mensagem_detalhe.html', {'mensagem': mensagem, 'page_title': 'Detalhe da Mensagem'})

@login_required
def mensagem_excluir(request, pk):
    """ Permite excluir uma mensagem de contato. """
    mensagem = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        mensagem.delete()
        messages.success(request, 'Mensagem excluída com sucesso.')
        return redirect('core:lista_mensagens')
    return render(request, 'mensagem_confirm_delete.html', {'mensagem': mensagem, 'page_title': 'Excluir Mensagem'})

# --- Views de Depoimentos ---

@login_required
def depoimento_lista(request):
    """ Lista todos os depoimentos (READ). """
    depoimento_list = Testimonial.objects.all().order_by('-created_at')
    paginator = Paginator(depoimento_list, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'page_title': 'Gerenciamento de Depoimentos'}
    return render(request, 'depoimento_lista.html', context)


@login_required
def depoimento_criar(request):
    """ Cria um novo depoimento (CREATE). """
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo depoimento criado com sucesso!')
            return redirect('core:depoimento_lista')
    else:
        form = TestimonialForm()
    return render(request, 'depoimento_form.html', {'form': form, 'page_title': 'Criar Novo Depoimento'})

@login_required
def depoimento_editar(request, pk):
    """ Edita um depoimento existente (UPDATE). """
    depoimento = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=depoimento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Depoimento atualizado com sucesso!')
            return redirect('core:depoimento_lista')
    else:
        form = TestimonialForm(instance=depoimento)
    return render(request, 'depoimento_form.html', {'form': form, 'page_title': f'Editar Depoimento ID: {pk}'})

@login_required
def depoimento_excluir(request, pk):
    """ Exclui um depoimento existente (DELETE). """
    depoimento = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        depoimento.delete()
        messages.success(request, 'Depoimento excluído com sucesso.')
        return redirect('core:depoimento_lista')
    return render(request, 'mensagem_confirm_delete.html', {'mensagem': depoimento, 'page_title': 'Excluir Depoimento'})

# --- View de Configuração Global ---

@login_required
def siteconfig_editar(request):
    """
    Permite editar o objeto SiteConfig (ID 1) DENTRO da interface do Dashboard.
    """
    config, created = SiteConfig.objects.get_or_create(pk=1) 
    
    if request.method == 'POST':
        form = SiteConfigForm(request.POST, request.FILES, instance=config)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações da Home Page atualizadas com sucesso!')
            return redirect('core:dashboard')
        else:
            messages.error(request, 'Houve um erro na atualização. Verifique os campos.')
    else:
        form = SiteConfigForm(instance=config)
    return render(request, 'siteconfig_form.html', {'form': form, 'page_title': 'Editar Configurações do Site'})

# --- CRUD de Serviços ---

@login_required
def servico_lista(request):
    """ Lista todos os serviços (READ - List). """
    servico_list = Servico.objects.all().order_by('name')
    return render(request, 'servico_lista.html', {'servico_list': servico_list, 'page_title': 'Gerenciamento de Serviços'})

@login_required
def servico_criar(request):
    """ Cria um novo serviço (CREATE). """
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo serviço criado com sucesso!')
            return redirect('core:servico_lista')
    else:
        form = ServicoForm()
    return render(request, 'servico_form.html', {'form': form, 'page_title': 'Criar Novo Serviço'})

@login_required
def servico_editar(request, pk):
    """ Edita um serviço existente (UPDATE). """
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço atualizado com sucesso!')
            return redirect('core:servico_lista')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'servico_form.html', {'form': form, 'page_title': f'Editar Serviço: {servico.name}'})

@login_required
def servico_excluir(request, pk):
    """ Exclui um serviço existente (DELETE). """
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        servico.delete()
        messages.success(request, 'Serviço excluído com sucesso.')
        return redirect('core:servico_lista')
    return render(request, 'mensagem_confirm_delete.html', {'mensagem': servico, 'page_title': 'Excluir Serviço'})