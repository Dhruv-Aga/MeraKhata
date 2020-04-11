from django.db import models
from django.contrib.postgres.fields import ArrayField
from MeraKhata.settings.common import AUTH_USER_MODEL
from MeraKhata.constant import SELLER_TYPE
from commodity.models import Item


class Seller(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100)
	firm_name = models.CharField(max_length=100)
	previous_code = models.CharField(max_length=100, blank=True, default="")
	short_name = models.CharField(max_length=20, blank=True, default="")
	description = models.TextField()
	seller_type = models.CharField(choices=SELLER_TYPE, default='Firm', max_length=5)
	tax_id = models.CharField(max_length=100, blank=True, default="")
	branch_address = models.CharField(max_length=100, blank=True, default="")
	branch_city = models.CharField(max_length=20, blank=True, default="")
	branch_country = models.CharField(max_length=20, blank=True, default="")
	branch_pincode = models.CharField(max_length=20, blank=True, default="")
	office_address = models.CharField(max_length=100, blank=True, default="")
	office_city = models.CharField(max_length=20, blank=True, default="")
	office_country = models.CharField(max_length=20, blank=True, default="")
	office_pincode = models.CharField(max_length=20, blank=True, default="")
	items = models.ManyToManyField(Item, blank=True)
	connections = models.ManyToManyField('self', blank=True)
	
	class Meta:
		ordering = ['created']

	def __str__(self):
		return "Seller " + str(self.id) + ": " +  self.name 
