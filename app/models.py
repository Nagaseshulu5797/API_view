from django.db import models
# Create your models here.

class Product_category(models.Model):
    category_name=models.CharField(max_length=100)
    categoty_id=models.PositiveIntegerField()
    
class Product(models.Model):
    category_name=models.ForeignKey(Product_category,models.CASCADE)
    Pname=models.CharField(max_length=100)
    Pid=models.PositiveIntegerField()
    Price=models.DecimalField(max_digits=8,decimal_places=2)
    Pdate=models.DateField()
    
