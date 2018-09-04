from django.db import models
import ast
from django.contrib.auth.models import User


class Ratings(models.Model):
	item_name = models.CharField(max_length=1000)
	item_rating = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now_add=True)
	rater = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Rating"

	def __str__(self):
		return self.item_name +' '+ self.item_rating

	def user_rated(self):
		return [self.item_name, self.item_rating]


class Product(models.Model):
	product_name = models.CharField(max_length=1000)
	product_seller = models.CharField(max_length=250)
	product_old_price = models.CharField(max_length=250)
	product_current_price = models.CharField(max_length=250)
	product_url = models.CharField(max_length=1500)
	product_categories = models.CharField(max_length=1500)
	product_valid_sizes = models.CharField(max_length=500)
	product_off = models.CharField(max_length=100)
	product_valid_images = models.CharField(max_length=1500)
	product_color = models.CharField(max_length=500, default=['Not Available in Colors'])
	product_description = models.TextField(default='No Description Available')
	product_sub_sub_categories = models.CharField(max_length=1500, default="")
	product_store_name = models.CharField(max_length=250, default="U")
	product_images_urls = models.CharField(max_length=1500, default="")
	product_old_colors = models.CharField(max_length=500, default="")
	product_old_sizes = models.CharField(max_length=500, default="")
	product_gender = models.CharField(max_length=250, default="")
	date = models.DateTimeField(auto_now_add=True)

	'''
	class Meta:
		verbose_name_plural = "products"
	'''

	def __str__(self):
		#return  'Product Name: '+ self.product_name + ' and seller is: ' + self.product_seller 
		return  self.product_name +'|'+ self.product_seller+'|'+ self.product_old_price+'|'+ self.product_current_price+'|'+ self.product_url+'|'+ self.product_categories+'|'+ self.product_valid_sizes +'|'+ self.product_off +'|'+ self.product_valid_images +'|'+ self.product_color

	def arr_products(self):
		return [self.product_name , self.product_seller , self.product_old_price , self.product_current_price , self.product_url , self.product_categories , self.product_valid_sizes , self.product_off , self.product_valid_images, self.product_color]

	def detect_changes(self):
		return [self.product_current_price, self.product_valid_sizes, self.product_color]

	def get_color(self):
		try:
			return [each for each in ast.literal_eval(self.product_color)]
		except ValueError:
			pass

	def images_as_list(self):
		try:
			return [each for each in ast.literal_eval(self.product_valid_images)]
		except ValueError:
			pass

	def sizes_as_list(self):
		try:
			return [each for each in ast.literal_eval(self.product_valid_sizes)]
		except ValueError:
			pass


	def category_as_list(self):
		try:
			return [each for each in ast.literal_eval(self.product_categories)]
		except ValueError:
			pass


	def old_price(self):
		if self.product_old_price == "No Old Price":
			return self.product_old_price
		return self.product_old_price


	def new_price(self):
		return self.product_current_price


class News(models.Model):
	product_name = models.CharField(max_length=1000)
	product_seller = models.CharField(max_length=250)
	product_old_price = models.CharField(max_length=250)
	product_current_price = models.CharField(max_length=250)
	product_url = models.CharField(max_length=1500)
	product_categories = models.CharField(max_length=1500)
	product_valid_sizes = models.CharField(max_length=500)
	product_off = models.CharField(max_length=100)
	product_valid_images = models.CharField(max_length=1500)
	product_price_change_type = models.CharField(max_length=100, default='Nil')
	product_color_change = models.CharField(max_length=100, default='No')
	product_size_change = models.CharField(max_length=100, default='No')
	product_news = models.TextField()
	product_color = models.CharField(max_length=500, default=["Not Available in Colors"])
	product_description = models.TextField(default='No Description Available')
	product_sub_sub_categories = models.CharField(max_length=1500, default="")
	product_store_name = models.CharField(max_length=250, default="")
	product_images_urls = models.CharField(max_length=1500, default="")
	product_old_colors = models.CharField(max_length=500, default="")
	product_old_sizes = models.CharField(max_length=500, default="")
	product_gender = models.CharField(max_length=250, default="U")
	date = models.DateTimeField(auto_now_add=True)

	
	class Meta:
		verbose_name_plural = "News"
	

	def __str__(self):
		return  'Product News is: '+ self.product_news

	def get_color(self):
		return [each for each in ast.literal_eval(self.product_color)]

	def images_as_list(self):
		return [each for each in ast.literal_eval(self.product_valid_images)]


	def sizes_as_list(self):
		return [each for each in ast.literal_eval(self.product_valid_sizes)]


	def category_as_list(self):
		return [each for each in ast.literal_eval(self.product_categories)]


	def percentage_off(self):

		if self.product_old_price == "No Old Price":
			return 0

		self.product_old_price	= self.product_old_price.replace(',', '')
		self.product_current_price	= self.product_current_price.replace(',', '')
		
		self.product_old_price = int(self.product_old_price)
		self.product_current_price = int(self.product_current_price)

		if self.product_old_price > self.product_current_price:
			#There is percentage Off
			off =   self.product_old_price - self.product_current_price
			calc = (off/self.product_old_price) * 100
			return int(calc)
		else:
			#There is an increase in price
			off =  self.product_current_price - self.product_old_price
			calc = (off/self.product_current_price) * 100
			return int(calc)

	def old_price(self):
		if self.product_old_price == "No Old Price":
			return self.product_old_price
		elif ',' not in str(self.product_old_price):
			return "{:,}".format(self.product_old_price)
		else:
			return self.product_old_price


	def new_price(self):
		if ',' in str(self.product_current_price):
			return self.product_current_price
		elif len(str(self.product_current_price)) > 3:
			return self.product_current_price
		return self.product_current_price
		#return "{:,}".format(self.product_current_price)


