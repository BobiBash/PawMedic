from django.core.mail import send_mail

from PawMedic import settings
from appointments.models import Appointment
from django.dispatch import receiver
from django.db.models.signals import post_save
from celery import shared_task



@receiver(post_save, sender=Appointment)
def notify_user_appointment_booked(sender, instance, created, **kwargs):
    if created:
        send_appointment_notification.delay(
            user_email=instance.vet.email,
            appointment_details={
                'date': instance.slot.date,
                'time': instance.slot.time,
                'vet_name': instance.vet.get_fullname(),
                'pet_name': instance.pet.name
            }
        )

@shared_task
def send_appointment_notification(user_email, appointment_details):
    send_mail(
        subject='Your appointment details',
        message=f"""
        Your appointment has been booked:

        Date: {appointment_details['date']}
        Time: {appointment_details['time']}
        Vet: {appointment_details['vet_name']}
        Pet: {appointment_details['pet_name']}
        """,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email]
    )