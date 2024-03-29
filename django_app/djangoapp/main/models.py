from django.db import models
from django import forms

class Discounts(models.Model):
    title = models.CharField("Title", max_length=100)
    discount = models.CharField("Discount",max_length=20)
    price = models.CharField("Price", max_length=20)

    def __str__(self):
        return {self.title, self.discount, self.price}
    
    
    class Meta:
        db_table="new_table"