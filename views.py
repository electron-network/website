from django.shortcuts import render
#use comments always in your code:)

def index(request):
    return render(request, 'index.html', {})
