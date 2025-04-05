from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render
from django.core.mail import EmailMessage


def send_test_email(request):
    send_mail(
        subject='Hello from sajid khaja',
        message='congrats you have been seleted as python degveloper ',
        from_email='fwani829@gmail.com',  # Sender email (configured in settings.py)
        recipient_list=['sajidsultankhawaja@gmail.com'],  # Receiver email
        fail_silently=False,
    )
    return HttpResponse("Email sent!")



def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        sender_email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"Message from {name} <{sender_email}>:\n\n{message}"

        send_mail(
            subject='New Contact Form Message',
            message=full_message,
            from_email='fwani829@gmail.com',
            recipient_list=['fwani829@gmail.com'],  # Send to YOUR email
        )

        return HttpResponse("Message sent successfully!")

    return render(request, 'contact.html')





def dynamic_email_view(request):
    if request.method == 'POST':
        to_email = request.POST.get('to_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        uploaded_file = request.FILES.get('attachment')  # 👈 Get uploaded file

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email='fwani829@gmail.com',
            to=[to_email],
        )

        if uploaded_file:
            email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)

        email.send()
        return HttpResponse("Email sent successfully with attachment!")

    return render(request, 'send_email.html')


def front_page(request):
    return render(request, 'front_page.html')  # ✅ Added return
