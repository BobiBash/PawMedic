from datetime import date
from celery import shared_task
from appointments.models import AppointmentSlot


@shared_task
def clean_expired_appointments():
    AppointmentSlot.objects.filter(date__lt=date.today()).delete()