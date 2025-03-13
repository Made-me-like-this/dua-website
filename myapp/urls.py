
from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('duas/<int:dua_id>/', views.dua_detail, name='dua_detail'),
    path('learn/', views.learn, name='learn'),
    path('about/', views.about, name='about'),
    path('donate/', views.donate, name='donate'),
]
