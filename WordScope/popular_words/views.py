# github.com/kripersi , tg: @Marpexiz
from django.shortcuts import render
from .models import Words


def word_list_view(request):
    word_type = request.GET.get('type')
    if word_type:
        # Сортируем по типу (глаголы, сущ., прил., наречия)
        words = Words.objects.filter(word_type__iexact=word_type)
    else:
        words = Words.objects.all()
    return render(request, 'popular_words/word_list.html', {'words': words})

