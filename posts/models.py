from __future__ import unicode_literals

from django.db import models
import reverse


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
         return reverse("detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-id", "-timestamp", "-updated"]

