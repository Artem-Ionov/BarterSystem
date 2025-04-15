from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):                                             # Модель объявления
    title = models.CharField('Заголовок', max_length=200)           # Добавление полей модели
    description = models.TextField('Описание')
    category_dict = {'т': 'техника', 'м': 'мебель', 'о': 'одежда', 'к': 'книги', 'п': 'прочее'}
    category = models.CharField('Категория', max_length=1, choices=category_dict, default='п')
    condition_dict = {'н': 'новый', 'б': 'б/у'}
    condition = models.CharField('Состояние', max_length=1, choices=condition_dict, default='н')
    image = models.ImageField('Изображение', blank=True)
    created_at = models.DateTimeField(auto_now_add=True,  null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')

    def __str__(self):                                              # При обращении к экземпляру модели возвращается заголовок
        return self.title
