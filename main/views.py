import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from django.urls import reverse
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.


@csrf_exempt
@require_POST
def add_product_entry_ajax(request: HttpRequest):
    name = request.POST.get("name")
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    stock = request.POST.get("stock")
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user

    new_news = Product(
        name=name, 
        description=description,
        category=category,
        stock = stock,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_news.save()

    return HttpResponse(b"CREATED", status=201)

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def show_main(request: HttpRequest):
    filter_type = request.GET.get("filter", "all")  # default 'all'
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    context = {
        'nama': request.user.username,
        'kelas': 'PBP F',
        'applicationName': 'BliBola',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, 'main.html', context)

def create_product(request: HttpRequest):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        post_entry = form.save(commit = False)
        post_entry.user = request.user
        post_entry.save()
        return redirect('main:show_main')
    context={'form': form}
    return render(request, 'create_product.html', context)

@login_required(login_url='/login')
def show_product(request: HttpRequest, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product,
    }
    print(context)
    return render(request, 'product_detail.html', context)

def show_xml(request: HttpRequest):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request: HttpRequest):
    products = Product.objects.all().values(
        "id",
        "name",
        "price",
        "stock",
        "description",
        "thumbnail",   # pastikan nama field sesuai dengan model kamu
        "user",
    )
    return JsonResponse(list(products), safe=False)

def show_xml_by_id(request: HttpRequest, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request: HttpRequest, product_id):
    print("product_id: "+product_id)
    try:
        products = Product.objects.filter(pk=product_id).values()
        return JsonResponse(list(products), safe=False)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not Found"}, status=404)
    
def register(request: HttpRequest):
    if request.method == "POST":
        data = json.loads(request.body)
        form = UserCreationForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({ 
                "message": 'Your account has been successfully created!',
                "redirect_url": reverse('main:login'),
            }, status=201)
        else:
            return JsonResponse({ "errors": form.errors }, status=400)
    return render(request, 'register.html', {})

def login_user(request: HttpRequest):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = AuthenticationForm(request, data=data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = JsonResponse({"redirect_url": reverse("main:show_main")}, status=200)
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({ "errors": form.errors }, status=400)
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

