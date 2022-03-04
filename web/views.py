from django.shortcuts import render,redirect
from control.models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
import random

# Create your views here.

# WEB_INDEX
def web_index(request):
    if request.user.is_authenticated:
        customer = request.user.account
        order, created = Order.objects.get_or_create(
            account=customer, complete=False
        )
    else:
        order = None
    products = Product.objects.all()
    categories = Category.objects.all()
    slid = Slider.objects.all()
    context = {
        "products": products,
        "categories": categories,
        "order" : order,
        "slid" : slid
    }
    return render(request, 'web/pages/index.html', context)

# WEB_CATEGORY
def web_category(request, id):
    if request.user.is_authenticated:
        customer = request.user.account
        order, created = Order.objects.get_or_create(
            account=customer, complete=False
        )
    else:
        order = None
    categories = Category.objects.all()
    products = Product.objects.filter(category_id = id)
    context = {
        'products': products,
        'categories': categories,
        'c': id,
        "order" : order
    }
    return render(request, 'web/category/category.html', context)

# WEB_DETAIL
def web_detail(request, slug):
    if request.user.is_authenticated:
        customer = request.user.account
        order, created = Order.objects.get_or_create(
            account=customer, complete=False
        )
    else:
        order = None
    categories = Category.objects.all()
    product = Product.objects.get(slug = slug)
    context = {
        "product": product,
        "categories": categories,
        "order" : order
    }
    return render(request, "web/product/detail.html", context)

# WEB_ABOUT
@login_required(login_url="login")
def web_about(request):
    if request.user.is_authenticated:
        customer = request.user.account
        order, created = Order.objects.get_or_create(
        account=customer, complete=False
    )
    else:
        order = None
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        "products": products,
        "categories": categories,
        "order" : order
    }
    return render(request, 'web/about/about.html', context)

# WEB_404
@login_required(login_url="login")
def web_404(request):
    if request.user.is_authenticated:
        customer = request.user.account
        order, created = Order.objects.get_or_create(
        account=customer, complete=False
    )
    else:
        order = None
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        "products": products,
        "categories": categories,
        "order" : order
    }
    return render(request, 'web/about/404.html', context)











# LOGIN
def login(request):
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    if request.user.is_authenticated:
        customer = request.user.account
        order, created = Order.objects.get_or_create(
            account=customer, complete=False
        )
    else:
        order = None
    categories = Category.objects.all()
    context = {
        "categories": categories,
        'code': code,
        "order" : order
    }
    return render(request, 'web/login/login.html', context)

# REGISTER
def register(request):
    if request.user.is_authenticated:
        customer = request.user.account
        order, created = Order.objects.get_or_create(
            account=customer, complete=False
        )
    else:
        order = None
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'code': code,
        "order" : order
    }
    return render(request, "web/login/register.html", context)

# SIGN IN
def sign_in(request):
    if request.method =='POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('web_index')
        return redirect('/login/?error')

# SIGN UP
def sign_up(request):
    if request.method == 'POST':
        users = User.objects.all()

        for i in users:
            if request.POST['username'].lower() == i.username:
                return redirect('/register/?username')

        for i in users:
            if request.POST['email'].lower() == i.email:
                return redirect('/register/?email')

        u = User.objects.create_user(
            username = request.POST['username'].lower(),
            password = request.POST['password'],
            email = request.POST['email'].lower(),
            first_name = request.POST['full_name'],
        )
        u.account.phone = request.POST['number']
        u.account.save()
    return redirect('/login/?success')

# LOG_OUT
def log_out(request):
    auth.logout(request)
    return redirect('login')










# WEB_CART
@login_required(login_url="login")
def web_cart(request):
    if request.user.is_authenticated:
        customer = request.user.account
        order, created = Order.objects.get_or_create(
            account=customer, complete=False
        )
    else:
        order = None
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "order": order
    }
    return render(request, "web/pages/cart.html", context)

# ADD_TO_CART
def add_to_cart(request):
    customer = request.user.account
    order, created = Order.objects.get_or_create(
        account=customer, complete=False
    )
    data = json.loads(request.body)
    productId = data['productId']
    product = Product.objects.get(id=productId)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product
    )
    orderItem.quantity += int(data['quantity'])
    orderItem.save()
    return JsonResponse({'status': 200}, safe=False)

# WEB_CHECKOUT
def web_checkout(request):
    if request.user.is_authenticated:
        customer = request.user.account
        order, created = Order.objects.get_or_create(
            account=customer, complete=False
        )
    else:
        order = None
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "order": order
    }
    return render(request, "web/pages/checkout.html", context)






# ITEM_PLUS
def item_plus(request):
    customer = request.user.account
    order, created = Order.objects.get_or_create(
        account=customer, complete=False
    )
    data = json.loads(request.body)
    orderItem = OrderItem.objects.get(id=data['id'])

    orderItem.quantity +=  1
    orderItem.save()
    return JsonResponse({'status': 200}, safe=False)

# ORDER_REMOVE
def remove_order_item(request):
    customer = request.user.account
    order, created = Order.objects.get_or_create(
        account=customer, complete=False
    )
    data = json.loads(request.body)

    orderItem= OrderItem.objects.get(id=data['id'], order=order)
    orderItem.delete()
    return JsonResponse({'status': 200}, safe=False)

# WEB_COMPLETE
def complete(request):
    customer = request.user.account
    order, created = Order.objects.get_or_create(
        account=customer, complete=False
    )
    data = json.loads(request.body)
    order.complete = True
    c = ''
    for i in range(10):
        c += random.choice('1234567890QWERTYUIOASDFGHJKLZXCVBNMP')
    order.transaction = c
    order.fullname = data['fullname']
    order.phone = data['phone']
    order.email = data['email']
    order.address = data['address']
    # order.date_complete = '2022-02-04 17:50'
    order.save()
    return JsonResponse({'status': c}, safe=False) 








# CABINET
def cabinet(request):
    if request.user.is_authenticated:
        customer = request.user.account
        order, created = Order.objects.get_or_create(
            account=customer, complete=False
        )
    else:
        order = None
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        "products": products,
        "categories": categories,
        "order" : order
    }
    return render(request, 'web/cabinet/cabinet.html', context)

# DETAIL_CABINET
def cabinet_detail(request):
    if request.user.is_authenticated:
        customer = request.user.account
        order, created = Order.objects.get_or_create(
            account=customer, complete=False
        )
    else:
        order = None
    order = Order.objects.all()
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "order": order,
        "code": code
    }
    return render(request, "web/cabinet/detail.html", context)
