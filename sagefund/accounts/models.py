from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    date_of_birth = models.DateField(default="1900-01-01")

    def __str__(self):
        return self.username