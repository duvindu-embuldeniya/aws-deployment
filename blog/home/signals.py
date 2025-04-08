from django.db.models.signals import post_save, post_delete
from . models import User, Profile
from django.dispatch import receiver




def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        created_user = instance

        Profile.objects.create(
            user = instance
        )


@receiver(post_delete, sender = Profile)
def delete_user(sender, instance, *args, **kwargs):
    deleted_profile = instance
    del_user = deleted_profile.user

    del_user.delete()


post_save.connect(create_profile, sender=User)