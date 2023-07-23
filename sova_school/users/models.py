from django.db import models
from django.contrib.auth import models as auth_models
from django.core import validators


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
    )


    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return None
