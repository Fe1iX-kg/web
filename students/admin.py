from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email', 'enrolled']
    list_filter = ['enrolled']
    search_fields = ['name', 'email']