from django.db import models

from account.models import CustomerUser


class Category(models.Model):

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    quantity = models.IntegerField(default=0)

    def imageURL(self):
        if self.image:
            return self.image.url
        return ''

    def __str__(self):
        return self.name

class Comment(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment_product')
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name='comment_user')
    subject = models.CharField(max_length=55, blank=True)
    comment = models.TextField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class RatingStar(models.Model):

    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.value

class Rating(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, related_name='stars')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating_product')

    def __str__(self):
        return f'{self.star} - {self.product}'
