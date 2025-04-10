from django.forms import ModelForm
from .models import Ad

class AdForm(ModelForm):
    class Meta:
        model = Ad                                      # Создаём форму из модели
        fields = '__all__'                              # Форма будет иметь все те же поля