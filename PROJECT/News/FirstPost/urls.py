from django.urls import path
from .views import show, fulldetail, addarticle, updatearticle, deletearticle
 

urlpatterns = [
    path('', show, name='home'),
    path('fulldetail/<int:pk>', fulldetail, name='fulldetail'),
    path('addarticle', addarticle, name='addarticle'),
    path('updatearticle/<int:pk>', updatearticle, name='updatearticle'),
    path('deletearticle/<int:pk>', deletearticle, name='deletearticle'),
]