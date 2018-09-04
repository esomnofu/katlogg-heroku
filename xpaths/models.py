from django.db import models
import ast
from django.contrib.auth.models import User


class XpathList(models.Model):
	website_name = models.CharField(max_length=1000)
	major_url = models.CharField(max_length=1000)
	relay_links = models.CharField(max_length=1000)
	start_page_number = models.CharField(max_length=1000)
	end_page_number = models.CharField(max_length=1000)
	pagination_index = models.CharField(max_length=1000)
	product_url = models.CharField(max_length=1000)
	product_name = models.CharField(max_length=1000)
	product_seller = models.CharField(max_length=1000)
	product_color = models.CharField(max_length=1000)
	product_current_price = models.CharField(max_length=1000)
	product_old_price = models.CharField(max_length=1000)
	product_categories = models.CharField(max_length=1000)
	product_sizes = models.CharField(max_length=1000)
	product_percentage_off = models.CharField(max_length=1000)
	product_images = models.CharField(max_length=1000)
	product_description = models.CharField(max_length=1000)
	product_filters = models.CharField(max_length=1500, default="")
	product_filters_texts = models.CharField(max_length=1500, default="")



	def __str__(self):
		return self.website_name