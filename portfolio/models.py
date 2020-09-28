from django.db import models

class Project(models.Model):
    tittle=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='portfolio/images')
    url=models.URLField(blank=True)

    def __str__(self):
        return self.tittle

class Dumps(models.Model):
    name=models.CharField(max_length=100)
    version=models.DecimalField(max_digits=100, decimal_places=2)
    file=models.FileField(upload_to='portfolio/dumps')

    def __str__(self):
        return self.name
