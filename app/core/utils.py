from django.utils import timezone


def current_date():
    """Create current date object"""
    return timezone.now()
