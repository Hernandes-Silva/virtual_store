from django.contrib import admin
from .models import Item, Order
# Register your models here.
class ItemInline(admin.TabularInline):
    model = Item
    raw_id_fields = ['product']
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'cpf','email','paid','created','modified']
    list_filter = ['paid', 'created', 'modified']
    search_field = ['name', 'email', 'cpf']
    inline = [ItemInline]
