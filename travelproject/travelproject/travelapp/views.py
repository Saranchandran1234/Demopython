from django.http import HttpResponse
from django.shortcuts import render
from .models import place

#create your on views here.

obj=place.objects.all

def demo(request):
    return render(request,"index.html",{'result':obj})




