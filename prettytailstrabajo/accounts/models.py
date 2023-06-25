from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# PERFIL DE USUARIO

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
<<<<<<< HEAD
    first_name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Nombre')
    last_name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Apellidos')
    rut_user = models.IntegerField(null=True, blank=True, verbose_name='Rut')
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name='Dirección')
    location = models.CharField(max_length=50, null=True, blank=True, verbose_name='comuna')
=======
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='comuna')
>>>>>>> f37be34e12396f6c2c65534768d11806d03a7709
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Teléfono')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
<<<<<<< HEAD
        Profile.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.first_name = instance.first_name
    instance.profile.last_name = instance.last_name
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
=======
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
# Create your models here.
>>>>>>> f37be34e12396f6c2c65534768d11806d03a7709
