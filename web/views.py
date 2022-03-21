from django.shortcuts import render

def index(request):
    return render(request, 'web/index.html')

def meme(request):
    return render(request, 'web/meme.html')
    
# Create your views here.
