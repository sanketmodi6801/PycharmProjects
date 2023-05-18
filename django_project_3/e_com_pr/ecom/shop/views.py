import logging
from math import ceil

from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from .models import Product, Contact, Orders, OrderUpdate

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


def index(request):
    # return HttpResponse("In the app..!!")
    products = Product.objects.all()
    # print(products)
    # n = len(products)
    # slides = n // 4 + ceil(n / 4 - (n // 4))

    allProds = []
    catprods = Product.objects.values('Category', 'id')
    cats = {item['Category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(Category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'slides': slides, 'range': range(1, slides), 'product': products}
    params = {'allProds': allProds}
    return render(request, 'home.html', params)


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    # product = Product.objects.get(myid)
    # print(product)
    params = {'view': product[0]}
    return render(request, "productPage.html", params)


def about(request):
    return render(request, 'about us.html')


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('Email', '')
        phone = request.POST.get('no', '')
        address = request.POST.get('add ', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', '')

        order = Orders(items_json=items_json, name=name, email=email, mobile=phone, address=address, city=city,
                       state=state,
                       zip=zip_code)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank': thank, 'id': id})
    return render(request, 'checkout.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        # print(name,email,phone,desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'contact.html')


def tracker(request):
    # if request.method=="POST":
    #     orderId = request.POST.get('orderId', '')
    #     email = request.POST.get('email', '')
    #     try:
    #         order = Orders.objects.filter(order_id=orderId, email=email)
    #         if len(order)>0:
    #             update = OrderUpdate.objects.filter(order_id=orderId)
    #             updates = []
    #             for item in update:
    #                 updates.append({'text': item.update_desc, 'time': item.timestamp})
    #                 response = json.dumps(updates, default=str)
    #             return HttpResponse(response)
    #         else:
    #             return HttpResponse('{}')
    #     except Exception as e:
    #         return HttpResponse('{}')

    return render(request, 'extra.html')


def tracked(request):
    update = OrderUpdate.objects.all()
    hii = request.POST.get('orderId', '')
    h = int(hii)
    print(h)
    params = {'view': update[h - 1]}
    return render(request, 'tracked.html', params)


def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return render(request, 'index.html')
