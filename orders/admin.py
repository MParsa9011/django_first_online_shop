from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price']
    extra = 1
    show_change_link = True


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'phone_number', 'datetime_created', 'datetime_modified', 'is_paid']

    inlines = [
        OrderItemInline,
    ]



@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product','quantity', 'price']
    list_filter = ['order', 'product', 'quantity', 'price']
    ordering = ['-order']

