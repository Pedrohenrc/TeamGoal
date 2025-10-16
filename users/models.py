from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.socialaccount.models import SocialAccount
# Create your models here.

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="profiles/", blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)


    def get_photo(self):
        if self.photo:
            return self.photo.url
        
        try:
            social_account = SocialAccount.objects.get(user=self)
            if social_account.provider == 'google':
                return social_account.extra_data.get('picture', '')
            elif social_account.provider == 'github':
                return social_account.extra_data.get('avatar_url', '')
        except SocialAccount.DoesNotExist:
            pass
        
        return None
    
    def __str__ (self):
        return self.username