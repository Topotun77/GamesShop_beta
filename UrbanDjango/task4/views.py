from django.shortcuts import render
# from django.views.generic import TemplateView


def shop(request):
    context = {
        'items': ['Atomic Heart',
                  'Cyberpunk 2077',
                  'PayDay 2',
                  'Tetris',
                  'Змейка'],
        'back': '/'
    }
    return render(request, template_name='fourth_task/shop.html', context=context)


def basket(request):
    context = {
        'back': '/',
        'shop': '/shop'
    }
    return render(request, template_name='fourth_task/basket.html', context=context)


