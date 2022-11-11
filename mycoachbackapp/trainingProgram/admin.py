from django.contrib import admin
from .models.program import Category, Program
# Register your models here.

admin.site.register(Category)
admin.site.register(Program)