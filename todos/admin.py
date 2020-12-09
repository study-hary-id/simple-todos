from django.contrib import admin
from .models import Todos


class TodosAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'status',)

admin.site.register(Todos, TodosAdmin)

