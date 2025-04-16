from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Product

# Create your views here.

def home_view(request, *args, **kwargs):
    return HttpResponse("<h1> Wassup </h1>")

def product_detail_view(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    return HttpResponse(f"Product id {obj.id}")

def product_api_detail_view(request, id, *args, **kwargs):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"},
                            status_code=404)
    return JsonResponse({"id": obj.id})