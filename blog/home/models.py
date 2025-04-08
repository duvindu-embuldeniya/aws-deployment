from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media_profile_model', blank=True, null=True)


    def __str__(self):
        return f"{self.user.username}'s profile"
    
    @property
    def img_url(self):
        try:
            return f"{self.image.url}"
    
        except Exception as ex:
            return f"/static/images/static_profile_model/default.png"