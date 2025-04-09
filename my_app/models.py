from django.db import models

class Ad(models.Model):                                             # Модель объявления
    title = models.CharField('Заголовок', max_length=200)           # Добавление полей модели
    description = models.TextField('Описание')
    category_dict = {0: 'техника', 1: 'мебель', 2: 'одежда', 3: 'книги', 4: 'прочее'}
    category = models.CharField('Категория', max_length=1, choices=category_dict, default=4)
    condition_dict = {0: 'новый', 1: 'б/у'}
    condition = models.CharField('Состояние', max_length=1, choices=condition_dict, default=0)

    def __str__(self):                                              # При обращении к экземпляру модели возвращается заголовок
        return self.title
