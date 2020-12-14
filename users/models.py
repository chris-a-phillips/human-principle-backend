from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=False)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
    department = models.CharField(max_length=255, blank=False)
    team = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.email


# class UserAccountManager(BaseUserManager):
#     def create_user(self, email, name, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')

#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name)

#         user.set_password(password)
#         user.save()

#         return user


# class User(AbstractUser, PermissionsMixin):
#     email = models.EmailField(verbose_name='email',
#                               max_length=255, unique=True)
#     name = models.CharField(max_length=255, blank=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserAccountManager

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def get_full_name(self):
#         return self.name

#     def get_short_name(self):
#         return self.name

#     def __str__(self):
#         return self.email
