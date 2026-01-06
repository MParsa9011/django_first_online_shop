from django import forms

from django.utils.translation import gettext as _

from orders.models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'order_notes']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'order_notes': forms.Textarea(attrs={
                'rows': 7,
                'placeholder': _('If you have any questions, please write it')
            }),
        }
