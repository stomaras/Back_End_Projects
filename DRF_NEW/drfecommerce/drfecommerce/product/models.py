from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from .fields import OrderField
from django.core.exceptions import ValidationError
# Create your models here.

class ActiveQueryset(models.QuerySet):
    # def get_queryset(self):
    #     return super().get_queryset().filter(is_active=True)
    def isactive(self):
        return self.filter(is_active=True)

class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    
    class MPTTMeta:
        order_insertion_by = ['name']
        
    def __str__(self):
        return self.name
    
    

class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    id_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    
    objects = ActiveQueryset.as_manager()
    # isactive = ActiveManager()
    
    def __str__(self):
        return self.name
    
class ProductLine(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=100)
    stock_qty = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_line")
    is_active = models.BooleanField(default=False)
    order = OrderField(unique_for_field="product", blank=True)
    objects = ActiveQueryset.as_manager()
    
    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        qs = ProductLine.objects.filter(product=self.product)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("Duplicate Value")
    
    def __str__(self):
        return str(self.order)