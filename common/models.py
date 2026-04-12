from django.core.validators import MinLengthValidator
from django.db import models
from django_browser_reload.views import message

from accounts.models import PawMedicUser


# Create your models here.
class ReportedIssues(models.Model):
    user = models.ForeignKey(PawMedicUser, on_delete=models.CASCADE, related_name='issues')
    title = models.CharField(max_length=40)
    issue = models.TextField(max_length=2000, validators=[MinLengthValidator(30, message="Issue description must be at least 30 characters.")])
    created_at = models.DateField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
