from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('exercise1', views.exercise1, name='Exercise-1'),
    path('analyze', views.analyze, name='Analyzed Text')
]