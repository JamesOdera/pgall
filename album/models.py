from django.db import models
import datetime as dt


class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='image/', null=True)
    name = models.CharField(max_length =60)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location, null=True)

    def save_image(self):
        self.save()

