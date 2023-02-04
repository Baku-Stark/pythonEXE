from django.db import models

# Create your models here.
class Wish(models.Model):
    wish_title = models.CharField(max_length=250)
    my_wish = models.CharField(max_length=10000)

    def __str__(self):
        return self.wish_title