"""
DETAILED VIEW --- TO GET ALL RELEVANT INFORMATION FOR EACH PRODUCT ON THE DETAILED PAGE
THE CLASS TAKES THE FULL URL PATH TO THE DETAIL PAGE
ACCESSES ALL RELAVANT INFO AND MAKES AN INSTANCE OF THEM AND STORES AS OBJECTS IN A SET
"""
from lxml import html
import requests
import datetime
from products.general import *
from products.domain import *
from collections import Counter
from products.determine_category import *
import ast


class DetailCrawler(object):

	def __init__(self, starting_url, product_name, product_color, product_seller, product_current_price, product_old_price, product_categories, product_sizes, product_percentage_off, product_images, product_description, product_sub_sub_categories):

		self.starting_url = starting_url
		
		self.product_name = product_name

		self.product_color = product_color

		self.product_description = product_description
		
		if product_seller.strip() == "":
			self.product_seller = get_domain_name(starting_url)
		else:
			self.product_seller = product_seller
		
		self.product_current_price = product_current_price
		self.product_old_price = product_old_price
		self.product_categories = product_categories
		self.product_sizes = product_sizes
		self.product_percentage_off = product_percentage_off
		self.product_images = product_images
		self.product_sub_sub_categories = product_sub_sub_categories
		self.items = []

		self.colors =  ["AliceBlue","AntiqueWhite","Aqua","Aquamarine","Azure","Beige","Bisque","Black","BlanchedAlmond","Blue","BlueViolet","Brown","BurlyWood","CadetBlue","Chartreuse","Chocolate","Coral","CornflowerBlue","Cornsilk","Crimson","Cyan","DarkBlue","DarkCyan","DarkGoldenRod","DarkGray","DarkGrey","DarkGreen","DarkKhaki","DarkMagenta","DarkOliveGreen","Darkorange","DarkOrchid","DarkRed","DarkSalmon","DarkSeaGreen","DarkSlateBlue","DarkSlateGray","DarkSlateGrey","DarkTurquoise","DarkViolet","DeepPink","DeepSkyBlue","DimGray","DimGrey","DodgerBlue","FireBrick","FloralWhite","ForestGreen","Fuchsia","Gainsboro","GhostWhite","Gold","GoldenRod","Gray","Grey","Green","GreenYellow","HoneyDew","HotPink","IndianRed","Indigo","Ivory","Khaki","Lavender","LavenderBlush","LawnGreen","LemonChiffon","LightBlue","LightCoral","LightCyan","LightGoldenRodYellow","LightGray","LightGrey","LightGreen","LightPink","LightSalmon","LightSeaGreen","LightSkyBlue","LightSlateGray","LightSlateGrey","LightSteelBlue","LightYellow","Lime","LimeGreen","Linen","Magenta","Maroon","MediumAquaMarine","MediumBlue","MediumOrchid","MediumPurple","MediumSeaGreen","MediumSlateBlue","MediumSpringGreen","MediumTurquoise","MediumVioletRed","MidnightBlue","MintCream","MistyRose","Moccasin","NavajoWhite","Navy","OldLace","Olive","OliveDrab","Orange","OrangeRed","Orchid","PaleGoldenRod","PaleGreen","PaleTurquoise","PaleVioletRed","PapayaWhip","PeachPuff","Peru","Pink","Plum","PowderBlue","Purple","Red","RosyBrown","RoyalBlue","SaddleBrown","Salmon","SandyBrown","SeaGreen","SeaShell","Sienna","Silver","SkyBlue","SlateBlue","SlateGray","SlateGrey","Snow","SpringGreen","SteelBlue","Tan","Teal","Thistle","Tomato","Turquoise","Violet","Wheat","White","WhiteSmoke","Yellow","YellowGreen"]

		#Katlogg Sub Categories
		self.kids_fashion = {"['Dresses', 'Denim, Trouser and Leggins', 'Watches / Jewellery', 'Underwear and Socks', 'Shoes', 'Polos and Tshirts', 'Sleepwear', 'Bodysuits and Playsuits', 'Shirts', 'Miscellaneous']" : ["Kids", "Girls", "Baby", "Children", "Fashion for Girls", "Baby, Kids & Toys", "PENDANTS", "CROSS PENDANT", "NECKLACES", "BRACELETS / BANGLES", "Boys", "Kids Fashion", "Fashion for boys" ]}

		self.pet_supplies = { "['Pet Care Products','Pet Toys and Accessories','Pet foods','Miscellaneous']" : ['Pet Supplies', 'Pet supplies'] }

		self.women_fashion = { '["Dresses","Kimonos","Jumpers and Cardigans","Jumpsuits and Playsuits","Hoodies and Sweatshirts","Lingerie and Nightwear","Shorts","Skirts","Coats and Jackets","Socks and Tights","Suits","Swimwear and Beachwear","Tops","Trousers and Leggins","Miscellaneous"]' : ["Women's Fashion",'Women', 'Youth','Equipment', 'Sales','Ankara Styles', 'Multi-Pack','Singlets','Traditional',
		'Trousers, Shorts & Leggings', "Women's Trousers", "Women's Tops", "Women's clothing", "Women's Skirts", "Women's Plus Size", "Women's Dresses", "Women's wear", "Traditional Clothing & Accessories", "Suits & Blazers","Women's Ready to Wear", 'Beach & Swimwear',"Women's T-Shirts", 'Plus Sizes',
		'Jumpsuits and Playsuits', 'Islamic Wear','Jumpers & Cardigans', 'Socks & Tights','Skirts', 'Trousers & Leggings','Babydolls', 'Sunglasses','Dresses', 'Swimwear & Beachwear','BUTT PADS', 'Shoes','Shorts', 'Jeans',
		 'Coats & Jackets','Suits & Blazers', 'Lingerie & Nightwear','Polo Shirts', 'Denim','Kimonos', 'Lingerie and Sleepwear','Apparel', 'Underwear & Sleepwear','Hoodies & Sweatshirts','Clothing','Corporate Wear','Tops','Jeans & Jeggings']}

		self.sub_sub_categories = [self.kids_fashion, self.pet_supplies, self.women_fashion]


		#Convert all values in list to lower case to completely match
		lowercase_list = []
		for each_sub in self.sub_sub_categories:
			for key, value in each_sub.items():
				for item in value:
					item = item.lower().strip()
					item.replace("'","")
					lowercase_list.append(item)

			each_sub[key] = lowercase_list
			lowercase_list = []
		
	def __str__(self):
		return('All Items:', self.items)


	def product_detail(self):
		each_item = self.get_item_from_link(self.starting_url)
		if each_item["current_price"] is None:
			#print("Not Added")
			return
		else:
			self.items.append(each_item)
			return


	def find_needle(self, needle, haystack):
		counted = Counter(haystack.split())[needle]
		return counted



	def get_item_from_link(self, link):
			
			start_page = requests.get(link)
			tree = html.fromstring(start_page.text)

			url = link
			#IF more than one xpath was supplied
			if ',' in self.product_name:
				for link in self.product_name.split(','):
					current_name = tree.xpath(link)
					if current_name != []:
						break
				#print("Initial Current Price", current_prices)
				name = list_to_string(current_name)
				try:
					name_in_title_case = name.title()
				except:
					name_in_title_case=[]

			else:
				names = tree.xpath(self.product_name)
				name = list_to_string(names)
				try:
					name_in_title_case = name.title()
				except:
					name_in_title_case=[]




			if self.product_color == '':
				color = []
				colors = name_in_title_case
				for each in self.colors:
					if each in colors:
						color.append(each)
				if len(color) == 0:
					color = ["Not Available in Colors"]
				#print('Colors is', color)
			else:
				colors = tree.xpath(self.product_color)
				color = filter_list_colors(colors)


			if '.' in self.product_seller:
				seller = self.product_seller
			
			elif ',' in self.product_seller:
				for link in self.product_seller.split(','):
					sellers = tree.xpath(link)
					if sellers != []:
						break
				seller = seller_availability(sellers)
			else:
				sellers = tree.xpath(self.product_seller)
				seller = seller_availability(sellers)

		
			if ',' in self.product_current_price:
				for link in self.product_current_price.split(','):
					current_prices = tree.xpath(link)
					if current_prices != []:
						break
				current_price = current_price_availability(current_prices)
			else:
				current_prices  = tree.xpath(self.product_current_price)
				current_price = current_price_availability(current_prices)

			#Fix for Bestbuysforless.com.ng
			if ',' in self.product_old_price:
				old_price_check = self.product_old_price.split(',')
				old_check = tree.xpath(old_price_check[1])
				if old_check == []:
					old_price = old_price_availability(old_check)
				else:
					old_prices = tree.xpath(old_price_check[0])
					old_price = old_price_availability(old_prices)
			else:
				old_prices  = tree.xpath(self.product_old_price)
				old_price = old_price_availability(old_prices)
			
			
			categories = tree.xpath(self.product_categories)
			categories = list_items_to_categories(categories)
			

			sizes  = tree.xpath(self.product_sizes)
			valid_sizes = sizes_availability(sizes)
			if "Not Available in Sizes" not in valid_sizes:
				valid_sizes = list_items_to_string(valid_sizes)
			
			percentage_off = tree.xpath(self.product_percentage_off)
			off = off_availability(percentage_off)

			
			#Fix For Buyless.com.ng
			if ',' in self.product_images:
				for link in self.product_images.split(','):
					current_images = tree.xpath(link)
					#print('Current Images', current_images)
					if current_images != []:
						break
				#Fix for Dreamcare.com.ng
				self.project = get_domain_name(self.starting_url)
				for index, image in enumerate(current_images):
					if ('http' not in image) and (self.project not in image):
						new_image = 'http://'+self.project+'/'+image
						current_images[index] = new_image
				valid_images = get_valid_images(current_images)
			else:
				#print('Images Xpath', self.product_images)	
				images = tree.xpath(self.product_images)
				#print("Initial valid_images is", images)

				#Fix for Dreamcare.com.ng
				self.project = get_domain_name(self.starting_url)
				for index, image in enumerate(images):
					if ('http' not in image) and (self.project not in image):
						new_image = 'http://'+self.project+'/'+image
						images[index] = new_image
				#print("Initial 2 valid_images is", images)
				valid_images = get_valid_images(images)
				#print("valid_images is", valid_images)

			

			#Fix For Dreamcare.com.ng
			if ',' in self.product_description:
				for link in self.product_description.split(','):
					current_description = tree.xpath(link)
					#print('Current description', current_description)
					if current_description != []:
						break
				valid_description = description_availability(current_description)
			
			else:
				description = tree.xpath(self.product_description)
				#print('Initial Description', description)
				valid_description = description_availability(description)



			#Work on Categories
			#Work on valid_description

			maleCount = 0
			femaleCount = 0
			productGender = ""

			categories = categories.lower()
			haystacks = ""

			for each_category in categories.split(','):
				haystacks += " " + each_category

			maleNeedles = ["man", "male", "males", "male's", "boy", "men", "boys", "guy", "guys", "men's", "boy's", "guy's", "gentlemen", "gent", "gents", "gent's"]
			femaleNeedles = ["woman", "women", "women's", "girl", "girls", "ladies", "lady", "girl's", "female", "females"]
	

			for each in maleNeedles:
				maleCount += self.find_needle(each, haystacks)



			for each in femaleNeedles:
				femaleCount += self.find_needle(each, haystacks)


			if( (maleCount > 0) and (femaleCount == 0) ):
				#Its a Male Product tag it as Male for Gender
				productGender = "M"
				#Instantiate MaleCount back to zero
				maleCount = 0

			elif((maleCount == 0) and (femaleCount > 0)):
				#its a Female Product we tag it as Female for Gender
				productGender = "F"
				#Instantiate Female Count back to Zero
				femaleCount = 0

			else:
				productGender = "U"
				maleCount = 0
				femaleCount = 0

			#We check if this call came from the Filter class or this site has no filters... we assign directly and N/A for now
			if( (self.product_sub_sub_categories == "") or (self.product_sub_sub_categories is None)):
				#self.product_sub_sub_categories = "Not Assigned"
				if categories[-1:] is ",":
					categories = categories[:-1]
				each_category = categories.split(",")
				#We assign this filter gotten from the category
				if len(each_category) < 3:
					self.product_sub_sub_categories = each_category[-1]
				else:
					self.product_sub_sub_categories = each_category[-2]
			


			#Here we have to decide which Sub category Haystack we are passing to Determine Function
			#or alternatively which one we selecting based on d filter text gotten
			haystack = ""
			for sub_cat in self.sub_sub_categories:
				for key, value in sub_cat.items():
					comparingVar = self.product_sub_sub_categories.lower().strip()
					comparingVar.replace("'","")
					if comparingVar in value:
						haystack = key
						break


			#If the filter doesn't match any of our sub sub filtered items we automatically assign Miscallaneous
			if((haystack == "") or (haystack is None) ):
				result = "Miscellaneous" + " | " + self.product_sub_sub_categories

			else:
				haystack = ast.literal_eval(haystack)
				selectedName = DetermineCategory(name, haystack)
				#selectedName = DetermineCategory(self.product_sub_sub_categories, haystack)
				result = selectedName.assignCategory()
				result = result + " | " + self.product_sub_sub_categories


			each_item = {'name':name, 'seller':seller, 'current_price':current_price, 'old_price':old_price, 'url':url, 'categories':categories, 'valid_sizes':valid_sizes, 'off':off, 'valid_images':valid_images[0], 'images_url':valid_images[1], 'store_name':get_store_name(self.starting_url), 'gender':productGender, 'sub_sub': result, 'color':color, 'description':valid_description}
			return each_item

'''
otedola = DetailCrawler('https://www.konga.com/crux-mens-flannel-red-lumberjack-shirt-3953065', "//div[@class='product-name']/text()", "", "//div[@class='col-lg-9 col-md-9 col-sm-9 nopadding']/div[@class='merchant-header']/a[@class='merchant-name']/text()", "//div[@class='purchase-actions']/span[@class='price']/text()", "//div[@class='purchase-actions']/span[@class='previous-price']/text()", '//div[@class="breadcrumbs"]/ul/li/a/text()',  "//div[@class='i_do_not_exists']", "//div[@class='i_do_not_exists']", '//div[@class="carousel-inner"]/div/img/@src', "//div[@class='product-long-description-brief']/p/text()")
otedola.product_detail()
for item in otedola.items:
	print(item)

'''
