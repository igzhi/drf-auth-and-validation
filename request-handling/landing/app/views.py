from collections import Counter
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    click_mode = request.GET.get('from-landing')
    if click_mode == 'original':
        counter_click[click_mode] += 1
    if click_mode == 'test':
        counter_click[click_mode] += 1
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    landing_mode = request.GET.get('ab-test-arg')
    if landing_mode == 'test':
        counter_show[landing_mode] += 1
        return render_to_response('landing_alternate.html')
    if landing_mode == 'original':
        counter_show[landing_mode] += 1
        return render_to_response('landing.html')
    else:
        return HttpResponse('Неверный модификатор')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    if counter_show['test'] == 0:
        test_conversion = 'Просмотров не было'
    else:
        test_conversion = round(counter_click['test'] / counter_show['test'], 2)
    if counter_show['original'] == 0:
        original_conversion = 'Просмотров не было'
    else:
        original_conversion = round(counter_click['original'] / counter_show['original'], 2)
    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
