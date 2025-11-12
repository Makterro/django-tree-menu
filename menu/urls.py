from django.urls import path
from .views import test_menu_view, product_page, dairy_page, dairy_milk_page, fruits_page, fruits_apple_page, vegetables_page, vegetables_potato_page, vegetables_potato_best_page

urlpatterns = [
    path('', test_menu_view, name='test_menu'),
    
    path('products/', product_page, name='products'),
    
    path('products/dairy/', dairy_page, name='dairy'),
    path('products/dairy/milk/', dairy_milk_page, name='milk'),
    
    path('products/fruits/', fruits_page, name='fruits'),
    path('products/fruits/apple/', fruits_apple_page, name='apple'),
    
    path('products/vegetables/', vegetables_page, name='vegetables'),
    path('products/vegetables/potato/', vegetables_potato_page, name='potato'),
    path('products/vegetables/potato/best/', vegetables_potato_best_page, name='potato_best'),
]