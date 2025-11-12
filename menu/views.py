from django.shortcuts import render

def test_menu_view(request):
    return render(request, 'menu/test_menu.html')


def product_page(request):
    return render(request, 'menu/simple_page.html', {'title': 'Продукты'})

def dairy_page(request):
    return render(request, 'menu/simple_page.html', {'title': 'Молочные продукты'})
def dairy_milk_page(request):
    return render(request, 'menu/simple_page.html', {'title': 'Молоко'})

def fruits_page(request):
    return render(request, 'menu/simple_page.html', {'title': 'Фрукты'})
def fruits_apple_page(request):
    return render(request, 'menu/simple_page.html', {'title': 'Яблоко'})

def vegetables_page(request):
    return render(request, 'menu/simple_page.html', {'title': 'Овощи'})
def vegetables_potato_page(request):
    return render(request, 'menu/simple_page.html', {'title': 'Картошка'})
def vegetables_potato_best_page(request):
    return render(request, 'menu/simple_page.html', {'title': 'Картошка вкусная'})