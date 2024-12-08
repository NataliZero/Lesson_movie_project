from django.shortcuts import render
from .models import Film  # Импортируем модель Film

def home(request):
    films = Film.objects.all()  # Получаем все фильмы из базы данных
    return render(request, 'films/home.html', {'films': films})  # Передаём их в шаблон
