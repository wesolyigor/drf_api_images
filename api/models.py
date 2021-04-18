import os

from django.conf import settings
from django.db import models
from django.utils import timezone


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"users/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


class Images(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField("Image", upload_to=upload_to, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

