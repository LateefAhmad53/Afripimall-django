from django import forms
from piauth.models import CustomUser
from django import forms
from piauth.models import Product
from django_select2.forms import Select2Widget  # Import Select2Widget
from piauth.models import UserProfile


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'address', 'country', 'city', 'phone')


    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.password:
            self.fields['password'].widget = forms.TextInput(attrs={'type': 'password', 'value': '********'})




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'short_description', 'regular_price', 'discount_price', 'product_image', 'category', 'long_description', 'user']
        widgets = {
            'short_description': forms.Textarea(attrs={'rows': 3}),
            'long_description': forms.Textarea(attrs={'rows': 5}),
            'user': Select2Widget,  # Use Select2Widget for the user field
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = CustomUser.objects.all()




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add 'enctype="multipart/form-data"' attribute to the form
        self.fields['upload'].widget.attrs.update({'accept': 'image/*'})  # Add accept attribute to limit file types

