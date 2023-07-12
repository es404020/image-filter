from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
room =[
    {
        'id':1,'name':'java'
    },
    {
        'id':2 ,'name':'moon'
    },
    {
        'id':3,'name':'mojo'
    },

]

def index(request):
    return render(request,'index.html',{'rooms': room})
    # return HttpResponse('hello')

def rooms(request):
    return render(request,'rooms.html',{})