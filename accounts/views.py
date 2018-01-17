import re

from django.http import JsonResponse

from accounts.models import Signup


def email_capture(request):
    email_address = request.POST.get('email', '')

    # Parse the email string, make sure it's valid
    parsed = email_address.strip().lower()
    if not parsed or not re.match(r'[^@]+@[^@]+\.[^@]+', parsed):
        return JsonResponse({'msg': 'Bad Email'}, status=400)

    # Make sure we don't duplicate emails
    signup, created = Signup.objects.get_or_create(email=parsed)

    if not created:
        return JsonResponse({'msg': 'Already Exists'}, status=400)

    return JsonResponse({'msg': 'Success'})
