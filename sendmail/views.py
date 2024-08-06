from django.shortcuts import render, HttpResponse
from .forms import EmailFORM
from django.core.mail import send_mail
from django.conf import settings


def post_data(request):
    if request.method == 'POST':
        form = EmailFORM(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"Hello, это {cd['name']}"
            message = f"{cd['comments']} \n\n Моя почта: {cd['email']}"
            recipient_list = [settings.EMAIL_HOST_USER]  # ваш email, указанный в настройках
            send_mail(
                subject, message, settings.EMAIL_HOST_USER, recipient_list
            )
            return HttpResponse('<h1>Спасибо</h1>')
    else:
        form = EmailFORM()
    return render(request, 'form.html', {
        "form": form
    })
