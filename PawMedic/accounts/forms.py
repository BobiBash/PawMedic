from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'password1', 'password2')