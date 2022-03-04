from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


# INDEX
@login_required(login_url="login")
def control_index(request):
    context = {}
    return render(request, 'control/index/index.html', context)

# CATEGORY_ALL
@login_required(login_url="login")
def category_all(request):
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "code": code,
    }
    return render(request, "control/category/all.html", context)

# CATEGORY_ADD
@login_required(login_url="login")
def category_add(request):
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "code": code
    }
    return render(request, "control/category/add.html", context)

# CATEGORY_CREATE
@login_required(login_url="login")
def category_create(request):
    if request.method == "POST": 
        arr = list(map(lambda x: x.title.lower(), Category.objects.all()))
        if request.POST["category_title"].lower() not in arr:
            Category.objects.create(
                title = request.POST["category_title"],
                priority = request.POST["category_priority"]
            )
            return redirect("/control/category/all/?create")
        else:
            return redirect("/control/category/add/?title")

# CATEGORY_DETAIL
@login_required(login_url="login")
def category_detail(request, slug):
    category = Category.objects.get(slug = slug)
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "category": category,
        "code": code
    }
    return render(request, "control/category/detail.html", context)

# CATEGORY_EDIT
@login_required(login_url="login")
def category_edit(request):
    if request.method == 'POST':
        c = Category.objects.get(id=request.POST['id'])
        arr = list(map(lambda x: x.title.lower(), Category.objects.all()))      
        if request.POST["category_title"].lower() == c.title.lower():
            c.priority = request.POST['category_priority']
            c.save()
            return redirect("/control/category/all/?edit")
        elif request.POST["category_title"].lower() not in arr:
            c.title = request.POST['category_title']
            c.priority = request.POST['category_priority']
            c.save()
            return redirect("/control/category/all/?edit")
        else:
            return redirect("/control/category/detail/{}/?title".format(c.slug))

# CATEGORY_DELETE
@login_required(login_url="login")
def category_delete(request):
    if request.method == "POST":
        c = Category.objects.get(id=request.POST['id'])
        c.delete()
    return redirect("/control/category/all/?delete")










# PRODUCT_ALL
@login_required(login_url="login")
def product_all(request):
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    products = Product.objects.all()
    context = {
        "products": products,
        "code": code
    }
    return render(request, "control/product/all.html", context)

# PRODUCT_ADD
@login_required(login_url="login")
def product_add(request):
    categories = Category.objects.all()
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        'categories': categories,
        "code": code
    }
    return render(request, "control/product/add.html", context)

# PRODUCT_CREATE
@login_required(login_url="login")
def product_create(request):
    if request.method == 'POST' and request.FILES['file']:
        arr = list(map(lambda x: x.title.lower(), Product.objects.all()))
        if request.POST["title"].lower() not in arr:
            Product.objects.create(
                priority = request.POST['priority'],
                title = request.POST['title'],
                price = request.POST['price'],
                description = request.POST['description'],
                category_id = request.POST['category'],
                image_min = request.FILES['file'],
                image_max = request.FILES['file'],
            )
            return redirect('/control/product/all/?create/product')
        else:
            return redirect("/control/product/add/?title/product")

# PRODUCT_DETAIL
@login_required(login_url="login")
def product_detail(request, slug):
    product = Product.objects.get(slug = slug)
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    categories = Category.objects.all()
    context = {
        "product": product,
        "categories": categories,
        "code": code
    }
    return render(request, "control/product/detail.html", context)

# PRODUCT_EDIT
@login_required(login_url="login")
def product_edit(request):
    if request.method == 'POST' or request.FILES['file']:
        p = Product.objects.get(id=request.POST['id'])
        arr = list(map(lambda x: x.title.lower(), Product.objects.all()))
        if request.POST["title"].lower() == p.title.lower():
            p.priority = request.POST['priority']
            p.price = request.POST['price']
            p.description = request.POST['description']
            p.category_id = request.POST['category']
            try:
                p.image_min = request.FILES['file']
                p.image_max = request.FILES['file']
            except:
                pass
            p.save()
            return redirect('/control/product/all/?edit/product')
        elif request.POST["title"].lower() not in arr:
            p.title = request.POST['title']
            p.priority = request.POST['priority']
            p.price = request.POST['price']
            p.description = request.POST['description']
            p.category_id = request.POST['category']
            try:
                p.image_min = request.FILES['file']
                p.image_max = request.FILES['file']
            except:
                pass
            p.save()
            return redirect('/control/product/all/?edit/product')
        else:
            return redirect('/control/product/detail/{}/?title/product'.format(p.slug))

