from django.db import models
from django.urls import reverse

# Create your models here.
class UserManage(models.Model):
    username =models.CharField(max_length=32, null=True, blank=True)
    password =models.CharField(max_length=32, null=True, blank=True)
    conformpassword =models.CharField(max_length=100, null=True, blank=True)
    
  
    class Meta:
        db_table='usermanage'
        
class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)
    
    class Meta:
        ordering=("name",)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('ShoppingApp:product_by_category', args=[self.slug])
        
    def __str__(self):
        return '{}'.format(self.name)
    
class Product(models.Model):
    name=models.CharField(max_length=250,unique=250)
    slug=models.SlugField(max_length=250,unique=250)
    description=models.TextField(max_length=250)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product',blank=True)
    stock=models.IntegerField()
    available=models.BooleanField()
    createdby=models.DateTimeField(auto_now=True)
    updatedby=models.DateField(auto_now=True)

    def get_url(self):
        return reverse('ShoppingApp:prodCatedetail', args=[self.category.slug,self.slug])
    
    class Meta:
        ordering=("name",)
        verbose_name='product'
        verbose_name_plural='products'
        
    def __str__(self):
        return '{}'.format(self.name)