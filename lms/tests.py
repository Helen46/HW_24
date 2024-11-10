from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson, Subs
from users.models import User


class LmsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@gmail.com", is_staff=True, is_superuser=True)
        self.course = Course.objects.create(name="Test course", description="Test course", owner=self.user)
        self.lesson = Lesson.objects.create(name="Test lesson", description="Test lesson", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """ Тест просмотра урока"""
        url = reverse("lms:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), self.lesson.name
        )

    def test_lesson_create(self):
        """ Тест создания урока"""
        url = reverse("lms:lessons_create")
        data = {
            "name": "Test",
            "description": "Test",
            "video_linc": "youtube"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        """ Тест изменения урока"""
        url = reverse("lms:lessons_update", args=(self.lesson.pk,))
        data = {
            "name": "Test",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "Test"
        )

    def test_lesson_list(self):
        url = reverse("lms:lessons_list")
        response = self.client.get(url)
        data = response.json()
        # print(data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "course": self.course.pk,
                    "preview": None,
                    "description": self.lesson.description,
                    "video_linc": None,
                    "owner": self.user.pk
                }
            ]
        }
        self.assertEqual(
            data, result
        )

    def test_lesson_delete(self):
        """ Тест удаления урока"""
        url = reverse("lms:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )


class SubsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@gmail.com", is_staff=True, is_superuser=True)
        self.course = Course.objects.create(name="Test course", description="Test course", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subs(self):
        url = reverse("lms:subs_create")
        data = {"course": self.course.pk}
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, {"message": 'Подписка добавлена'}
        )

    def test_unsubs(self):
        url = reverse("lms:subs_create")
        data = {"course": self.course.pk}
        Subs.objects.create(course=self.course, user=self.user)
        response = self.client.post(url,data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {'message': "Подписка удалена"})