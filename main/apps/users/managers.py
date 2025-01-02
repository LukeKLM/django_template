from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            msg = "Users must have an email address"
            raise ValueError(msg)

        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            last_login=timezone.now(),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def by_home(self, home):
        return self.filter(home=home)


class CustomUserQueryset(models.QuerySet):
    def active(self, active=True):
        """
        Filter users based on their is_active status.
        :param active: Can filter active, non active, all
        :return: CustomUser QuerySet
        """
        if active is not None:
            return self.filter(is_active=active)

        return self.all()

    def not_active(self):
        """
        Filter users which are not active.
        :return: CustomUser QuerySet
        """
        return self.filter(is_active=False)

    def owner(self, user):
        """Vrátí sám sebe"""
        return self.filter(pk=user.pk)
