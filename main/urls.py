from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='main'),
    path('politic/', views.politic, name='Политика'),
    path('sport/', views.sport, name='Спорт'),
    path('auto/', views.auto, name='Автомобили'),
    path('IT/', views.IT, name='IT'),
    path('medic/', views.medic, name='Медицина'),
    path('else_news/', views.else_news, name='Прочее'),
    path('about/<slug:slug>/', views.about, name='about')
]