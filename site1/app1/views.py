from django.shortcuts import render
from django.http import HttpResponse

def index(r):
    return render(r, 'index.html')
	
def about(r):
    return render(r, 'about_us.html', {"values":["Александр Рей","https://freelancehunt.com/freelancer/qwaszx000.html"]})
	
def hello_world(r):
	return HttpResponse("<h1>Hello, world!</h1>")
	
def formHandler(r):
	print("Form request with data: " + str(r.POST))
	return HttpResponse("<h1>Hello, world!</h1>")
