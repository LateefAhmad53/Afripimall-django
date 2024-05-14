from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Additional fields
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
   


    def masked_password(self):
        return "********"

    # The password field is automatically handled by Django and not defined here

    def __str__(self):
        return self.username
    

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    short_description = models.TextField()
    regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=100)
    long_description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    def __str__(self):
        return self.product_name

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    upload = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    organization = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=50, blank=True)
    timezone = models.CharField(max_length=50, blank=True)
    currency = models.CharField(max_length=10, blank=True)
    # Add other profile fields as needed    

    