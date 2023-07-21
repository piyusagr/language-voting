from django.urls import path
from .views import *
urlpatterns = [
    path("",main,name="voteee"),
    path("getquery",getquery,name="getquery"),
    
]
