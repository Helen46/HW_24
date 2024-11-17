from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from lms.models import Course, Subs


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
    course = Course.objects.get(pk=course_pk).first()
    subs = Subs.objects.filter(course=course)
    email_list = []
    for sub in subs:
        email_list.append(sub.user.email)
    if email_list:
        return send_mail(
            "Информация об обновлении",
            f"Курс {course.name}, на который вы подписаны, был обнавлен",
            settings.EMAIL_HOST_USER,
            email_list
        )
