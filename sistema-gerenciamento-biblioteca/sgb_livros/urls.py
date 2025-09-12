from django.urls import path
from . import views 

urlpatterns = [
    #path('', views.livros),
    #path("salva_livro" , views.salva_livro)
    path('', views.cadastra_livro, name='cadastra_livro'),
]
