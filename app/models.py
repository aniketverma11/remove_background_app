from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/')

class Result(models.Model):
    image = models.ImageField(upload_to='images/')