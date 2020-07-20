from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    # refer = models.CharField(max_length=500)

    def __str__(self):
         return self.summary
