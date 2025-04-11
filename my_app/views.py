from django.shortcuts import render, redirect
from .models import Ad
from .forms import AdForm

def ad_list(request):
    "Получение списка объявлений"
    ads = Ad.objects.all()                                      # Получение всех объектов модели
    return render(request, 'ad_list.html', {'ads': ads})

def create_ad(request):
    "Создание нового объявления"
    if request.method == 'POST':                                # Если метод запроса POST, проверяем валидность данных
        form = AdForm(request.POST, request.FILES)              # Данные, введённые в поля формы, и загруженные файлы 
        if form.is_valid():                                     
            form.save()                                         # Если данные валидны, сохраняем их в базе
            return redirect('ad_list')                          # и перенаправляем на страницу со списком объявлений
    else:
        form = AdForm()                                         # Если метод запроса не POST, выводим пустую форму
    return render(request, 'create_ad.html', {'form': form})

def delete_ad(request, id):
    "Удаление объявления"
    ad = Ad.objects.get(id=id)                                  # Получение объекта объявления с помощью id, переданного из шаблона
    ad.delete()
    return redirect('ad_list')                                  # Возврат на страницу со списком объявлений