"""
The get_all_major_category_links File Creates a Project Name with the Domain Name and its function is to get all the Major Categories of the Domain Name
"""

#Import Modules Needed
import os
from products.domain import *
from lxml import html
import requests
import datetime
import ast
import time


#Home Crawler Class to gather the Links of all Major Categories
#And Store in an Array 
class HomeCrawler(object):
	
	# Takes in the Home Page of the URL i.e home_page
	def __init__(self, home_page, major_url, relay_links):
		
		#The URL Home Page
		self.home_page = home_page.strip()

		self.major_url = major_url.strip()
		
		if relay_links.strip() == '':
			self.relay_links = ''
		else:
			self.relay_links = ast.literal_eval(relay_links)
			

		#Self.categories stores all the Major Categories
		self.categories = []

		#This Property self.project is Used to Create the Project Name
		ans = get_full_domain_name(self.home_page)
		
		if ans == "ng.fashpa.com":
			self.project = "ng.fashpa.com"
		else:
			self.project = get_domain_name(home_page)


		#Creating the project Name with the Current Day Time Stamp at Initialization if only Project Doesn't Exists
		if not os.path.exists('products/' + self.project+' - '+str(datetime.date.today())):
			print('Created New Project :',  self.project+' - '+str(datetime.date.today()))
			os.makedirs(os.path.join('products/' + self.project+' - '+str(datetime.date.today())))
		else:
			print('Sorry Website :',  self.project, 'Has Been Crawled Today')
			return




	#Returns All Categories in the Array Above as a String
	def __str__(self):
		return('All Categories are:', self.categories)

	#Calls the function to gather all categories specifically for Konga Home Page
	def crawl(self):
		links = self.get_all_categories(self.home_page)
		return links

	#Gathers all Major Categories Links / hrefs in Jumia homepage
	#Gathers all Major Categories Links / hrefs in Jumia homepage
	def get_all_categories(self, link):
			start_page = requests.get(link)
			# time.sleep(30)
			tree = html.fromstring(start_page.content, parser=html.HTMLParser(encoding="utf-8"))
			names = tree.xpath(self.major_url)
			# print("Major Categories are: ", names)
			for name in names:
				#Fix For DelphiMetals
				if ('http' not in name) and (self.project not in name):
					ans = get_full_domain_name(self.home_page)
					name = 'http://'+self.project+'/'+name

				#print('Slash Count For ', name, 'is', name.count('/'))
				#Fix for Bambiano to bypass home page
				
				#Fix for Fastforwardstores
				if name[-2] == '/':
					name = name[:-2]
				elif name[-1] == '/':
					name = name[:-1]
				#End Fastforward Fix
				if name.count('/') < 3:
					continue
				#End Fastforward Fix


				if 'blog' in name:
					continue

				if self.relay_links != '':
					for key, value in self.relay_links.items():
						if key.strip() == name:
							name = value.strip()
			
				self.categories.append(name)

'''
#This is only uncommented if you wish to view the Major Categories Only
crawler = HomeCrawler('https://www.konga.com/', '//span[@class="category-main"]/span[@class="category-main-title"]/a/@href', '')
crawler.crawl()
for category in crawler.categories:
	print(category)
'''