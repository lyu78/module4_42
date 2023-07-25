from django.db import models


class Advertisement(models.Model):

    # Заголовок
    # Небольшое текстовое поле
    title = models.CharField("Заголовок", max_length=128)

    # Описание
    # Большое текстовое поле
    description = models.TextField("Описание")

    # Цена
    # Число с фиксированной точностью
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)

    # Уместен ли торг
    # Логическое значение
    auction = models.BooleanField("Торг", help_text="Отметьте, если хотите торговаться")

    # Дата создания
    created_at = models.DateTimeField(auto_now_add=True)

    # Дата изменения
    updated_at = models.DateTimeField(auto_now=True)

    # Изображение

    # Адрес

    # Отзывы/рейтинг продавца

    # Контакты продавца

    # Похожие товары
