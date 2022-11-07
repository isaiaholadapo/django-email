
from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage, get_connection, EmailMultiAlternatives


# Create your views here.

def send_emails(request):
    if request.method == "POST":
        with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            recipient_list = request.POST.get("email").split()
            subject = request.POST.get("subject")
            email_from = settings.EMAIL_HOST_USER
            message = request.POST.get("message")

            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()

    return render(request, 'mail/send_emails.html')


def send_email(request):
    if request.method == "POST":
        with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            subject = request.POST.get("subject")
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST.get("email"), ]
            message = request.POST.get("message")

            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()

    return render(request, 'mail/home.html')

def html_email(request):
    if request.method == "POST":
        with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            recipient_list = request.POST.get("email").split()
            subject = request.POST.get("subject")
            email_from = settings.EMAIL_HOST_USER
            message = request.POST.get("message")
            attachment = request.POST.get("attachment")

            msg = EmailMessage(subject, message, email_from, recipient_list, connection=connection)
            msg.attach_file(attachment)
            msg.send()

    return render(request, 'mail/html_emails.html')

