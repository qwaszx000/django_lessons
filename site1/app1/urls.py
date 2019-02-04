#created by me

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
	path('about/', views.about, name="about"), 
	path('hello', views.hello_world, name="hello_world"),
	path('form_handler', views.formHandler, name="formH"),
	path('landing', views.landing, name="landing"),
]
urlpatterns += staticfiles_urlpatterns()