# PRODUCT_DELETE
@login_required(login_url="login")
def product_delete(request):
    if request.method == "POST":
        p = Product.objects.get(id=request.POST['id'])
        p.delete()
    return redirect("/control/product/all/?delete/product")







# ORDERS
@login_required(login_url="login")
def control_orders(request):
    orders = Order.objects.all()
    context = {
        "orders": orders
    }
    return render(request, "control/orders/all.html", context)

# ORDER_DETAIL
@login_required(login_url="login")
def order_detail(request, id):
    order = Order.objects.get(id = id)
    context = {
        "order": order
    }
    return render(request, "control/orders/detail.html", context)

# ORDER_COMPLETE
@login_required(login_url="login")
def order_complete(request):
    if request.method == "POST":
        order = Order.objects.get(id = request.POST["id"])
        order.proccessed = True
        order.save()
        return redirect("control_orders")
        







 
#  SLIDER_ADD
@login_required(login_url="login")
def slider_add(request): 
    try: 
        code = request.build_absolute_uri().split("?")[1] 
    except: 
        code = None 
    context = { 
        "code": code 
    } 
    return render(request, "control/slider/add.html", context) 
 
# SLIDER_ALL
@login_required(login_url="login")
def slider_all(request): 
    try: 
        code = request.build_absolute_uri().split("?")[1] 
    except: 
        code = None 
    slid = Slider.objects.all() 
    context = { 
        "slid": slid, 
        "code": code 
    } 
    return render(request, "control/slider/all.html", context) 
 
# SLIDER_CREATE
@login_required(login_url="login")
def slider_create(request): 
    if request.method == 'POST' and request.FILES['file']: 
        arr = list(map(lambda x: x.title.lower(), Slider.objects.all())) 
        if request.POST["title"].lower() not in arr: 
            Slider.objects.create( 
                title = request.POST['title'], 
                img = request.FILES['file'],                 
            ) 
            return redirect('/control/slider/all/?create') 
        else: 
            return redirect("/control/slider/add/?title") 
 
# SLIDER_DETAIL
@login_required(login_url="login")
def slider_detail(request, id): 
    slid = Slider.objects.get(id = id) 
    try: 
        code = request.build_absolute_uri().split("?")[1] 
    except: 
        code = None 
    context = { 
        "slid": slid, 
        "code": code 
    } 
    return render(request, "control/slider/detail.html", context) 
 
# SLIDER_EDIT
@login_required(login_url="login")
def slider_edit(request): 
    if request.method == 'POST' or request.FILES['file']: 
        p = Slider.objects.get(id = request.POST['id']) 
        arr = list(map(lambda x: x.title.lower(), Slider.objects.all())) 
        if request.POST["title"].lower() == p.title.lower(): 
            p.title = request.POST['title'] 
            try: 
                p.img = request.FILES['file'] 
            except: 
                pass 
            p.save() 
            return redirect('/control/slider/all/?edit/news') 
        elif request.POST["title"].lower() not in arr: 
            p.title = request.POST['title'] 
            try: 
                p.img = request.FILES['file'] 
            except: 
                pass 
            p.save() 
            return redirect('/control/slider/all/?edit/slider') 
        else: 
            return redirect('/control/slider/detail/{}/?name/product'.format(p.id)) 
 
#SLIDER_DELETE
@login_required(login_url="login")
def slider_delete(request): 
    if request.method == "POST": 
        p = Slider.objects.get(id=request.POST['id']) 
        p.delete() 
    return redirect("/control/slider/all/?delete/news")