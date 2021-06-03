from . import views
from django.urls import path

app_name = 'Superhero'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:SuperHeroes_id>/', views.detail, name='detail')
]