from django.contrib import admin
from .models import Blog, Petcare, Petcarecategory, PetcareCategoriesPetcarecategoryOwners

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Petcare)
class PetCareAdmin(admin.ModelAdmin):
    pass

@admin.register(Petcarecategory)
class PetCareCategoryAdmin(admin.ModelAdmin):
    pass

# @admin.register(PetcareCategoriesPetcarecategoryOwners)
# class PetcareCategoriesPetcarecategoryOwnersAdmin(admin.ModelAdmin):
#     pass