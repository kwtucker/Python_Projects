from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    #title = models.CharField(max_length=120, null=True, blank=True)
    #content = models.TextField()
    meetup_id = models.IntegerField(default=0)
    meetup_link = models.CharField(max_length=120, null=True, blank=True)
    # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'id': self.id})