from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=20)
    discription = models.CharField(max_length=100)
    date = models.DateField()


class Meta:
        db_table = "blog"