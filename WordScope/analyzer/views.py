# tg: @Marpexiz , github.com/kripersi
import re
from collections import Counter
from django.shortcuts import render

MAX_FILE_SIZE = 1 * 1024 * 1024  # 1 MB


def analyzer_view(request):
    results = []
    stats = []
    error = None

    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']

        if file.size > MAX_FILE_SIZE:
            error = "Файл слишком большой. Максимальный размер — 1 МБ."
        else:
            try:
                text = file.read().decode('utf-8')
            except UnicodeDecodeError:
                error = "Ошибка чтения файла. Убедитесь, что он сохранён в кодировке UTF-8."

        if not error:
            raw_words = text.split()
            clean_words = []

            for word in raw_words:
                word = re.sub(r'\W+', '', word)
                word = word.lower()
                if len(word) > 2:
                    clean_words.append(word)

            counter = Counter(clean_words)
            sorted_items = counter.most_common(150)

            for word, count in sorted_items:
                results.append({
                    'text': word,
                    'count': count
                })

            stats = {
                'count_symbols': len(text),
                'count_words': len(raw_words),
                'count_punctuation': len(re.findall(r'[.,\-!?;:—()\[\]\'"]', text)),
                'count_space': text.count(' ')
            }

    return render(request, 'analyzer/analyzer_text.html', {
        'results': results,
        'error': error,
        'stats': stats
    })

