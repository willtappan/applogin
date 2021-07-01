from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Registro(models.Model):
    """Profile model.

    Proxy model that extends the base data with other
    information.
    """

    user =models.OneToOneField(User, on_delete=models.CASCADE)
    pais =models.CharField(max_length=20)
    estado =models.CharField(max_length=20)
    genero =models.CharField(max_length=10)

    def __str__(self):
        """Return username."""
        return self.user.username


