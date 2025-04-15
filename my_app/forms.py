from django.forms import ModelForm
from .models import Ad

class AdForm(ModelForm):
    class Meta:
        model = Ad                                      # Создаём форму из модели
        exclude = ['user']                              # Форма будет иметь все те же поля, кроме тех, что указаны здесь