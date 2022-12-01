from django.shortcuts import render
from django.shortcuts import get_object_or_404
from ShoppingApp.models import UserManage, Category, Product
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.

def home(request):
    return render(request,'index.html')
def log(request):
    return render(request,'login.html')    
def index(request):
    return render(request,'index.html')    
def nav(request):
    return render(request,'nav.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def base(request):
    return render(request,'base.html')



def allProdCat(request,c_slug=None):
    c_page=None
    products_lists=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_lists=Product.objects.all().filter(category=c_page, available=True)
    else:
        products_lists=Product.objects.all().filter(available=True)
    paginator=Paginator(products_lists,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage, InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(request,"category.html",{'category':c_page,'products':products})

def product(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html', {'product':product})