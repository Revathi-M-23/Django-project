from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def Smile(request):
    return HttpResponse('<h2>Always Keep smiling...</h2>')

def Faith(request):
    return HttpResponse('<i><h2>Believe In Yourself..</i></h2>')


