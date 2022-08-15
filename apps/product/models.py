from django.contrib.auth.models import User
from django.db import models
from colorfield.fields import ColorField
from apps.blog.models import Tag


# Create your models here.


class Category(models.Model):
    FONT_TYPE = (
        (0, 'text'),
        (1, 'square'),
        (2, 'circle'),
        (3, 'tag'),
        (4, 'parent node'),
    )
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                        limit_choices_to={'font_type': 4})
    font_type = models.IntegerField(choices=FONT_TYPE, default=4)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    price = models.FloatField()
    tags = models.ManyToManyField(Category, limit_choices_to={'font_type': 3})
    mid_rate = models.FloatField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name

    @property
    def get_mid_rate(self):
        rates = self.product_rate.all()
        mid = 0
        try:
            mid = sum([i.rate for i in rates]) / rates.count()
        except ZeroDivisionError:
            pass
        self.mid_rate = round(mid)
        self.save()
        return round(mid)


class ProductColor(models.Model):
    color = ColorField(default='#000000')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_color')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return f'image of {self.product}'


class ProductSize(models.Model):
    size = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_size')

    def __str__(self):
        return self.size


class ProductRate(models.Model):
    RATE = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_rate')
    rate = models.IntegerField(choices=RATE, default=0)

    def __str__(self):
        return f'rate of {self.user.username}'
