from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfilesAdmin(admin.ModelAdmin):
    ordering = ['-id']
    search_fields = ['user__username']
