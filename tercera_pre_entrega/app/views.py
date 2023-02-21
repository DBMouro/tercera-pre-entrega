from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .models import User, Warehouse, Product
from .forms import CreateUserForm, LookupUserForm, CreateWarehouseForm, LookupWarehouseForm, CreateProductForm, LookupProductForm


def users(request):
    all_users = User.objects.all().values()
    print(all_users)
    template = loader.get_template('list.html')    
    context = {
        'users': all_users,
    }
    return HttpResponse(template.render(context))

def user_details(request, id):
    user = User.objects.get(id = id)
    template = loader.get_template('details.html')
    context = {
        'user': user
    }
    return HttpResponse(template.render(context, request))

def user_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = User(
                first_name = request.POST['first_name'], 
                last_name = request.POST['last_name'], 
                age = request.POST['age'],
                joined_date = date.today()
            )
            user.save()
            return HttpResponseRedirect(f'/users/details/{user.id}')
    else:
        form = CreateUserForm()

    return render(request, 'create.html', {'form': form})

def user_find(request):
    if request.method == 'POST':
        print(request.POST)
        form = LookupUserForm(request.POST)
        if form.is_valid():
            users = User.objects.filter(first_name__contains = request.POST['first_name']).filter(last_name__contains = request.POST['last_name']).values()
            if request.POST['age']:
                users = users.filter(age = request.POST['age'])
            print(users)
            template = loader.get_template('list.html')    
            context = {
                'users': users,
            }
            return HttpResponse(template.render(context))
    else:
        form = LookupUserForm()

    return render(request, 'find.html', {'form': form})

def warehouses(request):
    warehouses = Warehouse.objects.all().values()
    print(warehouses)
    template = loader.get_template('list.html')    
    context = {
        'warehouses': warehouses,
    }
    return HttpResponse(template.render(context))

def warehouse_details(request, id):
    warehouse = Warehouse.objects.get(id = id)
    template = loader.get_template('details.html')
    context = {
        'warehouse': warehouse
    }
    return HttpResponse(template.render(context, request))




def warehouse_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = CreateWarehouseForm(request.POST)
        if form.is_valid():
            wh = Warehouse(
                alias = request.POST['alias'], 
                location = request.POST['location'], 
                capacity_in_m3 = request.POST['capacity_in_m3'],
                cooling_system = True if request.POST.get('cooling_system') else False
            )
            wh.save()
            return HttpResponseRedirect(f'/warehouses/details/{wh.id}')
    else:
        form = CreateWarehouseForm()

    return render(request, 'create.html', {'form': form})

def warehouse_find(request):
    if request.method == 'POST':
        print(request.POST)
        form = LookupWarehouseForm(request.POST)
        if form.is_valid():
            warehouses = Warehouse.objects.filter(alias__contains = request.POST['alias']).filter(location__contains = request.POST['location']).values()
            print("Print")
            print(warehouses)
            if request.POST.get('cooling_system'):
                warehouses = warehouses.filter(cooling_system = True)
            if request.POST['capacity_in_m3']:
                warehouses = warehouses.filter(capacity_in_m3 = request.POST['capacity_in_m3'])
            print(warehouses)
            template = loader.get_template('list.html')    
            context = {
                'warehouses': warehouses,
            }
            return HttpResponse(template.render(context))
    else:
        form = LookupWarehouseForm()

    return render(request, 'find.html', {'form': form})



def products(request):
    products = Product.objects.all().values()
    print(products)
    template = loader.get_template('list.html')    
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context))

def product_details(request, id):
    product = Product.objects.get(id = id)
    print(product)
    template = loader.get_template('details.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))

def product_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = CreateProductForm(request.POST)
        if form.is_valid():
            product = Product(
                name = request.POST['name'], 
                category = request.POST['category'], 
                price = float(request.POST['price'])
            )
            product.save()
            return HttpResponseRedirect(f'/products/details/{product.id}')
    else:
        form = CreateProductForm()

    return render(request, 'create.html', {'form': form})

def product_find(request):
    if request.method == 'POST':
        print(request.POST)
        form = LookupProductForm(request.POST)
        if form.is_valid():
            products = Product.objects.filter(name__contains = request.POST['name']).filter(category__contains = request.POST['category']).values()
            if request.POST['price']:
                products = products.filter(price = request.POST['price'])
            template = loader.get_template('list.html')    
            context = {
                'products': products,
            }
            return HttpResponse(template.render(context))
    else:
        form = LookupProductForm()

    return render(request, 'find.html', {'form': form})

