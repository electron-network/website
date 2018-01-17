from django.urls import path

from accounts.views import email_capture


app_name = 'accounts'

urlpatterns = [
    path('email-capture/', email_capture, name='email-capture')
]
