from django.contrib import admin

from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(Pizza)
