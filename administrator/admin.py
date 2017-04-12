from django.contrib import admin
from django.db.models import TextField
from django.forms import Textarea

from .models import Blog, Location, Category, CategoryLocationsLocationCategories

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 1})},
    }

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 1})},
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 1})},
    }

# @admin.register(CategoryLocationsLocationCategories)
# class CategoryLocationsLocationCategoriesAdmin(admin.ModelAdmin):
#     pass