from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Products(models.Model):

    '''
    these will be the models that will include all the products that will be used by the site.
    It will borrow from the class of Django Models and in the end it will return the title of
    product as a __unicode__ method. In addition to this a few things need to be included.
    1. presence of a Slug field which will be a unique field that will be synchronized with the
        title. This is what will identify a product for instance at the URL
    2.
    '''

    title = models.CharField(max_length=140, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(max_digits=100, default=29.99, decimal_places=2)
    sale_price = models.DecimalField(max_digits=100, null=True, blank=True, decimal_places=2)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):

        '''

        :return: it will return the title of the product  on the admin page.
        '''
        return self.title

    class Meta:
        unique_together = ("title", "slug")

    def get_price(self):
        return self.price

    def get_absolute_url(self):
        return reverse("single_product", kwargs={"slug": self.slug})



class ProductImage(models.Model):
    product = models.ForeignKey(Products)
    image = models.ImageField(upload_to='products/images/')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.product.title


class VariationManager(models.Manager):

    def sizes(self):

         return self.all().filter(category="size")

    def gender(self):

         return self.all().filter(category="gender")

    def color(self):

         return self.all().filter(category="color")

    def package(self):

         return self.all().filter(category="package")


VAR_CATEGORIES = (
        ("size", "size"),
        ("gender", "Gender"),
        ("color", "color"),
        ("package", "package"),
)


class Variation(models.Model):
    # linking up the product variation to the product itself

    product= models.ForeignKey(Products)

    # all the categories expressed within the tuple VAR_CATEGORIES now placed in the model
    category= models.CharField(max_length=120, choices=VAR_CATEGORIES, default="color")

    # linking up the product variation to the product image.
    image= models.ForeignKey(ProductImage, null=True, blank=True)

    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    #setting up the variations manager so that the variations can work
    objects = VariationManager()


    def __unicode__(self):
       return self.title