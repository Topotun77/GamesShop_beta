from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# from django.views.generic import TemplateView

basket_: dict = {}


def shop(request: HttpRequest):
    if request.method == 'POST':
        product = request.POST.get('product')
        if product in basket_.keys():
            basket_[product] += 1
        else:
            basket_[product] = 1
    print(basket_, len(basket_))
    context = {
        'items': ['Atomic Heart',
                  'Cyberpunk 2077',
                  'PayDay 2',
                  'Tetris',
                  'Змейка'],
        'basket': len(basket_),
        'back': '/'
    }
    return render(request, template_name='fourth_task/shop.html', context=context)


def basket(request: HttpRequest):
    global basket_
    if request.method == 'POST':
        basket_ = {}
    print(basket_, len(basket_))
    context = {
        'back': '/',
        'shop': '/shop',
        'basket': len(basket_),
        'basket_': basket_,
    }
    return render(request, template_name='fourth_task/basket.html', context=context)


