'''
The get_all_item_links_by_sub_category uses the HomeCrawler Class
Gets the Major Categories
Create Folders by Name for All Major Categories inside the Main Project Folder i.e(jumia.com.ng)
Creates a txt File to Store All Products Links by Name for All Major Categories
Crawls All the Major Categories
Add All the Product Links in the Appropriate Text File
'''

#Import Modules Needed
import os
from lxml import html
import requests
from products.domain import *
#import datetime
#from products.get_all_major_category_links import HomeCrawler
#from products.detailed_view import DetailCrawler
#from products.general import *
#import time



#Each Category Crawler Class
class FilterCategoryCrawler(object):
	
	#Initialization Method

	#We pass in a last Argument(Xpath - filter) - if filter is available Detailed Crawler will be by filter.
	def __init__(self, starting_url, start_page_number, end_page_number, concatenation, product_url, product_filters, product_filters_texts):
		#Each Category URL Passed in
		self.starting_url = starting_url

		#A Set of Unique Items for All Links in Each Category
		self.items = set()
		self.fourth_layer_urls = set()
		self.fourth_layer_urls_texts = {}


		self.start_page_number = int(start_page_number)
		self.end_page_number = int(end_page_number)
		#self.pagination_index = pagination_index

		#Concatenation - I.E How to Navigate Through Each URL
		self.concatenation = concatenation

		self.product_url = product_url

		self.product_filters = product_filters

		self.product_filters_texts = product_filters_texts


		#A Counter to Help Iterate over All Pages in Each Category Initialize to 1
		self.page = 1

		#This is a Counter that Holds Current Page we are Crawling at Each Category Page we still just initialize to 1
		self.counter = ''


		ans = get_full_domain_name(self.starting_url)

		if ans == "ng.fashpa.com":
			self.project = "ng.fashpa.com"
		else:
			self.project = get_domain_name(starting_url)
		
	

	#To String Method Returns all items
	def __str__(self):
		return('All Items:', self.items)


	#The Crawl Function
	def crawl(self):

		#If no Pagination index is provided the program ignores to crawl all the webpages
		#And instead crawls only the specified page interval
		#It first of all gets the maximum pagination number
		#self.get_max_pagination_link(self.starting_url)
		if self.counter != '':
			#And Loops through it while there are still pages available
			while self.page <= self.counter:
				#Gets all URLS of each products per category
				self.get_item_from_link(self.starting_url)
		else:
			#This is when only some specified page intervals are to be crawled
			#we now set the page used in the url as the self.start_page_number
			#self.page = self.start_page_number
			while self.start_page_number <= self.end_page_number:
				self.get_item_from_selected_links(self.starting_url)

		return

	#Method to get maximum pagination number
	def get_max_pagination_link(self, link):
						
			start_page = requests.get(link)

			tree = html.fromstring(start_page.text)

			pagination = tree.xpath(self.pagination_index)
				
			self.counter = int(pagination[-1])

			

	#Method to Gather All URLs of each product in each category
	def get_item_from_link(self, link):
				
			start_page = requests.get(link + self.concatenation + str(self.page))		

			tree = html.fromstring(start_page.text)

			links = tree.xpath(self.product_url)
		
			for link in links:
				self.items.add(link)
			self.page += 1
			

	#Method to Gather All URLs of each product in each category
	def get_item_from_selected_links(self, link):

			start_page = requests.get( link + self.concatenation + str(self.start_page_number) )		
			tree = html.fromstring(start_page.text)

			#START OF SUB SUB CATEGORIES
			#START OF SUB SUB CATEGORIES
			#START OF SUB SUB CATEGORIES
			#Get Filters Links (URL) if available
			filters = ""
			each_filters_texts = ""

			window_list = []

			if ',' in self.product_filters:
				for link in self.product_filters.split(','):
				
					current_filters = tree.xpath(link)
					# print('current_filters URLS:  ', current_filters)
					if current_filters != []:
						filters = current_filters
						break

				#Fix for BestBuyforless
				#Fix for BestBuyforless
				#Fix for BestBuyforless
				if self.project == "bestbuyforless.com.ng":	
					for each in filters:
						if "false" in each:
							each = each.split("=")
							neededEach = each[1]
							neededEach = neededEach[1:]
							neededEach = neededEach[:-16]
							window_list.append(neededEach)
					filters = window_list

				# print("Filters URLs are: ", filters)

			else:
				filters = tree.xpath(self.product_filters)
				#Fix for BestBuyforless
				#Fix for BestBuyforless
				#Fix for BestBuyforless
				if self.project == "bestbuyforless.com.ng":		
					for each in filters:
						if "false" in each:
							each = each.split("=")
							neededEach = each[1]
							neededEach = neededEach[1:]
							neededEach = neededEach[:-16]
							window_list.append(neededEach)
					filters = window_list
					
				# print("Filters URLs are: ", filters)

	

			temp_trim_list = []
			#Get the corresponding Texts
			if ',' in self.product_filters_texts:
				for link in self.product_filters_texts.split(','):

					current_filters = tree.xpath(link)
					# print('current_filters TExts : ', current_filters)
					if current_filters != []:
						each_filters_texts = current_filters
						break
				#Fix for BestBuyforless
				#Fix for BestBuyforless
				#Fix for BestBuyforless
				for each in each_filters_texts:
					each_trimmed = each.strip()
					if each_trimmed != "":
						temp_trim_list.append(each_trimmed)

				each_filters_texts = temp_trim_list
				# print("Each Filters TExts are: ", each_filters_texts)

			else:
				each_filters_texts = tree.xpath(self.product_filters_texts)
				#Fix for BestBuyforless
				#Fix for BestBuyforless
				#Fix for BestBuyforless
				for each in each_filters_texts:
					each_trimmed = each.strip()
					if each_trimmed != "":
						temp_trim_list.append(each_trimmed)

				each_filters_texts = temp_trim_list
				# print("Each Filters TExts are: ", each_filters_texts)


			# print("Count of Filters URLS is: --- ", len(filters),  "Where as count of Filters Texts is --- ", len(each_filters_texts))

			#Fix for Konga
			#Fix for Konga
			#Fix for Konga
			urls_len = len(filters)
			texts_len = len(each_filters_texts)
			removal_url = urls_len - texts_len
			removal_texts = texts_len - urls_len

			#If either of the links or urls is more than their opposite nos
			#We remove the excess numbers from the beginning of the Array
			#As was discovered by physical verification on Sites "Konga" source code
			if( removal_url > 0):
				filters = filters[removal_url:]
			elif( removal_texts > 0 ):
				each_filters_texts = each_filters_texts[removal_texts:]
			

			#Make it a key value pair in a Dictionary
			start = 0
			while start < len(filters):
				self.fourth_layer_urls_texts[filters[start]] = each_filters_texts[start]
				start += 1

			for eachFilter in filters:
				if ('http' not in eachFilter) and (self.project not in eachFilter):
					eachFilter = 'http://'+self.project+'/'+eachFilter
				self.fourth_layer_urls.add(eachFilter)

			#End OF SUB SUB CATEGORIES
			#End OF SUB SUB CATEGORIES
			#End OF SUB SUB CATEGORIES

		

			links = tree.xpath(self.product_url)
			for link in links:
				#Fix For DelphiMetals
				if ('http' not in link) and (self.project not in link):
					link = 'http://'+self.project+'/'+link
				self.items.add(link)
			self.start_page_number += 1



"""
================================================================================================================================================================================================
================================================================================================================================================================================================
================================================================================================================================================================================================
OUTSIDE THE CLASS
OUTSIDE THE CLASS
OUTSIDE THE CLASS
================================================================================================================================================================================================
================================================================================================================================================================================================
================================================================================================================================================================================================
"""


	

