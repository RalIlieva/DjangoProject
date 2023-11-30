from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact-submit/', views.contact_submit, name='contact_submit'),
    path('product_category/<str:category>/', views.product_category, name='product_category'),
    path('snake/', views.snake_game_view, name='snake'),

    path('products/', views.products, name='products'),
]
