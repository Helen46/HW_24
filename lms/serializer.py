from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lessons_course = SerializerMethodField()

    def get_count_lessons_course(self, object):
        return object.lesson_set.count()

    class Meta:
        model = Course
        fields = ("name", "count_lessons_course")
