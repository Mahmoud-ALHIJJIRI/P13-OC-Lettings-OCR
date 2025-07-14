from django.contrib import admin
from lettings.models import Letting, Address


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('number', 'street', 'city')
