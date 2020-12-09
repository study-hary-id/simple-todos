from django.shortcuts import render
from django.http import HttpResponse
from .models import Todos

def index(request):
	items = Todos.objects.order_by('-id')
	return render(request, 'todos/index.html', {'items': items})

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

