from django.shortcuts import render, redirect
from .models import Ad, ExchangeProposal
from .forms import AdForm, ExchangeProposalForm, StatusForm

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
            ad = form.save(commit=False)                        # Если данные валидны, сохраняем их в базе
            ad.user = request.user
            ad.save()
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

def proposal_list(request):
    "Получение списка предложений"
    proposals = ExchangeProposal.objects.all()
    return render(request, 'proposal_list.html', {'proposals': proposals})

def create_proposal(request):
    "Создание нового предложения"
    if request.method == 'POST':
        form = ExchangeProposalForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('proposal_list')
    else:
        form = ExchangeProposalForm(request.user)               # Передаём в форму текущего пользователя
    return render(request, 'create_proposal.html', {'form': form})

def proposal_status(request, id):
    "Изменение статуса объявления"
    proposal = ExchangeProposal.objects.get(id=id)
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            proposal.status = form.cleaned_data['status']       # Получаем значение, введённое в поле формы "статус"
            proposal.save()
            return redirect('proposal_list')
    else:
        form = StatusForm(initial={'status': proposal.status})  # Передаём в форму значение из экземпляра модели
    return render(request, 'proposal_status.html', {'form': form, 'proposal': proposal})

def delete_proposal(request, id):
    "Удаление предложения"
    proposal = ExchangeProposal.objects.get(id=id)
    proposal.delete()
    return redirect('proposal_list')