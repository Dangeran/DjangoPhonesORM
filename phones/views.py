import operator

from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort == 'name':
        new_phones = sorted(phones, key=operator.attrgetter('name'))
        context = {'phones': new_phones}
    elif sort == 'min_price':
        new_phones = sorted(phones, key=operator.attrgetter('price'))
        context = {'phones': new_phones}
    elif sort == 'max_price':
        new_phones = sorted(phones, key=operator.attrgetter('price'), reverse=True)
        context = {'phones': new_phones}
    else:
        context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
