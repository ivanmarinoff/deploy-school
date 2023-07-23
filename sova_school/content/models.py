from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify



UserModel = get_user_model()


class Content(models.Model):
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    text = models.TextField(
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    updated_at = models.DateTimeField(default=datetime.now(), blank=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.user}-{self.id}')
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.text}'

    # def get_absolute_url(self):
    #     if self.pk:
    #         return reverse_lazy('content-details', kwargs={'pk': self.pk})
    #     return reverse_lazy('read-content', kwargs={'pk': self.pk})
