from django.db.models import query
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.shortcuts import render
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

#FBVs - Function Based Views
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)
