
from django.urls import path
from app2 import views
app_name="app2"


urlpatterns = [
    path('upi2/',views.upi2,name="upi2"),
    path('hulli2/',views.hulli2,name="hulli2"),
]
