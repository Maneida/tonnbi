from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
    ]

emal = models.EmailField(_('email address'), unique=True)
user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='buyer')
phone_number = models.CharField(max_length=15, blank=True)

