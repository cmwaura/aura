from django.contrib import admin

from .models import Products, ProductImage, Variation
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    '''
    This will be the admin configuration of each individual product that is entered.
    With this he will not only be able to search through the products but can edit
    features of the products from the admin product dashboard.
    '''

    date_hierarchy = 'timestamp'
    # adding the items to have a searchable characteristic
    search_fields = ['title', 'description']
    # fields in products/models.py
    list_display = ['title', 'price', 'active', 'updated']
    # give the admin the edit capabilities in the items
    list_editable = ['price', 'active']
    # Sorting out the list based on characteristics
    list_filter = ['price', 'title']

    # these are the readonly fields
    readonly_fields = ['updated', 'timestamp']

    # pre-populating the slug field based on the title
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Products

# register the  models and the admins
admin.site.register(Products, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Variation)