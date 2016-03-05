from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Event(models.Model):
    group_name = models.CharField(max_length=120, null=True, blank=True)
    event_name = models.CharField(max_length=120, null=True, blank=True)
    event_date = models.CharField(max_length=120, null=True, blank=True)
    event_id = models.CharField(max_length=255, null=True, blank=True)
    event_url = models.CharField(max_length=120, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:update', kwargs={'id': self.id})
