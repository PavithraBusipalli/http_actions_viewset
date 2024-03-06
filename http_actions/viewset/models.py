from django.db import models

from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    pc_id=models.IntegerField(primary_key=True)
    pc_name=models.CharField(max_length=100)

    def __str__(self):
        return self.pc_name

class Product(models.Model):
    pc_id=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    p_id=models.IntegerField()
    p_name=models.CharField(max_length=100)
    p_price=models.IntegerField()
    p_brand=models.CharField(max_length=100)
