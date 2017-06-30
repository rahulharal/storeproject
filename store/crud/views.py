from django.shortcuts import render
from crud.models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File
import base64
from django.core import serializers

@csrf_exempt 
def add_branch(request):
	if request.POST:
		branch_name = request.POST['branch_name']
		Branch.objects.create(brach_name= branch_name)
		return HttpResponse("Branch Save")
@csrf_exempt 
def add_brand(request):
	if request.POST:
		brand_name = request.POST['brand_name']
		Brands.objects.create(brand_name=brand_name)
		return HttpResponse("Brand Save")
@csrf_exempt 
def add_product(request):
	if request.POST:
		product_name = request.POST['product_name']
		Products.objects.create(product_name=product_name)
		return HttpResponse("Product Save")

@csrf_exempt 
def add_store(request):
	if request.POST:
		branch_name = request.POST['branch_name']
		branch = Branch.objects.get(brach_name=branch_name)
		brand_name = request.POST['brand_name']
		brand = Brands.objects.get(brand_name=brand_name)
		product_name = request.POST['product_name']
		product = Products.objects.get(product_name=product_name)

		img = request.POST['image']
		rating = request.POST['rating']
		address = request.POST['address']
		name = request.POST['name']

		with open("media/product.jpg", "wb") as image:
		  image.write(img.decode('base64'))
		img = File(open("media/product.jpg","rb"))

		store = Store.objects.create(image=img, product=product, rating=rating, address=address, name=name)
		store.branch.add(branch)
		store.brands.add(brand)
		store.save()
		return HttpResponse("Brand Save")

@csrf_exempt 
def show_store(request):
	store=Store.objects.all()
	data = serializers.serialize("json", store)
	return HttpResponse(data)
