from django.db import models

from django.utils.translation import gettext as _

from django.conf import settings


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    is_paid = models.BooleanField(default=False, verbose_name=_('Is Paid?'))

    first_name = models.CharField(max_length=100, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=100, verbose_name=_('Last Name'))
    phone_number = models.CharField(max_length=15, verbose_name=_('Phone Number'))
    address = models.CharField(max_length=500, verbose_name=_('Address'))

    order_notes = models.TextField(blank=True, verbose_name=_('Order Notes'))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Date Modified'))

    def __str__(self):
        return f'Order {self.id} : {self.first_name} {self.last_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'OrderItem {self.id} : {self.product} x {self.quantity} price: {self.price} in {self.order.id}'

