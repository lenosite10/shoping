from django.shortcuts import render ,get_object_or_404
from store.models import Product
from category.models import Category


def store(reguest, category_slug=None):
    categories = None
    products = None
    
    if category_slug !=None:
        categories = get_object_or_404(Category , slug = category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
        
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
        
    
    context= {
        'products':products,
        'product_count':product_count,
    }
    return render(reguest,'store/store.html',context)

def detail_product(request, category_slug , product_slug):
    try:
        singel_product= Product.objects.get(category__slug=category_slug, slug=product_slug)
    
    except Exception as e:
        raise e
    
    context = {
        'singel_product':singel_product,
    }
    
    
    return render(request,'store/product_detail.html',context)
