from django.http import HttpResponse
from django.shortcuts import render

def main_page(request):
    return render(request,'index.html')

def second_page(request):
    return render(request, 'second.html')

def third_page(request):
    return render(request, 'third.html')

def first_page(request):
    return render(request, 'first.html')