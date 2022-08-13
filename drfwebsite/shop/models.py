from time import timezone
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField('Product name', max_length=255,)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,)
    description = models.CharField('Description', max_length=255)
    price = models.DecimalField('Price', max_digits=9, decimal_places=2,)
    # image = models.ImageField('Product image', upload_to='images/',  null=True, blank=False,)
    is_published = models.BooleanField(default=True,)
    published_time = models.DateField(default=timezone,)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
     
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,)

    def __str__(self):
        return self.name
    