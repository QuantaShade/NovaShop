from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    category_id = request.GET.get("category")
    if category_id:
        products = products.filter(category_id=category_id)
    context = {
        'categories': categories,
        'products': products,
        "selected_category": category_id,
    }
    return render(request, 'pages/home.html', context)

def shop(request):
    return render(request, 'pages/shop.html')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customers/list.html", {
        "customers": customers
    })


def customer_create(request):

    if request.method == "POST":
        Customer.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            address=request.POST["address"],
        )
        return redirect("customer_list")

    return render(request, "customers/create.html")


def customer_update(request, id):

    customer = get_object_or_404(Customer, id=id)

    if request.method == "POST":
        customer.first_name = request.POST["first_name"]
        customer.last_name = request.POST["last_name"]
        customer.email = request.POST["email"]
        customer.phone = request.POST["phone"]
        customer.address = request.POST["address"]

        customer.save()

        return redirect("customer_list")

    return render(request, "customers/update.html", {
        "customer": customer
    })


def customer_delete(request, id):

    customer = get_object_or_404(Customer, id=id)

    if request.method == "POST":
        customer.delete()
        return redirect("customer_list")

    return render(request, "customers/delete.html", {
        "customer": customer
    })

def category_create(request):

    if request.method == "POST":
        Category.objects.create(
            name=request.POST["name"],
            description=request.POST["description"]
        )

        return redirect("category_list")

    return render(request, "categories/create.html")


def category_update(request, id):

    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        category.name = request.POST["name"]
        category.description = request.POST["description"]

        category.save()

        return redirect("category_list")

    return render(request, "categories/update.html", {
        "category": category
    })


def category_delete(request, id):

    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        category.delete()
        return redirect("category_list")

    return render(request, "categories/delete.html", {
        "category": category
    })

def product_list(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, "pages/productView.html", {
        "product": product
    })


def product_create(request):

    categories = Category.objects.all()

    if request.method == "POST":

        Product.objects.create(
            category=Category.objects.get(id=request.POST["category"]),
            name=request.POST["name"],
            description=request.POST["description"],
            price=request.POST["price"],
            stock=request.POST["stock"],
            image=request.FILES["image"],
        )

        return redirect("product_list")

    return render(request, "products/create.html", {
        "categories": categories
    })


def product_update(request, id):

    product = get_object_or_404(Product, id=id)
    categories = Category.objects.all()

    if request.method == "POST":

        product.category = Category.objects.get(id=request.POST["category"])
        product.name = request.POST["name"]
        product.description = request.POST["description"]
        product.price = request.POST["price"]
        product.stock = request.POST["stock"]

        if "image" in request.FILES:
            product.image = request.FILES["image"]

        product.save()

        return redirect("product_list")

    return render(request, "products/update.html", {
        "product": product,
        "categories": categories
    })


def product_delete(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")

    return render(request, "products/delete.html", {
        "product": product
    })

def order_list(request):

    orders = Order.objects.all()

    return render(request, "orders/list.html", {
        "orders": orders
    })


def order_create(request):

    customers = Customer.objects.all()

    if request.method == "POST":

        Order.objects.create(
            customer=Customer.objects.get(id=request.POST["customer"]),
            status=request.POST["status"],
            total_price=request.POST["total_price"]
        )

        return redirect("order_list")

    return render(request, "orders/create.html", {
        "customers": customers
    })


def order_update(request, id):

    order = get_object_or_404(Order, id=id)
    customers = Customer.objects.all()

    if request.method == "POST":

        order.customer = Customer.objects.get(id=request.POST["customer"])
        order.status = request.POST["status"]
        order.total_price = request.POST["total_price"]

        order.save()

        return redirect("order_list")

    return render(request, "orders/update.html", {
        "order": order,
        "customers": customers
    })


def order_delete(request, id):

    order = get_object_or_404(Order, id=id)

    if request.method == "POST":
        order.delete()
        return redirect("order_list")

    return render(request, "orders/delete.html", {
        "order": order
    })


def order_item_list(request):

    items = OrderItem.objects.all()

    return render(request, "order_items/list.html", {
        "items": items
    })


def order_item_create(request):

    orders = Order.objects.all()
    products = Product.objects.all()

    if request.method == "POST":

        product = Product.objects.get(id=request.POST["product"])
        quantity = int(request.POST["quantity"])

        OrderItem.objects.create(
            order=Order.objects.get(id=request.POST["order"]),
            product=product,
            quantity=quantity,
            unit_price=product.price,
            subtotal=product.price * quantity
        )

        return redirect("order_item_list")

    return render(request, "order_items/create.html", {
        "orders": orders,
        "products": products
    })


def order_item_update(request, id):

    item = get_object_or_404(OrderItem, id=id)

    orders = Order.objects.all()
    products = Product.objects.all()

    if request.method == "POST":

        product = Product.objects.get(id=request.POST["product"])
        quantity = int(request.POST["quantity"])

        item.order = Order.objects.get(id=request.POST["order"])
        item.product = product
        item.quantity = quantity
        item.unit_price = product.price
        item.subtotal = product.price * quantity

        item.save()

        return redirect("order_item_list")

    return render(request, "order_items/update.html", {
        "item": item,
        "orders": orders,
        "products": products
    })


def order_item_delete(request, id):

    item = get_object_or_404(OrderItem, id=id)

    if request.method == "POST":
        item.delete()
        return redirect("order_item_list")

    return render(request, "order_items/delete.html", {
        "item": item
    })