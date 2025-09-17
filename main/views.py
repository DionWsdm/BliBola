from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm

# Create your views here.
def show_main(request: HttpRequest):
    product_list = Product.objects.all()
    context = {
        'nama': 'Dion Wisdom Pasaribu',
        'kelas': 'PBP F',
        'applicationName': 'BliBola',
        'product_list': product_list,
    }
    return render(request, 'main.html', context)

def create_product(request: HttpRequest):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    context={'form': form}
    return render(request, 'create_product.html', context)

def show_product(request: HttpRequest, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

def show_xml(request: HttpRequest):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request: HttpRequest):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request: HttpRequest, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(requestL: HttpRequest, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        json_data = serializers.serialize("json", product_item)
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
