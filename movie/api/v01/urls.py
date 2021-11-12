from django.urls import path
from .views import index,create,show,update,destroy
app_name = "movie-v1"

urlpatterns = [
    path('create/',create,name='create'),
    path('show/<int:id>',show,name='show'),
    path('update/<int:id>',update,name='update'),
    path('updatev2/<int:id>',update,name='update'),
    path('destroy/<int:id>',destroy,name='destroy'),
    path('',index,name='index'),

]