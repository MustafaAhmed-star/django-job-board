
from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #city = models.
    phone_num=models.CharField(max_length=11,null=True ,blank=True)
    image= models.ImageField(upload_to ='profile/')
    
    def __str__(self):
        return str(self.user)


@receiver(post_save ,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
