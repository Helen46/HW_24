from django.db import models

from config import settings
from config.settings import NULLABLE


class Course(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    preview = models.ImageField(
        upload_to="lms/images",
        verbose_name="Изображение",
        help_text="Загрузите изображение",
        **NULLABLE
    )
    description = models.TextField(
        verbose_name="Описание курса",
        help_text="Укажите описание курса",
        **NULLABLE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Автор",
        help_text="Укажите автора курса"
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курск",
        help_text="Выберите курс",
        related_name="lesson_set",
        **NULLABLE
    )
    preview = models.ImageField(
        upload_to="lms/images",
        verbose_name="Изображение",
        help_text="Загрузите изображение",
        **NULLABLE
    )
    description = models.TextField(
        verbose_name="Описание урока",
        help_text="Укажите описание урока"
    )
    video_linc = models.URLField(
        verbose_name="Ссылка на видеоурок",
        help_text="Укажите ссылку видеоурока",
        **NULLABLE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Автор",
        help_text="Укажите автора урока"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
