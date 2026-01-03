from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from products.models import Product, Comment


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'active', ]
    extra = 1
    show_change_link = True


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'active', ]

    inlines = [
        CommentsInline,
    ]



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'active', 'datetime_created']
    list_filter = ['active', 'author', 'product', 'datetime_created']
    ordering = ['-product']

