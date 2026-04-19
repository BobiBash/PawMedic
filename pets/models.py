from cloudinary.models import CloudinaryField
from django.db import models

from accounts.models import PawMedicUser
from pets.validators import validate_date


class Pet(models.Model):
    owner = models.ForeignKey(PawMedicUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    date_of_birth = models.DateField(validators=[validate_date])
    pet_photo = CloudinaryField("pet_photos", null=True, blank=True)