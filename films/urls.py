from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('add-film/', views.add_film, name='add_film'),  # Страница добавления фильма
]
