from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'todos/index.html')

def active(request):
	return render(request, 'todos/index.html')

def completed(request):
	return render(request, 'todos/index.html')

def clear_completed(request):
	return render(request, 'todos/index.html')

def create(request):
	return render(request, 'todos/index.html')

def update(request, id):
	return render(request, 'todos/index.html')

def delete(request, id):
	return render(request, 'todos/index.html')

