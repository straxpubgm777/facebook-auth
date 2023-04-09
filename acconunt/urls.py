from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home_page'),
    path('login/',login,name='login_page'),
]   