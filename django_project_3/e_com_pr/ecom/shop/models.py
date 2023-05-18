from django.db import models


# Create your models here.


class Product(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    pub_date = models.DateField()
    desc = models.CharField(max_length=1000, default='')
    image = models.ImageField(upload_to='media/images', default=" ")

    def __str__(self):
        return self.name


class Contact(models.Model):
    message_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=25)
    desc = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=5000)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc


