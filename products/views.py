from django.http import Http404
from typing import ContextManager
from django.db.models import query
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
#CBVs - Class Based Views
class ProductListView(ListView):
    #Traz todos os produtos do banco de dados sem filtro
    queryset = Product.objects.all()
    template_name = "products/list.html"

    #def get_context_data(self, *args, **kwargs):
    #    context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #    print(context)
    #    return context

class ProductDetailView(DetailView):
    #Traz todos os produtos do banco de dados
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context =  super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

#FBVs - Function Based Views
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)

def product_detail_view(request, pk=None, *args, **kwargs):
    print(args)
    print('-'*30)
    print(kwargs)
    print('-'*30)
    #queryset = Product.objects.all()
    #instance = Product.objects.get(pk=pk) #Pega o ID do objeto
    #instance = get_object_or_404(Product, pk=pk)

    qs = Product.objects.filter(id=pk)

    if qs.count() == 1:
        instance = qs.first
    else:
        raise Http404("Esse produto não existe...")

    context = {
        #'object_list': queryset
        'object': instance
    }
    return render(request, "products/detail.html", context)
