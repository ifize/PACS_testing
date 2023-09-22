from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Studies


def studies_table(request):
    data = Studies.objects.order_by('id')  # Упорядочиваем данные по полю 'id'
    
    # Инициализируем пагинатор с данными и количеством элементов на странице (например, 10)
    paginator = Paginator(data, 10)
    
    # Получаем номер текущей страницы из параметра запроса (по умолчанию 1)
    page_number = request.GET.get('page')
    
    # Получаем объект страницы
    page = paginator.get_page(page_number)
    
    if request.is_ajax():
        studies_data = [
            {
                'patient_fio': study.patient_fio,
                'patient_birthdate': study.patient_birthdate,
                'study_uid': study.study_uid,
                'study_date': study.study_date.strftime('%Y-%m-%d %H:%M:%S'),  # Преобразуем дату и время в строку
                'study_modality': study.study_modality.name  # или другое поле, которое вы хотите отобразить
            }
            for study in page
        ]
        return JsonResponse(studies_data, safe=False)
    
    return render(request, 'studies_table.html', {'page': page})

def init_db(request):
    return render(request, 'test_datatable/init_db.html')
