from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()


class Advertisement(models.Model):

    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        "Изображение",
        upload_to="advertisements/"
    )
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

    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.strftime("%H:%M:%S")
            return format_html(
                "<span style='color:green; font-weight:bold;'> Сегодня в {}</span>",
                created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Фото')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{}" style="max-height:80px; max-width:80px">',
                self.image.url
            )

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'

    # Изображение

    # Адрес

    # Отзывы/рейтинг продавца

    # Контакты продавца

    # Похожие товары
