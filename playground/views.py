from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return render(request, 'hello.html')

def abc(request):
    return render(request, 'abc.html')