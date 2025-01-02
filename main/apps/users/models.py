from auditlog.registry import auditlog
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from main.apps.users.managers import CustomUserManager
from main.apps.users.managers import CustomUserQueryset


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=254, default="")
    last_name = models.CharField(max_length=254, default="")

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        default=False,
        help_text="určuje možnost přístupu do administrace",
    )

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager().from_queryset(CustomUserQueryset)()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    class Meta:
        verbose_name = "uživatel"
        verbose_name_plural = "uživatelé"
        ordering = ("email",)

    def __str__(self):
        if self.first_name and self.last_name:
            return self.fullname
        return str(self.email)

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"


auditlog.register(User)
