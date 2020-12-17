from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(email=self.normalize_email(
            email), name=name)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name, password):

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    team = models.CharField(max_length=255, default='no team provided')
    department = models.CharField(max_length=255, default='no department provided')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'team', 'department']

    def __str__(self):
        return self.email
