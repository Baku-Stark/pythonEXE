from django.db import models

# Create your models here.
class wishFormModel(models.Model):

    STATUS = ((1, 'Doing'), (2, 'Done'))

    wish_form = models.CharField(max_length=100)
    description = models.TextField()
    done = models.CharField(max_length=1, choices=STATUS)
    created_at = models.DateTimeField()