from django.shortcuts import render, get_list_or_404, redirect

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def avaliacoes(request):
    return render(request, "core/avaliacoes.html")