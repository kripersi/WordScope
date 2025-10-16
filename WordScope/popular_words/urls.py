from django.urls import path
from .views import word_list_view

app_name = 'popular_words'

urlpatterns = [
    path('', word_list_view, name='words'),
]

