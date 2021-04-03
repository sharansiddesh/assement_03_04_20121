from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def upi1(request):
    return HttpResponse("<h1> page of app1.upi")


def hulli1(request):
    return render(request,"app1/hulli1.html")