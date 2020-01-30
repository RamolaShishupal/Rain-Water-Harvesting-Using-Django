from django.db import models

# Create your models here.

class Volume(models.Model):
    rain=models.FloatField(max_length=50)
    area=models.FloatField(max_length=50)

    def __str__(self):
        return '{}'.format(self.rain)
    def __str__(self):
        return '{}'.format(self.area)
    class Meta:
        verbose_name_plural='rain'














