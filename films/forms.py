from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'review']  # Поля, которые будут в форме
        labels = {
            'title': 'Название фильма',
            'description': 'Описание фильма',
            'review': 'Отзыв о фильме',
        }
