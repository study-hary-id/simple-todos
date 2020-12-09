from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import Todos


def index(request):
	items = Todos.objects.order_by('-id')
	return render(request, 'todos/index.html', 
		{'items': items})


def active(request):
	items = Todos.objects.filter(status=False) \
				.order_by('-id')
	return render(request, 'todos/index.html', 
		{'items': items})


def completed(request):
	items = Todos.objects.filter(status=True) \
				.order_by('-id')
	return render(request, 'todos/index.html', 
		{'items': items})


def clear_completed(request):
	Todos.objects.filter(status=True).delete()
	return HttpResponseRedirect(reverse('index'))


def create(request):
	try:
		title = request.POST['title']
		todos = Todos(title=title)
		todos.save()
		return HttpResponseRedirect(reverse('index'))
	except Exception:
		return HttpResponseRedirect(reverse('index'))


def update(request, id):
	try:
		todo = Todos.objects.get(id=id)
		todo.status = not todo.status
		todo.save()
		return HttpResponseRedirect(reverse('index'))
	except ObjectDoesNotExist:
		return HttpResponseRedirect(reverse('index'))


def delete(request, id):
	try:
		todo = Todos.objects.get(id=id)
		todo.delete()
		return HttpResponseRedirect(reverse('index'))
	except ObjectDoesNotExist:
		return HttpResponseRedirect(reverse('index'))

