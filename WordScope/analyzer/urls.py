# tg: @Marpexiz , github.com/kripersi

from django.urls import path
from .views import analyzer_view

app_name = 'analyzer'

urlpatterns = [
    path('', analyzer_view, name='analyzer_text'),
]

