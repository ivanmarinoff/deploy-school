from django.core.validators import validate_email
from django.db import models
from django.contrib.auth import models as auth_models
from django.core import validators
from django.urls import reverse
from django.views import defaults


def validate_only_alphabetical(value):
    if not value.isalpha():
        raise validators.ValidationError("Only alphabetical characters are allowed")


class User(auth_models.AbstractUser):
    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        validators=[
            validate_only_alphabetical,
        ]
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        validators=[
            validate_only_alphabetical,
        ]
    )
    email = models.EmailField(
        unique=True,
        validators=[validate_email],
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return None

    def get_absolute_url(self):
        return reverse("profile-details", kwargs={"pk": self.objects.pk})


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.user.email} - {self.user.first_name} - {self.user.last_name} - {self.user.username} - {self.user.password}'
