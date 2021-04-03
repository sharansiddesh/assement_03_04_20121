from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def upi2(request):
    return HttpResponse("<h1> page of app2.upi")


def hulli2(request):
    return render(request,"app2/hulli2.html")