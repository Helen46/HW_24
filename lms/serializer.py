from rest_framework.fields import SerializerMethodField
from rest_framework import serializers

from lms.models import Course, Lesson, Subs
from lms.validators import validate_permitted_resources


class LessonSerializer(serializers.ModelSerializer):
    video_linc = serializers.CharField(validators=[validate_permitted_resources])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lessons_course = SerializerMethodField()

    def get_count_lessons_course(self, object):
        return object.lesson_set.count()

    class Meta:
        model = Course
        fields = ("name", "count_lessons_course")


class SubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subs
        fields = "__all__"
