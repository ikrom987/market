from distutils.command.upload import upload
from email.mime import image
from tkinter import CASCADE
from turtle import title
from unicodedata import category
from django.db import models
from django_resized import ResizedImageField
from slugify import slugify
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True, blank=True)
    priority = models.IntegerField()

    def __str__(self):
        return  self.title

    def total_products(self):
        return Product.objects.filter(category=self).count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title).lower()
        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ("priority",)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField()
    image_min = ResizedImageField(size=[250, 250], quality=100, upload_to="products/")
    image_max = ResizedImageField(size=[600, 600], quality=100, upload_to="products/")
    priority = models.IntegerField()
    drop = models.BooleanField(default=False)

    def __str__(self):
        return  self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title).lower()
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ("priority",)


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(blank=True, null=True)
    address = models.TextField()

    def __str__(self):
        return self.user.username


class Order(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    transaction = models.CharField(max_length=255, null=True, blank=True)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_complete = models.DateTimeField(auto_now=True)
    proccessed = models.BooleanField(default=False)

    def get_total_order_item_count(self):
        c = 0
        for i in OrderItem.objects.filter(order=self):
            c += i.quantity
        return c 

    def get_total_order_item_sum(self):
        c = 0
        for i in OrderItem.objects.filter(order=self):
            c += i.get_total()
        return c 

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def get_total(self):
        return self.product.price * self.quantity

class Slider(models.Model): 
    title = models.CharField(max_length=255) 
    img = models.ImageField() 
    date_create = models.DateTimeField(auto_now_add=True)