from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import CustomerDetails

# Create your views here.
def addandshow(request):
  customer = CustomerDetails(request.POST)
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    address = request.POST['address']
    city = request.POST['city']
    zipcode = request.POST['zipcode']

    customer = CustomerDetails.objects.create(name=name, email=email, address=address, city=city, zipcode=zipcode)
    customer.save()
    customer = CustomerDetails.objects.all()
  else:
    customer = CustomerDetails()
    customer = CustomerDetails.objects.all()

  return render(request, 'addandshow.html', {'customer':customer})

def edit(request, id):
  customer = CustomerDetails.objects.get(id=id)
  return render(request, 'edit.html', {'customer':customer})

def update(request, id):
  if request.method=='POST':
    customer = CustomerDetails.objects.filter(id=id)
    customer.update(
      name = request.POST['name'],
      email = request.POST['email'],
      address = request.POST['address'],
      city = request.POST['city'],
      zipcode = request.POST['zipcode'],
    )
  return redirect('/')

def delete(request, id):
  customer = CustomerDetails.objects.get(id=id)
  customer.delete()
  return redirect('/')