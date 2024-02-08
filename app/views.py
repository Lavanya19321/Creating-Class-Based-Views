from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http import HttpResponse
from app.forms import *


# returning http respose using classbased view
class Cbvhttpresponse(View):
    def get(self,request):
        return HttpResponse('<h1> this is the string from class based view </h1>')
    
#rendering of html page using class based view
class cbvhtml(View):
    def get(self,request):
        return render(request,'cbvhtml.html')
    
#Insert data through modelforms
class insert_school_by_cbv(View):
    def get(self,request):
        SFO=schoolform()
        d={'SFO':SFO}
        return render(request,'insert_school_by_cbv.html',d)
    def post(self,request):
        SFDO=schoolform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
        return HttpResponse('inserted successfully')


 
 
