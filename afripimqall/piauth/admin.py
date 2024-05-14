from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser
from .forms import CustomUserForm
from piauth.models import Product
from piauth.models import UserProfile
from piauth.forms import UserProfileForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('address', 'country', 'city', 'phone')}),  # Add your custom fields here
    )
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')  # Customize the displayed fields

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'regular_price', 'discount_price', 'category', 'user')
    list_filter = ('category',)
    search_fields = ('product_name',)


    def masked_password(self, obj):
        return "********"  # This function will show masked password in admin panel

    def get_masked_password(self, obj):
        return self.masked_password(obj)

    masked_password.short_description = 'Password'

# Unregister the default UserAdmin and register your CustomUserAdmin
admin.site.unregister(Group)
#admin.site.unregister(UserAdmin)
admin.site.register(CustomUser, CustomUserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm

admin.site.register(UserProfile, UserProfileAdmin)
