from django.db import models
import datetime as dt


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    publicated = models.DateTimeField(null=True, blank=True, default=dt.datetime.now)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def is_publicated(self):
        return bool(self.publicated)