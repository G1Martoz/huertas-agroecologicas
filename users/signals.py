from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver

@receiver(post_save, sender=User)
def add_user_to_default_group(sender, instance, created, **kwargs):
    if created:
        try:
            usuario_group = Group.objects.get(name='Usuario')
            instance.groups.add(usuario_group)
        except Group.DoesNotExist:
            # Create the group if it doesn't exist
            usuario_group = Group.objects.create(name='Usuario')
            instance.groups.add(usuario_group)