from django.shortcuts import render
from django import http

# Create your views here.
def show_main(request: http.HttpRequest):
    context = {
        'nama': 'Dion Wisdom Pasaribu',
        'kelas': 'PBP F',
        'applicationName': 'BliBola',
    }
    return render(request, 'main.html', context)
