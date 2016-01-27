from django.shortcuts import render, Http404
from .models import Products, ProductImage

# Create your views here.


def get_products(request):
    '''
    The aim of this module is to take in all the products and display them on the
    webpage using the main page
    :param request:takes in a request
    :return: renders the request, template and context dict which is the products
    '''
    products = Products.objects.all()
    context = {
        "products": products
    }
    template = "product/home.html"
    return render(request, template, context)


def get_single_product(request, slug):
    '''

    :param request: takes in a request value
    :param slug: takes in the slug from the model Products to use as a get
    function since it is unique. The URL will also be in the form of the slug

    :return: renders the context(Dict), request, and template which is in this
    case the product/single.html

    '''
    try:
        product = Products.objects.get(slug=slug)
        images = ProductImage.objects.filter(product=product)
        context = {
            'product': product,
            'images': images
        }
        template = "products/single.html"
        return render(request, context, template)
    except:
        raise Http404
