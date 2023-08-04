from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify

UserModel = get_user_model()

# class UserChoices(models.Model):
#     CHOICES = (
#         ('CHOICE_ANSWER', 'Choice answer'),
#         ('OK', 'Okay'),
#         ('NO', 'No'),
#         ('I_AM_NOT_SURE', 'I am not sure'),
#     )
#     choices = models.CharField(
#         max_length=20,
#         choices=CHOICES,
#         blank=True,
#         null=True,
#         default='CHOICE_ANSWER',
#     )
#
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         if commit:
#             self.choices = self.choices.upper()
#         return self.choices
#
#     def __str__(self):
#         return f'{self.choices}'

CHOICES = (
    ('CHOICE ANSWER', 'Choice answer'),
    ('OK', 'Okay'),
    ('NO', 'No'),
    ('I AM NOT SURE', 'I am not sure'),
)


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
        on_delete=models.CASCADE,
    )

    user_choices = models.CharField(
        max_length=20,
        choices=CHOICES,
        blank=True,
        null=True,
        default='CHOICE_ANSWER',
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

    def __str__(self):
        return f'{self.title} :\n {self.text} :\n {self.user_choices}'


class UserAnswers(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.DO_NOTHING,
    )

    # user_choices = models.ForeignKey(
    #     to=Content,
    #     on_delete=models.DO_NOTHING,
    #     related_name='choices',
    #     # default=1,
    # )

    # content = models.ForeignKey(
    #     to=Content,
    #     on_delete=models.DO_NOTHING,
    #     # related_name='answers',
    #     null=True,
    #     blank=True,
    #     # default=1,
    # )

    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # if commit:
        #     self.user.save()
        #     self.user_choices.save()
        #     self.content.save()
        #     self.user = self.user
        #     self.content = self.content
        #     self.user_choices = self.user_choices

        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user} '
