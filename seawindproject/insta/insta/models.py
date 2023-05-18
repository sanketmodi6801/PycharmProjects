from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Posts(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    link = models.CharField(max_length=10000, default=" ")
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
