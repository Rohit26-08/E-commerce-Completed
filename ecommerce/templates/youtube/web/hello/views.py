from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage(request):
    data={'name':['ankush','rohit','kalu'],
          'number':[]}
    return render(request,'index.html',data)
def ankush(request): 
    return HttpResponse('hello how are you')
def rohit(request):
    return HttpResponse("hello i am hear")
