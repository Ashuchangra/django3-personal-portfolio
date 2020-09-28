from django.db import models

class Blog_project(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    description=models.CharField(max_length=300)

    def __str__(self):
        return self.title
