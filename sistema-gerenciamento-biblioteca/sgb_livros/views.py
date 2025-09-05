from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def livros(request):
    return render(request, 'livros.html')

def salva_livro(request):
    titulo_livro = request.POST["titulo_livro"] #pegar nome do livro que esta no .HTML
    autor_livro = request.POST["autor_livro"]
    editora_livro = request.POST["editora_livro"]
    return render(request, 'livros.html', context={'titulo_livro':titulo_livro})