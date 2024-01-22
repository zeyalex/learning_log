from django.shortcuts import render

def index(request):
    """Головна сторінка "Журналу спостережень"."""
    return render(request, 'learning_logs/index.html') 
