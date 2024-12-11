from django.shortcuts import render, redirect
from .models import Film  # Импортируем модель Film
from .forms import FilmForm  # Импортируем форму

# Функция для главной страницы
def home(request):
    films = Film.objects.all()  # Получаем все фильмы из базы данных
    return render(request, 'films/home.html', {'films': films})  # Передаём их в шаблон

# Функция для добавления фильма
def add_film(request):
    if request.method == 'POST':  # Если данные отправлены через форму
        form = FilmForm(request.POST)
        if form.is_valid():  # Проверяем, что форма заполнена корректно
            form.save()  # Сохраняем данные в базу
            return redirect('home')  # Перенаправляем на главную страницу
    else:
        form = FilmForm()  # Пустая форма для GET-запроса
    return render(request, 'films/add_film.html', {'form': form})
