from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class Research(models.Model):
    author = models.ForeignKey('auth.User')
    source = models.TextField()
    keywords = models.TextField()
    meaning = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.keywords



# Create your models here.
