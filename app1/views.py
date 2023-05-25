from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('This is the first FBV response')

def second(request):
    return HttpResponse('This is the second FBV response')

def one(request):
    return render(request,'one.html')

def two(request):
    return render(request,'two.html')