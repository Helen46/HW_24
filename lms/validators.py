from rest_framework.serializers import ValidationError

permitted_resources = "youtube"


def validate_permitted_resources(value):
    if permitted_resources not in value:
        raise ValidationError("Используется не допустимый сторонний ресурс")
