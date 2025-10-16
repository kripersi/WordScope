from django.db import models


class Words(models.Model):
    eng_word = models.CharField(max_length=100, verbose_name="Английское слово")
    ru_word = models.CharField(max_length=100, verbose_name="Русское слово")
    word_type = models.CharField(max_length=50, verbose_name="Тип слова")
    example = models.TextField(verbose_name="Пример использования")

    def __str__(self):
        return f"{self.eng_word} — {self.ru_word}"

