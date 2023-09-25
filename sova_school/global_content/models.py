from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()


class GlobalContent(models.Model):
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    text = models.TextField(
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        blank=True,
        null=True,
    )

    file = models.FileField(
        upload_to='files',
        blank=True,
        null=True,
        default=None,
    )
    video = models.FileField(
        upload_to='videos',
        blank=True,
        null=True,
        default=None,
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.user}-{self.id}')
        return super().save(*args, **kwargs)




    def __str__(self) -> str:
        return f'{self.text} - {self.title} - {self.user} - {self.slug} - {self.image_url} - {self.file} - {self.video}'

