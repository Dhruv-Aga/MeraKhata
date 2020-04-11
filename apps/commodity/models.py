from django.db import models
from MeraKhata.settings.common import AUTH_USER_MODEL
from MeraKhata.constant import UNIT_TYPES


class Item(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, related_name='item_owner', null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    previous_code = models.CharField(max_length=100, blank=True, default="")
    short_name = models.CharField(max_length=100, blank=True, default="")
    bar_code = models.CharField(max_length=100, blank=True, default="")
    tax_code = models.CharField(max_length=100, blank=True, default="")
    unit = models.CharField(choices=UNIT_TYPES, default='KG', max_length=100, blank=True, null=True)
    maximum_retail_price = models.FloatField(blank=True, null=True)
    purchase_rate = models.FloatField(blank=True, null=True)
    selling_rate = models.FloatField(blank=True, null=True)
    min_quantity = models.FloatField(blank=True, null=True)
    tax_percentage = models.FloatField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    balance_quantity = models.FloatField(blank=True, null=True)
    balance_amount = models.FloatField(blank=True, null=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return "Item " + str(self.id) + ": " +  self.name 