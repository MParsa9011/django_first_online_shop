from django.http import HttpResponse
from django.views import generic
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, reverse
from django.utils.translation import gettext as _
from django.contrib import messages

from .forms import CommentForm
from .models import Product, Comment
from cart.forms import AddToCartForm

# def test_translation(request):
#     result = _('Hello')
#     messages.success(request, 'this is a success message')
#     return HttpResponse(result)


class ProductListView(generic.ListView):
    # model = Product
    # queryset = Product.objects.filter(active=True)
    queryset = Product.objects.all()
    context_object_name = 'products/products_list.html'
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartForm()
        return context

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    # def get_success_url(self):
    #     return reverse('product_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        obj.product = product


        return super().form_valid(form)



