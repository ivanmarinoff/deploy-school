from django.db import models





class WEBContent(models.Model):
    pass

    # title = models.CharField(
    #     max_length=100,
    #     blank=True,
    #     null=True,
    # )
    # text = models.TextField(
    #     blank=True,
    #     null=True,
    # )
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(default=datetime.now, blank=True)
    #
    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.CASCADE,
    # )
    # slug = models.SlugField(
    #     unique=True,
    #     blank=True,
    #     null=True,
    # )
    #
    # photos = models.ImageField(
    #     upload_to='images/',
    #     blank=True,
    #     null=True,
    # )
    # image_url = models.URLField(
    #     blank=True,
    #     null=True,
    # )
    #
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     if not self.slug:
    #         self.slug = slugify(f'{self.title}-{self.id}')
    #     return super().save(*args, **kwargs)

    # def __str__(self) -> str:
    #     return f'{self.text}'






