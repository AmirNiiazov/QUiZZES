from django.shortcuts import render
from django.core.paginator import Paginator
from exams.models import Exam


def home(request):
    if not request.user.is_authenticated:
        # Если пользователь не авторизован, показываем страницу с приветствием
        return render(request, 'welcome.html')

    # Если пользователь авторизован, показываем список тестов
    exams = Exam.objects.all()

    # Реализуем поиск
    search_query = request.GET.get('q', '')  # Получаем значение из поисковой строки
    if search_query:
        exams = exams.filter(title__icontains=search_query)  # Фильтрация по названию теста

    # Пагинация
    paginator = Paginator(exams, 5)  # 5 тестов на странице
    page_number = request.GET.get('page')  # Номер текущей страницы
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj, 'search_query': search_query})
