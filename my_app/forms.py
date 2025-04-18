from django import forms
from .models import Ad, ExchangeProposal

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad                                      # Создаём форму из модели
        exclude = ['user']                              # Форма будет иметь все поля модели, кроме тех, что указаны здесь

class ExchangeProposalForm(forms.ModelForm):
    class Meta:
        model = ExchangeProposal
        fields = '__all__'                              # Форма будет иметь все те же поля, что и модель

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)                                   # Обращаемся к конструктору суперкласса
        self.fields['ad_sender'].queryset = Ad.objects.filter(user=user)    # Выводим объявления только текущего пользователя
        self.fields['ad_receiver'].queryset = Ad.objects.exclude(user=user) # Выводим объявления всех пользователей кроме текущего

class StatusForm(forms.Form):                                               # Т.к. нужно поменять лишь одно поле, нет особого смысла использовать ModelForm
    status_dict = {'expect': 'ожидает', 'accepted': 'принята', 'rejected': 'отклонена'}
    status = forms.ChoiceField(label='Статус', choices=status_dict)