from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
    )


class MyUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, url, password=None):
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            return ValueError("Users must have a password")
        if not url:
            raise ValueError("Users must have a portfolio url")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            url=url,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, first_name, last_name, url, password):
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            url=url,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email                   = models.EmailField(verbose_name='email', max_length=255, unique=True)
    date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active               = models.BooleanField(default=True)
    is_admin                = models.BooleanField(default=False)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    first_name              = models.CharField(max_length=150)
    last_name               = models.CharField(max_length=150)
    url                     = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'url']

    objects = MyUserManager()

    def __str__(self):
        return self.email + ", " + self.first_name + ", " + self.last_name


    def has_perm(self, perm, obj=None):
        return self.is_admin


    def has_module_perms(self, app_Label):
        return True