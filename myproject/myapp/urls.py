#my url to use
from django.urls import path
from .import views
urlpatterns=[
    path('',views.home, name='home')
]
