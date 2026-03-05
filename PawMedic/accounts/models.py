from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .choices import PawMedicUserType


# Create your models here.
class PawMedicUser(AbstractUser):
    email = models.EmailField(unique=True)

    phone = PhoneNumberField(unique=True)
    role = models.CharField(max_length=20, choices=PawMedicUserType.choices, default=PawMedicUserType.OWNER)
