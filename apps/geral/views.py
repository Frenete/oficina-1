from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import OficinaForm

from .models import Oficina


@login_required
def home(request):
    template_name = 'geral/home.html'
    context = {}
    return render(request, template_name, context)


@login_required
def nova_oficina(request):
    template_name = 'geral/nova_oficina.html'
    context = {}
    if request.method == 'POST':
        form = OficinaForm(request.POST)
        if form.is_valid():
            of = form.save(commit=False)
            of.usuario = request.user
            of.save()
            messages.success(request, 'Oficina cadastradada com sucesso')
            return redirect('geral:lista_oficina')
    form = OficinaForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def lista_oficina(request):
    template_name = 'geral/lista_oficina.html'
    oficinas = Oficina.objects.filter(usuario=request.user) # select * from oficina where usuario = usuario_de_sessão
    context = {
        'oficinas': oficinas,
    }
    return render(request, template_name, context)


@login_required
def excluir_oficina(request, pk):
    oficina = get_object_or_404(Oficina, pk=pk)
    oficina.delete()
    messages.info(request, 'Oficina excluída com sucesso')
    return redirect('geral:lista_oficina')

@login_required
def editar_oficina(request, pk):
    template_name = 'geral/nova_oficina.html'
    context={}
    oficina = get_object_or_404(Oficina, pk=pk)
    if request.method == 'POST':
        form = OficinaForm(data=request.POST, instance=oficina)
        form.save()
        messages.success(request, 'Oficina atualizada com sucesso')
        return redirect('geral:lista_oficina')
    form = OficinaForm(instance=oficina)
    context['form'] = form
    return render(request, template_name, context)

