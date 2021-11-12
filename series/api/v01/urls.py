from django.urls import path
from .views import index
app_name = "series-v1"

urlpatterns = [
    path('',index,name='index')
]