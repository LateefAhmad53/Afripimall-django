from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from piauth.models import Product
#from piauth.models import UserProfile



# Create your views here.
def home(request):
    return render(request,"home.html")

def newhome(request):
    return render(request,"newhome.html")

def loading(request):
    return render(request,"loading.html")

def addcategory(request):
    return render(request,"addcategory.html")


def cart(request):
    return render(request,"cart.html")

def checkout(request):
    return render(request,"checkout.html")

def contact(request):
    return render(request,"contact.html")

def create_gift(request):
    return render(request,"creategift.html")

def customer_service(request):
    return render(request, 'customer-service.html')


def discover(request):
    return render(request,"discover.html")

def gift_card(request):
    return render(request,"gift-card.html")

@login_required
def index(request):
    # Retrieve all products
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def dashboard(request):
    return render(request,'dashboard.html')


def inventory(request):
    return render(request,"inventory.html")

def my_shop(request):
    return render(request,"my-shop.html")

def order_history(request):
    return render(request,"order-history.html")

def order_receipt(request):
    return render(request,"order-receipt.html")

def sell(request):
    return render(request,"sell.html")

def shop_grid(request):
    return render(request,"shop-grid.html")

def track_order(request):
    return render(request,"track-order.html")

def user(request):
    return render(request,"user.html")

def wallet(request):
    return render(request,"wallet.html")







