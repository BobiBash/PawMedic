from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .choices import PawMedicUserType
from .forms import RegistrationForm, LoginForm


# Create your views here.
def register_view(request):
    return render(request, 'accounts/register.html')

class RegisterView(CreateView):
    template_name = 'accounts/register_user.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['role'] = PawMedicUserType.OWNER
        return kwargs

    def form_valid(self, form):
        user = form.save(commit=False)
        user.role = PawMedicUserType.OWNER
        user.save()
        return redirect('home')

class RegisterVetView(CreateView):
    template_name = 'accounts/register_vet.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['role'] = PawMedicUserType.VET
        return kwargs

    def form_valid(self, form):
        user = form.save(commit=False)
        user.role = PawMedicUserType.VET
        user.is_active = False
        user.save()
        return redirect('home')

class LoginUserView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

