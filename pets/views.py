from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
import cloudinary.uploader
from .forms import PetForm
from .models import Pet

# Create your views here.
class ListPet(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = 'pets.view_pet'
    model = Pet
    template_name = 'pets/pets.html'

    def get_queryset(self):
        return Pet.objects.filter(owner_id=self.request.user.id)

class ViewPet(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = 'pets.view_pet'
    model = Pet
    template_name = 'pets/view-pet.html'

    def get_queryset(self):
        return Pet.objects.filter(owner_id=self.request.user.id)

class AddPet(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'pets.add_pet'
    form_class = PetForm
    template_name = 'pets/add-pet.html'
    success_url = reverse_lazy('pets')

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.owner_id = self.request.user.id
        photo = self.request.FILES.get('pet_photo')
        if photo:
            result = cloudinary.uploader.upload(photo)
            pet.pet_photo = result['public_id']
        pet.save()
        return redirect('pets')

class EditPet(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'pets.change_pet'
    form_class = PetForm
    template_name = 'pets/edit-pet.html'
    success_url = reverse_lazy('pets')

    def form_valid(self, form):
        pet = form.save(commit=False)
        photo = self.request.FILES.get('pet_photo')
        if photo:
            result = cloudinary.uploader.upload(photo)
            pet.pet_photo = result['public_id']
        pet.save()
        return redirect('pets')

    def get_queryset(self):
        return Pet.objects.filter(owner_id=self.request.user.id)

class DeletePet(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = 'pets.delete_pet'
    model = Pet
    template_name = 'pets/delete-pet.html'
    success_url = reverse_lazy('pets')

    def get_queryset(self):
        return Pet.objects.filter(owner_id=self.request.user.id)
