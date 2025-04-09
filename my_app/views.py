from django.shortcuts import render
from .models import Ad

def ad_list(request):
    "Получение списка объявлений"
    ads = Ad.objects.all()                                      # Получение всех объектов модели
    return render(request, 'ad_list.html', {'ads': ads})
