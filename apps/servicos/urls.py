from django.urls import path
app_name = 'servicos'

from .import views

urlpatterns = [
    path('novo-servico/', views.novo_servico, name='novo_servico'),
    path('servicos/', views.lista_servicos, name='lista_servicos'),
    path('editar-servico/<int:pk>/', views.editar_servico, name='editar_servico'),

]