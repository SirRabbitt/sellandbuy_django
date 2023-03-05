from django.shortcuts import render, redirect
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

# Create your views here.
from . models import Product, Category
from . forms import ProductForm


def ShowAllProducts(request):
    if Category == None:
        products = Product.objects.filter(is_published = True).order_by('-price')
    else :
        products = Product.objects.filter(category__name = Category)



    page_num = request.GET.get("page")
    paginator = Paginator(products,3)
    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    categories = Category.objects.all()    

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'showProducts.html', context)


def ProductDetail(request, pk):
    eachProduct = Product.objects.get(id=pk)
    
    context = {
        'eachProduct': eachProduct
    }
    return render(request, 'productDetail.html', context)
@login_required(login_url = 'login')
def addProduct(request):
    form = ProductForm()
    if request.method== 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showProducts')

    context = { 
        "form":form
    }

    return render(request,'addProduct.html', context)
@login_required(login_url = 'login')
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('showProducts')
     
    context = { 
        "form":form
    }

    return render(request,'updateProduct.html', context)

@login_required(login_url = 'login')
def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('showProducts')


def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query :
            products = Product.objects.filter(name__contains = query) 
            return render (request, 'searchbar.html', {'products':products})
        else:
            print("No information to show")
            return request(request, 'searchbar.html',{})

        
