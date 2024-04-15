from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField 
from django.db.models.signals import post_save


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, null=True,blank=True)
    Phone = models.CharField(max_length=100, null=True,blank=True) 
    
    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['username'] 

    def __str__(self):
        return self.email
    
    def save(self, *args,**kwargs):
        email_username, mobile = self.email.split('@')
        if self.first_name == "" or self.full_name == None:
            self.full_name= email_username
        if self.username == "" or self.username == None:
            self.full_name= email_username

        super(User,self).save()
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.FileField(upload_to="image", default="default/default-user.jpg",null=True,blank=True)
    full_name = models.CharField(max_length=100, null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    gender = models.CharField(max_length=10, null=True,blank=True)
    country = models.CharField(max_length=10, null=True,blank=True)
    state = models.CharField(max_length=10, null=True,blank=True)
    city = models.CharField(max_length=10, null=True,blank=True)
    address = models.CharField(max_length=10, null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefghijkl") # automatically generates randome pid

    def __self__(self):
        if self.full_name:
            return str(self.full_name)
        else:
            return str(self.user.full_name)


    def save(self, *args,**kwargs):
        if self.first_name == "" or self.full_name == None:
            self.full_name= self.user.full_name

        super(profile,self).save(*args,**kwargs)


def create_user_profile(sender, instance, create, **kwargs):
    if created:
        profile.objects.create(user=instance)

def save_user_profile(sender,instance,**kwargs):
    instance.Profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)


