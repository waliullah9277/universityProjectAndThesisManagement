from django.core.exceptions import ValidationError


def validate_phone(value):

    if len(value) < 11:
        raise ValidationError(
            "Phone number must be at least 11 digits."
        )