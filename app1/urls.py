
from django.urls import path
from app1 import views
app_name="app1"

urlpatterns = [
    path('upi1/',views.upi1,name="upi1"),
    path('hulli1/',views.hulli1,name="hulli1"),
]
