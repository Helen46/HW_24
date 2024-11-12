from django.contrib import admin

from lms.models import Course, Lesson, Subs


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    search_fields = ("name",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("name", "course")
    search_fields = ("name", "course")


@admin.register(Subs)
class SubsAdmin(admin.ModelAdmin):
    list_display = ("user", "course")
    search_fields = ("user", "course")
