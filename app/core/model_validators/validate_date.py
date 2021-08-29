from django.core.exceptions import ValidationError
import datetime


def validate_date(date):
    current_date = datetime.datetime.now().date()
    if date.date() >= current_date:
        return date
    else:
        raise ValidationError("This Date is Past")
