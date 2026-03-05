from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import PawMedicUser
from .validators import validate_password_strength, validate_username_taken, validate_username_alpha
from .choices import PawMedicUserType


class RegistrationForm(UserCreationForm):
    class Meta:
        model = PawMedicUser
        fields = ('username', 'email', 'password1', 'password2', 'phone')


    def __init__(self, *args, role=None, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'outline-none'
            self.fields[field].help_text = None
            self.fields[field].error_messages = {
                 'required': f'Please enter your {field}.',
            }
        if role != PawMedicUserType.VET:
            self.fields.pop('phone')


    def clean_username(self):
        username = self.cleaned_data.get('username')
        validate_username_taken(username)
        validate_username_alpha(username)
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        validate_password_strength(password1)
        return password1



class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Invalid username/email or password.",
        'inactive': "This account is inactive.",
    }
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'outline-none'

        self.fields['username'].error_messages = {
            'required': 'Please enter your username or email.',
        }
        self.fields['password'].error_messages = {
            'required': 'Please enter your password.',
        }




