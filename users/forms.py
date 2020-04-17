from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from address.models import AddressField

from .models import CustomUser
from django.db import models


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        address = AddressField()
        model = CustomUser
        fields = ('church_name','address', 'phone_number', 'email', 'password1', 'password2',)



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
