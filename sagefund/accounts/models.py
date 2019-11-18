from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    date_of_birth = models.DateField()

    def __str__(self):
        return self.username