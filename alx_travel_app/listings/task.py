from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_confirmation_email(email, booking_reference):
    send_mail(
        subject="Booking Confirmed",
        message=f"Your booking {booking_reference} has been confirmed.",
        from_email="noreply@alxtravel.com",
        recipient_list=[email],
        fail_silently=False,
    )
