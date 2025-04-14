from django.shortcuts import render, redirect
from .models import Ad
from .forms import AdForm

def ad_list(request, filter_param=None):
    "Получение списка объявлений + фильтрация"
    if not filter_param:                                        # Если параметр фильтрации не передаётся,
        ads = Ad.objects.all()                                  # получаем все объекты модели
    else:                                                       # В противном случае выводим только отфильтрованные объявления
        ads = Ad.objects.filter(condition=filter_param) | Ad.objects.filter(category=filter_param)
        if not ads:                                             # Если же ни одно объявление не удовлетворяет параметру фильтрации,
            ads = 'Для данного параметра фильтрации нет ни одного объявления'   # выводим соответствующее сообщение
    # В шаблон передаём флаг отсутствия объявлений с заданными параметрами фильтрации и словари, переданные из модели                                      
    context = {'ads': ads, 'is_filter': isinstance(ads, str), 'categories': Ad.category_dict, 'conditions': Ad.condition_dict}
    return render(request, 'ad_list.html', context)

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

def update_ad(request, id):
    "Редактирование объявления"
    ad = Ad.objects.get(id=id)                                  # Получение объекта объявления с помощью id, переданного из шаблона
    if request.method == "POST":                                # Если метод запроса POST, проверяем валидность данных
        form = AdForm(request.POST, request.FILES, instance=ad) # Данные, введённые в поля формы, загруженные файлы, экземпляр модели
        if form.is_valid():                                     
            form.save()                                         # Если данные валидны, сохраняем их в базе
            return redirect('ad_list')                          # и перенаправляем на страницу со списком объявлений
    else:
        form = AdForm(instance=ad)                              # Если метод запроса не POST, выводим форму c ранее сохранёнными данными
    return render(request, 'update_ad.html', {'form': form, 'ad': ad})

def delete_ad(request, id):
    "Удаление объявления"
    ad = Ad.objects.get(id=id)                                  # Получение объекта объявления с помощью id, переданного из шаблона
    ad.delete()
    return redirect('ad_list')                                  # Возврат на страницу со списком объявлений