from datetime import date

from marshmallow import ValidationError


def validate_date(value):
    if value > date.today():
        raise ValidationError("Please enter a valid date.")