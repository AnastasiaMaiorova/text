from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_name', 'first_name', 'email', 'phone', 'address']


admin.site.register(Customer, CustomerAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    # prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class OilAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'artikul', 'slug', 'price', 'available', 'valume', 'stock']
    # list_filter = ['available', 'created', 'updated']


admin.site.register(Oil, OilAdmin)


class FilterAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'artikul', 'slug', 'price', 'available', 'size', 'stock']
    # list_filter = ['available', 'created', 'updated']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'date']


admin.site.register(Filter, FilterAdmin)
admin.site.register(ProductCart)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Notification)
