from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def naveen(resquest):
    return HttpResponse(' is a good boy')
def kishore(resquest):
    return HttpResponse('play boy')
def puneeth(resquest):
      return HttpResponse('is a good boy')
def rakesh(resquest):
    return HttpResponse('is a bad boy')