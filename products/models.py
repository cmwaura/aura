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
        return reverse("single_product", kwargs={"slug":self.slug})
        #return "/products/%s/"%(self.slug)