class Xpath(models.Model):
	website_name = models.CharField(max_length=250)
	major_url = models.CharField(max_length=1500)
	product_old_price = models.CharField(max_length=1500)
	relay_links = models.CharField(max_length=2500)
	start_page_number = models.CharField(max_length=1500)
	end_page_number = models.CharField(max_length=1500)
	pagination_index = models.CharField(max_length=150)
	product_name = models.CharField(max_length=1500)
	product_seller = models.CharField(max_length=1500)
	product_color = models.CharField(max_length=1500)
	product_current_price = models.CharField(max_length=1500)
	product_old_price = models.CharField(max_length=1500)
	product_categories = models.CharField(max_length=1500)
	product_sizes = models.CharField(max_length=1500)
	product_percentage_off = models.CharField(max_length=1500)
	product_images = models.CharField(max_length=1500)
	product_description = models.CharField(max_length=1500)
	product_url = models.CharField(max_length=1500)



class Unidentified(models.Model):
	product_name = models.CharField(max_length=1000)
	product_seller = models.CharField(max_length=250)
	product_old_price = models.CharField(max_length=250)
	product_current_price = models.CharField(max_length=250)
	product_url = models.CharField(max_length=1500)
	product_categories = models.CharField(max_length=1500)
	product_valid_sizes = models.CharField(max_length=500)
	product_off = models.CharField(max_length=100)
	product_valid_images = models.CharField(max_length=1500)
	product_color = models.CharField(max_length=500, default=['Not Available in Colors'])
	product_description = models.TextField(default='No Description Available')
	product_sub_sub_categories = models.CharField(max_length=1500, default="")
	product_store_name = models.CharField(max_length=250, default="U")
	product_images_urls = models.CharField(max_length=1500, default="")
	product_old_colors = models.CharField(max_length=500, default="")
	product_old_sizes = models.CharField(max_length=500, default="")
	product_gender = models.CharField(max_length=250, default="")
	date = models.DateTimeField(auto_now_add=True)

	'''
	class Meta:
		verbose_name_plural = "products"
	'''

	def __str__(self):
		#return  'Product Name: '+ self.product_name + ' and seller is: ' + self.product_seller 
		return  self.product_name +'|'+ self.product_seller+'|'+ self.product_old_price+'|'+ self.product_current_price+'|'+ self.product_url+'|'+ self.product_categories+'|'+ self.product_valid_sizes +'|'+ self.product_off +'|'+ self.product_valid_images +'|'+ self.product_color

	def arr_products(self):
		return [self.product_name , self.product_seller , self.product_old_price , self.product_current_price , self.product_url , self.product_categories , self.product_valid_sizes , self.product_off , self.product_valid_images, self.product_color]

	def detect_changes(self):
		return [self.product_current_price, self.product_valid_sizes, self.product_color]

	def get_color(self):
		try:
			return [each for each in ast.literal_eval(self.product_color)]
		except ValueError:
			pass

	def images_as_list(self):
		try:
			return [each for each in ast.literal_eval(self.product_valid_images)]
		except ValueError:
			pass

	def sizes_as_list(self):
		try:
			return [each for each in ast.literal_eval(self.product_valid_sizes)]
		except ValueError:
			pass


	def category_as_list(self):
		try:
			return [each for each in ast.literal_eval(self.product_categories)]
		except ValueError:
			pass


	def old_price(self):
		if self.product_old_price == "No Old Price":
			return self.product_old_price
		return self.product_old_price


	def new_price(self):
		return self.product_current_price
