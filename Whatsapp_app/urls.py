from django.urls import path, include
from . import views
urlpatterns = [ 
    path('',views.home),
    path('message',views.loginPage),
    path('SendData',views.SendData),
]