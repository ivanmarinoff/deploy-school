from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify

UserModel = get_user_model()


class Content(models.Model):
    class Meta:
        ordering = ['-updated_at']

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    text = models.TextField(
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.id}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user} :\n {self.title} :\n {self.text}, :\n {self.image_url}'
