from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()


class Choices(models.Model):
    class UserChoices(models.TextChoices):
        YES = 'Yes'
        NO = 'No'
        I_AM_NOT_SURE = "I am not sure"
        # CHOICE_ANSWER = "Choice answer:"


class Content(models.Model):
    class Meta:
        ordering = ['-updated_at']

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
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
    )

    user_choices = models.CharField(
        max_length=20,
        choices=Choices.UserChoices.choices,
        blank=True,
        null=True,
        # default=Choices.UserChoices.CHOICE_ANSWER
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


class UserAnswers(models.Model):

    user_answers = models.ForeignKey(
        Content,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.user_answers