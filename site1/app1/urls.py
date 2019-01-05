#created by me

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
	path('about/', views.about, name="about"), 
	path('hello', views.hello_world, name="hello_world"),
	path('form_handler', views.formHandler, name="formH"),
]
