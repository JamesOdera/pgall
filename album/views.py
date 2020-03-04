from django.shortcuts import render
from django.http import HttpResponse

def photo(request):
    return render(request, 'photo.html')
