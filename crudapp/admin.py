from django.contrib import admin
from crudapp.models import Board

# Register your models here.
@admin.register(Board)
class Board(admin.ModelAdmin):
    list_display = ['id', 'title', 'body', 'update_date']
    list_display_links = ['id', 'title', 'body']