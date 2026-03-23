from django import forms
from django.core.exceptions import ValidationError

from .models import Pet

class PetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'pet_photo':
                field.widget.attrs.update({'class': 'hidden'})
                continue
            field.widget.attrs.update({'class': 'bg-white w-60 border rounded-sm p-1 focus:outline-none'})

    def clean_date_of_birth(self):
        date = self.cleaned_data['date_of_birth']
        if date > date.today():
            raise ValidationError("Please enter a valid date.")
        return date

    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'date_of_birth', 'pet_photo']


        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Pet name'
            }),
            'species': forms.TextInput(attrs={
                'placeholder': 'Pet species'
            }),
            'breed': forms.TextInput(attrs={
                'placeholder': 'Pet breed'
            }),
            'date_of_birth': forms.TextInput(attrs={
                'type': 'date',
                'placeholder': 'Pet birth date',
                'id': 'flatpickr-date'
            }),
            'pet_photo': forms.FileInput(attrs={
                'placeholder': 'Pet picture',
                'accept': 'image/*',
            }),
        }

        error_messages = {
            'name': {
                'required': 'Pet name is required.',
                'max_length': 'Pet name cannot exceed 100 characters.'
            },
            'species': {
                'required': 'Pet species is required.',
                'max_length': 'Pet species cannot exceed 100 characters.'
            },
            'breed': {
                'required': 'Pet breed is required.',
                'max_length': 'Pet breed cannot exceed 100 characters.'
            },
            'date_of_birth': {
                'required': 'Pet birth date is required.',

            }
        }


