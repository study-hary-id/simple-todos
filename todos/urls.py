from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('active/', views.active, name='active'),
	path('completed/', views.completed, name='completed'),
	path('clear_completed/', views.clear_completed, name='clear_completed'),
	path('create/', views.create, name='create'),
	path('<int:id>/update/', views.update, name='update'),
	path('<int:id>/delete/', views.delete, name='delete'),
]
