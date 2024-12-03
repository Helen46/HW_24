import datetime
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from lms.models import Course, Subs
from users.models import User


@shared_task
def send_mailing_obout_subs(course, email):
    """Отправка письма об успешной подписке на курс"""
    return send_mail(
        "Подписка на курс",
        f"Вы успешно подписались на курс {course}",
        settings.EMAIL_HOST_USER,
        [email]
    )


@shared_task
def send_mailing_obout_update(course_pk):
    """Отправка письма об обновлении курса"""
    course = Course.objects.get(pk=course_pk)
    subs = Subs.objects.filter(course=course)
    email_list = []
    for sub in subs:
        email_list.append(sub.user.email)
    if email_list:
        return send_mail(
            "Информация об обновлении",
            f"Курс {course.name}, на который вы подписаны, был обновлен",
            settings.EMAIL_HOST_USER,
            email_list
        )


@shared_task
def block_inactive_users():
    today = timezone.now().date()
    users = User.objects.filter(is_active=True)
    for user in users:
        if user.last_login:
            if user.last_login.date() + datetime.timedelta(days=30) < today:
                user.is_active = False
                user.save()


