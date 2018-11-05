from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def restaurants(request):
	return render(request,'canteens/restaurants.html')

def nc_gb(request):
	return render(request,'canteens/orders-list-gbnc.html')


def nc_8(request):
	return render(request,'canteens/orders-list-8bnc.html')

def nc_7(request):
	return render(request,'canteens/orders-list-7bnc.html')

def nc_3(request):
	return render(request,'canteens/orders-list-3bnc.html')

def checkout(request):
	value=request.GET.get('items')
	price=request.GET.get('total')

	# value=request.POST['items']
	# price=request.POST['total']
	# print(value)
	# print(price)
	return render(request,'canteens/checkout.html')

def bill(request):
	value=request.GET.get('items')
	price=request.GET.get('total')
	print(value)
	print(price)
	return render(request,'canteens/bill.html',{"value":value,"price":price,"user":request.user,})