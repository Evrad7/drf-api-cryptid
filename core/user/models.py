import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from ..abstract.models import AbstractManager, AbstractModel

# Create your models here.
class UserManager(AbstractManager, BaseUserManager):
   
    def create_user(self, username, email, password=None,
            **kwargs):
        """Create and return a `User` with an email, phone
            number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('User must have an email.')
        user = self.model(username=username,
            email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password,**kwargs):
        """
        Create and return a `User` with superuser (admin)
            permissions.
        """
        if password is None:
            raise TypeError('Superusers must have apassword.')
        if email is None:
            raise TypeError('Superusers must have anemail.')
        if username is None:
            raise TypeError('Superusers must have anusername.')
        user = self.create_user(username, email, password,
            **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

def user_directory_path(instance, filename):
    return "file_{}/{}".format(instance.public_id, filename)

class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True,
        max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    posts_liked=models.ManyToManyField(to="core_post.Post", related_name="liked_by")
    avatar=models.ImageField(null=True, blank=True, upload_to=user_directory_path)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
   
    objects = UserManager()

    def __str__(self):
       return f"{self.email}"
   
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    

    def like(self, post):
       self.posts_liked.add(post)
    
    def dislike(self, post):
        self.posts_liked.remove(post)

    def has_liked(self, post):
        return self.posts_liked.filter(pk=post.pk).exists()

