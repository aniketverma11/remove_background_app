from django.db import models

from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver


class Image(models.Model):
    image = models.ImageField(upload_to='images/')

class Result(models.Model):
    image = models.ImageField(upload_to='images/')


@receiver(post_delete, sender=Image)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)