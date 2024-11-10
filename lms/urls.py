from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.views import CourseViewSet, LessonCreateApiView, LessonListApiView, LessonUpdateApiView, \
    LessonRetrieveApiView, LessonDestroyApiView, SubsAPIView, SubsListAPIView
from lms.apps import LmsConfig

app_name = LmsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lessons_create"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lessons_retrieve"),
    path("lessons/update/<int:pk>/", LessonUpdateApiView.as_view(), name="lessons_update"),
    path("lessons/delete/<int:pk>/", LessonDestroyApiView.as_view(), name="lessons_delete"),
    path('subs/create/', SubsAPIView.as_view(), name='subs_create'),
    path('subs/', SubsListAPIView.as_view(), name='subs_list'),
]

urlpatterns += router.urls
