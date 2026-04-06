from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PawMedicUser, VetProfile, EmailConfirmation, Service


@admin.register(PawMedicUser)
class PawMedicUserAdmin(UserAdmin):
    model = PawMedicUser
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active', 'is_staff', 'groups')


@admin.register(VetProfile)
class VetProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'is_published')
    list_filter = ('is_published', 'specialization')


@admin.register(EmailConfirmation)
class EmailConfirmationAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'created_at')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
