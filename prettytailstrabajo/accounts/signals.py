from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_to_users_group(sender, instance, created, **kwargs):
    if created:
        try:
            users = Group.objects.get(name='Cliente')
        except Group.DoesNotExist:
            users = Group.objects.create(name='Administrativo')
            users = Group.objects.create(name='Cliente')
            users = Group.objects.create(name='Veterinario')            
        instance.user.groups.add(users)