from django.db import models
from django.contrib.auth.models import User

class AuthUserExtension(models.Model):
    """ for extended auth_user model """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile = models.CharField(max_length=13, null=True)
    