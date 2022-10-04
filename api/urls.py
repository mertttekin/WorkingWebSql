
from django.urls import  path
from .views import ariza_list


urlpatterns = [
    path('arizalar/', ariza_list)
]
