from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect
from piauth.models import CustomUser, Product
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from .utils import TokenGenerator,generate_token
from django.utils.http import  urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes,DjangoUnicodeDecodeError
from django.utils.encoding import  force_str
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse
from django.views.generic import View
from piauth.forms import ProductForm
from piauth.forms import UserProfileForm
from piauth.models import UserProfile



# Create your views here.


class activate(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=uid)#get_object_or_404
        except Exception as identifier:
            user = None
        
        if user is not None and generate_token.check_token(user, token):
                user.is_active= True
                user.save()
                messages.info(request, "Your account has been verified successfully.")
                return redirect(reverse('login_user'))
        
        return render(request, 'registration/activatefail.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('index')  # Assuming 'index' is the name of your index view
        else:
            messages.error(request,'Invalid username or password. Please try again.')
            return redirect('/auth/login_user')

    return render(request, 'registration/login_user.html')  # Make sure to replace 'your_template_folder' with the actual path

def register(request):
    username = ""

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        address = request.POST["address"]
        country = request.POST["country"]
        city = request.POST["city"]
        phone = request.POST["phone"]

        # Check password match
        if password1 != password2:
            messages.warning(request, 'Passwords do not match')
            return redirect('register')

        # Check username existence
        try:
            if CustomUser.objects.get(username=username):
                messages.info(request, 'User already exists')
                return redirect('register')
        except CustomUser.DoesNotExist:
            pass

        # Check email existence
        try:
            if CustomUser.objects.get(email=email):
                messages.info(request, 'User with this email already exists')
                return redirect('register')
        except Exception as identifier:
            pass

        # Create user
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password1,
            address=address,
            country=country,
            city=city,
            phone=phone
        )
        user.is_active = False
        user.save()
        
        # Send email for account activation
        email_subject = 'Activate your account'
        message = render_to_string('registration/activate.html', {
            'user': user,
            'domain': 'http://127.0.0.1:8000/',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user),
            
        })

        email_message=EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email],)
        email_message.send()
        messages.success(request, 'Account created successfully. Please check your email to verify your account.')
        return redirect('/auth/login_user')  # Redirect to the login page
    return render(request, 'registration/register.html')  # Make sure to replace 'your_template_folder' with the actual path
    
def logout_user(request):
    logout(request)
    return redirect('/auth/login_user')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def orders(request):
    return render(request,"orders.html")

def mail_send(request):
    return render(request,"registration/mail-send.html")

from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

from django.http import HttpResponseRedirect

def user_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Construct the URL for the Django admin profile editing page
    admin_profile_edit_url = reverse('admin:piauth_userprofile_change', args=[user_profile.id])
    
    # Append a query parameter for the redirect URL to the admin profile editing URL
    redirect_url = reverse('profile_view')  # URL name of the profile_view page
    admin_profile_edit_url += f'?next={redirect_url}'
    
    # Redirect users to the Django admin profile editing page
    return HttpResponseRedirect(admin_profile_edit_url)

from django.shortcuts import render, redirect
from django.urls import reverse

def profile_view(request):
    redirect_url = request.GET.get('next')  # Get the redirect URL from query parameters
    if redirect_url:
        return redirect(redirect_url)

    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = None
    else:
        user_profile = None
    
    return render(request, 'profile_view.html', {'user_profile': user_profile})



def account_settings_connections(request):
    return render(request,"account-settings-connections.html")

def account_settings_notifications(request):
    return render(request,"account-settings-notifications.html")

def password_change(request):
    return render(request,"registration/password_change.html")

def password_change_done(request):
    return render(request,"registration/password_change_done.html")

def mobile_verification(request):
    return render(request,"registration/mobile-verification.html")

def otp_verification(request):
    return render(request,"registration/otp-verification.html")

def reset(request):
        return render(request,"registration/reset.html")











@login_required
def addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'Product added successfully!')
            return redirect('product_success', product_id=product.id)
        
 # Redirect to the product detail page
    else:
        form = ProductForm()
    
    return render(request, 'addproduct.html', {'form': form})
@login_required
def product_detail(request, product_id,):
    # Retrieve the product object from the database
    product = get_object_or_404(Product, pk=product_id)
    # You may also perform additional logic here, such as checking permissions or adding view counts
    return render(request, 'product_detail.html', {'product': product})

#def product_success(request):
    #return render(request,"product_success.html")
def product_success(request, product_id,):
    # Retrieve the product object from the database
    product = get_object_or_404(Product, pk=product_id)
    # You may also perform additional logic here, such as checking permissions or adding view counts
    return render(request, 'product_success.html', {'product': product})
