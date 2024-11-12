from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE
from lms.models import Course, Lesson


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта",
        help_text="Укажите вашу элетронную почту"
    )
    phone = models.CharField(
        max_length=35,
        **NULLABLE,
        verbose_name="Номер телефона",
        help_text="Укажите ваш номер телефона"
    )
    city = models.CharField(
        max_length=50,
        **NULLABLE,
        verbose_name="Город",
        help_text="Укажите ваш город"
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        **NULLABLE,
        verbose_name="Аватар",
        help_text="Загрузите аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    CASH = "cash"
    CARD = "card"
    PAYMENT_TYPE = (
        (CASH, 'Наличными'),
        (CARD, 'Картой')
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
        **NULLABLE
    )
    payment_time = models.DateTimeField(
        verbose_name="Дата оплаты",
        auto_now_add=True,
        blank=True,
        null=True,
    )
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course",
        **NULLABLE
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="lesson",
        **NULLABLE
    )
    amount = models.PositiveIntegerField(
        default=0,
        verbose_name="Стоимость покупки"
    )
    payment_type = models.CharField(
        max_length=15,
        choices=PAYMENT_TYPE,
        default=CASH,
        verbose_name='Способ оплаты',
        help_text="Выберите способ оплаты"
    )
    session_id = models.CharField(
        max_length=255,
        **NULLABLE,
        verbose_name="ID сессии"
    )
    link = models.URLField(
        max_length=400,
        **NULLABLE,
        verbose_name="Ссылка на оплату"
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"Сумма: {self.amount}. Тип оплаты: {self.payment_type}."
