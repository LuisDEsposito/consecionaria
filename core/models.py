from django.db import models

# Create your models here.

class avatar_usuario(models.Model):
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
