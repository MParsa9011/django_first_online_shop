from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField



class Product(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=100)
    description = RichTextField(verbose_name=_('Description'))
    short_description = models.CharField(verbose_name=_('Short Description'), max_length=300, blank=True)
    price = models.PositiveIntegerField(verbose_name=_('Price'), default=0)
    active = models.BooleanField(verbose_name=_('Activate Status'), default=True)

    datetime_created = models.DateTimeField(verbose_name=_('Date created'), default=timezone.now)
    datetime_modified = models.DateTimeField(verbose_name=_('Date modified'), auto_now=True)
    image = models.ImageField(verbose_name=_('Product Image'), upload_to='product/product_images', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):

    PRODUCT_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Product'))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', verbose_name=_('author'))
    body = models.TextField(verbose_name=_('Comment'))
    stars = models.CharField(max_length=1, choices=PRODUCT_STARS, default='5', verbose_name=_('What is your star?'))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Date modified'))

    active = models.BooleanField(default=True, verbose_name=_('Activate Status'))

    # Manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.pk])
