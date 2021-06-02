from django.urls import path
from . import views

app_name = 'Superhero'
urlpatterns = [
    path('', views.index, name='index')
]