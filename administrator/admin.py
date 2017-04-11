from django.contrib import admin
from django.db.models import TextField
from django.forms import Textarea

from .models import Blog, Petcare, Petcarecategory, PetcareCategoriesPetcarecategoryOwners

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Petcare)
class PetCareAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 1})},
    }

@admin.register(Petcarecategory)
class PetCareCategoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 1})},
    }

# @admin.register(PetcareCategoriesPetcarecategoryOwners)
# class PetcareCategoriesPetcarecategoryOwnersAdmin(admin.ModelAdmin):
#     pass