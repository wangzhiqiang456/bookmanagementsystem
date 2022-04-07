from django.db import models

# Create your models here.

class Publisher(models.Model):   #一
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64,null=False)
    address = models.CharField(max_length=64,null=False)


class Book(models.Model):   #多
    bid = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5,decimal_places=2,default=10.01)
    inventery = models.IntegerField(verbose_name="库存数")
    sale_num = models.IntegerField(verbose_name="卖出数")
    publisher = models.ForeignKey('Publisher',on_delete=models.CASCADE)    #一对多
    
class Author(models.Model):  #多
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    book = models.ManyToManyField('Book')   #多对多

