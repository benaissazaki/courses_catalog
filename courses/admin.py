# pylint: disable=missing-class-docstring, missing-module-docstring
from django.contrib import admin
from .models import Category, Course


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'father_category')
    list_filter = ('father_category',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')