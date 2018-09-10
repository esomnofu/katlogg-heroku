
#Dango Modules
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
import json
import os
# from django.conf import settings
export DJANGO_SETTINGS_MODULE=catalogue.settings

#Paginator Module
from django.core.paginator import Paginator, EmptyPage, InvalidPage

#Modules For Crawler
from lxml import html
import requests
import datetime
from products.get_all_major_category_links import HomeCrawler
from products.get_all_item_links_by_sub_category import CategoryCrawler
from products.filter_category_crawler import FilterCategoryCrawler
from products.detailed_view import DetailCrawler
from products.general import *
from products.domain import *
from products.detect_changes import *
import time
import ast


#Module for Neural Network
from products.searchengine import *
#from products.nn import *



#Import Models Here

from products.models import *
from xpaths.models import *

#Get Object or 404
from django.shortcuts import get_object_or_404

from django.views.decorators.csrf import csrf_exempt

from random import randint




#ITEM BASED MODULES IMPORT
#ITEM BASED MODULES IMPORT
#ITEM BASED MODULES IMPORT
from .forms import MyUserRegisterForm, AddRating
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


#Modules for Recommendations Below
from django.contrib.auth.models import User
from .recommendations import *
from django.forms.models import model_to_dict


from products.layer_deep_filters import check_fourth_or_fifth_layer


#IMPORTS FOR API CALLS
#IMPORTS FOR API CALLS
#IMPORTS FOR API CALLS
#iMPORT GET_OBJECT_OR_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#Import Your Model
from .serializers import ProductSerializer


#Import Required From New Tutorial still on API CALLS
#Import Required From New Tutorial still on API CALLS
#Import Required From New Tutorial still on API CALLS
from rest_framework import viewsets


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



def crawl_worker(website_name, major_url, relay_links, start_page_number, end_page_number, concatenation_pattern, product_url, product_name, product_seller, product_color, product_current_price, product_old_price, product_categories, product_sizes, product_percentage_off, product_images, product_description, product_filters, product_filters_texts):

	print("request gotten from master: ", request)
	if website_name != '':
		
		#Instantiate an Object of the Neural Class that will index all URLs and associated texts in its page

		#Calling the HomeCrawler Class from the Index Module to get all Major Categories
		crawler = HomeCrawler(website_name, major_url, relay_links)
		crawler.crawl()


		data = {}  
		data['product'] = []  

		faker = {}  
		faker['product'] = []  

		#Looping Through All the Major Categories Found
		for category in crawler.categories:

			#Fix For BAMBIANO
			if category[-1:] is '/':
				category = category[:-1]

			cat_num = category.split('/')
			#print('Category List', cat_num)

			category_name = cat_num[-1]

			#Replace Question marks with nothing as it impedes folder/file creation
			category_name = category_name.replace('?', '')


			#Before we assume this category already exists lets check if it was completely crawled
			#Before we assume this category already exists lets check if it was completely crawled
			#Before we assume this category already exists lets check if it was completely crawled
			#Before we assume this category already exists lets check if it was completely crawled
			#Before we assume this category already exists lets check if it was completely crawled
			
			if os.path.exists( os.path.join('products/' +crawler.project+' - '+str(datetime.date.today())+'/'+category_name) ):
				path = 'products/' +crawler.project+' - '+str(datetime.date.today())+'/'+category_name
				text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
				print("Nos of txt files are: ", len(text_files))

				nosOfFiles = len(text_files)
				last = text_files[-1]
				print("Last File is: ", last)

				if nosOfFiles == 1 :
					os.remove(path+'/'+last)
					os.rmdir(path)
					print("We removed file and directory...", path+"/"+last)



			#Creating A Folder for every Category Under the Project Name which already bears the Timestamp of the Day
			if not os.path.exists( os.path.join('products/' +crawler.project+' - '+str(datetime.date.today())+'/'+category_name) ):
			


				#Creating a Folder For Each Category
				os.makedirs(os.path.join('products/' +crawler.project+' - '+str(datetime.date.today())+'/'+category_name) )


				print("Created Category: ", 'products/' +crawler.project+' - '+str(datetime.date.today())+'/'+category_name)

		#Creating a File for All Links Found in a Category		
				urls = os.path.join('products/' + crawler.project+' - '+str(datetime.date.today())+'/'+category_name +'/'+category_name+'.txt')
				

				#Argument One to Feed The News Function in General.py
				arg = os.path.join(BASE_DIR +'/products/'+ crawler.project+' - '+str(datetime.date.today())+'/'+category_name+'/')
				# print("arg Argument 1 is: ", arg)
				
				# arg = os.path.join('/Users/DIAMONDSCRIPTS/Desktop/katlogg/products/' + crawler.project+' - '+str(datetime.date.today())+'/'+category_name+'/')
				
				#Argument Two to Feed The News Function in General.py
				argz = os.path.join('/' + crawler.project+' - '+str(datetime.date.today())+'/'+category_name+'/')
				# print("argz Argzument 2 is: ", argz)

				if not os.path.isfile(urls):
					write_file(urls, '')


					#Crawl Each Category Gotten From HomeCrawler With CategoryCrawler
					if crawler.project == "delphimetals.com":
						category = category + "?view=list"
					crawl_each_category = CategoryCrawler(category, start_page_number, end_page_number, concatenation_pattern, product_url, product_filters, product_filters_texts)
					crawl_each_category.crawl()


					if(len(crawl_each_category.filters) > 0):
						
						fourth_layer_filters = ["Pet Supplies", "Pet Care Products", "Pet Toys and Accessories", "Pet Accessories", "Pet Food & Supplement", "Other operating systems", "All Brands", "Books, Movies & Music", "Stationery", "Art Craft and Sewing", "Temptations", "Exotic clothing , Adult Toys", "Plumbing Materials", "Building & Construction", "Home repairs", "Weddings", "Souvenirs"]
						already_picked_from_fourth_layer_filters = []
						for filter_url in crawl_each_category.filters:

						
							each_filter_category = FilterCategoryCrawler(filter_url, start_page_number, end_page_number, concatenation_pattern, product_url, product_filters, product_filters_texts)
							each_filter_category.crawl()
							set_to_file(each_filter_category.items, urls)							
							matrix = NeuralCrawler('searchindex.db')

							#{'kids-bath': "Kids' Bath", 'kids-furniture': "Kids' Furniture", 'kids-room-decor': "Kids' Room Decor"}
							# {'http://konga.com/kids-furniture', 'http://konga.com/kids-bath', 'http://konga.com/kids-room-decor'}

							#print("Additional Fourth Layer url texts are: ", each_filter_category.fourth_layer_urls_texts)
							#print("Additional Fourth Layer urls are: ", each_filter_category.fourth_layer_urls)

							#So we can do a check and see if any of them is in our fourth_layer_filters - then if there is a match
							#We can find a way to add that url among the ones we are crawling
							
							#This Crawls the Fourth Layer and Returns Parameters needed for the Fifth
							response_for_fifth = check_fourth_or_fifth_layer(each_filter_category.fourth_layer_urls_texts, each_filter_category.fourth_layer_urls, fourth_layer_filters, already_picked_from_fourth_layer_filters, urls, start_page_number, end_page_number, concatenation_pattern, product_url, product_filters, product_filters_texts, product_name, product_color, product_seller, product_current_price, product_old_price, product_categories, product_sizes, product_percentage_off, product_images, product_description, data, faker, arg, argz, crawler.project, category_name)
							
							print("RESPONSE FOR FIFTH :- ", response_for_fifth)
							if(response_for_fifth != None):


								#Numerous Fifth Layers Are Supplied - We Iterate all Crawl those we need ---- We Crawl Fifth Layer and Thats All...
								for each_new in response_for_fifth:
									for fifth_layer_urls , fifth_layer_texts in each_new.items():
										#Key was converted to string we unconvert back to set
										#Value wasn't we pass like that
										fifth_layer_urls_set = ast.literal_eval(fifth_layer_urls)
										response_for_sixth = check_fourth_or_fifth_layer(fifth_layer_texts, fifth_layer_urls_set, fourth_layer_filters, already_picked_from_fourth_layer_filters, urls, start_page_number, end_page_number, concatenation_pattern, product_url, product_filters, product_filters_texts, product_name, product_color, product_seller, product_current_price, product_old_price, product_categories, product_sizes, product_percentage_off, product_images, product_description, data, faker, arg, argz, crawler.project, category_name)
							
							#Move on with the Rest of the Code

							for item in each_filter_category.items:
							# for item in list(each_filter_category.items)[:10]:
							# for item in list(each_filter_category.items)[:5]:
								#Let Us Index and Add Each Info From All Products Category to our Neural Network Databases Before Getting their Full Info With our DetailCrawler
								#Let Us Index and Add Each Info From All Products Category to our Neural Network Databases Before Getting their Full Info With our DetailCrawler
								#Let Us Index and Add Each Info From All Products Category to our Neural Network Databases Before Getting their Full Info With our DetailCrawler
								

								#matrix.crawl(item)
								


								#End of Neural Functionality
								#End of Neural Functionality
								#End of Neural Functionality

								#Possibly Fix for Jumia and Ajebo
								if ( website_name == "https://www.konga.com/"):
									actual_filter_names = filter_url.split('/')
									product_sub_sub_categories = actual_filter_names[-1]
								else:
									if crawler.project == "delphimetals.com":
										product_sub_sub_categories = filter_url[24:]
									else:
										product_sub_sub_categories = filter_url
							
								sub_sub = crawl_each_category.filters_texts[product_sub_sub_categories]
								product_info = DetailCrawler(item, product_name, product_color, product_seller, product_current_price, product_old_price, product_categories, product_sizes, product_percentage_off, product_images, product_description, sub_sub)
								product_info.product_detail()


								for items in product_info.items:
									data['product'].append(items)
									faker['product'].append(items)
									#time.sleep(5)

							the_url = os.path.join('products/' + crawler.project+' - '+str(datetime.date.today())+'/'+category_name +'/'+category_name+'_products_'+category_name+'_'+str(datetime.date.today())+'.txt')
							if not os.path.isfile(the_url):
								print('Created Dictionary Object Information File :',  crawler.project+' - '+str(datetime.date.today())+'/'+category_name+'/'+category_name+'_products_'+category_name+'_'+str(datetime.date.today())+'.txt')
								write_file(the_url, '')

							with open(the_url, 'w' ) as outfile:
								json.dump(faker, outfile)
							
							#We call the news function to work on the newly created product object file and add it to Mysql Product and News Database
							#And also add any product that has altered in attributes(i.e Price) to the News Table
							#The News Function Handles all these for us
							news(arg, argz)

							#The Set is Cleared after each Category is crawled and saved to file
							each_filter_category.items.clear()

							#The Set is Cleared after each Full Product Information is crawled and saved to file
							try:
								product_info.items.clear()
							except:
								pass

							faker = {}  
							faker['product'] = []

						
							


					#WE RUN ELSE BLOCK IF - THE CURRENT PRODUCT CATEGORY DOESN'T HAVE FILTERS
					else:	
						print("This Store doesnt have filters...")						
						#All the Links Stored in the Set Per Category Are Written to the File bearing the Category Name
						#set_to_file(list(crawl_each_category.items)[:40], urls)
						set_to_file(crawl_each_category.items, urls)

						#After Adding Each Links Per Category to File, Its time to get their Full Detail and Add to File Too
						
						matrix = NeuralCrawler('searchindex.db')

						#for item in list(crawl_each_category.items)[:40]:
						for item in crawl_each_category.items:
						# for item in list(crawl_each_category.items)[:10]:

							#Let Us Index and Add Each Info From All Products Category to our Neural Network Databases Before Getting their Full Info With our DetailCrawler
							#Let Us Index and Add Each Info From All Products Category to our Neural Network Databases Before Getting their Full Info With our DetailCrawler
							#Let Us Index and Add Each Info From All Products Category to our Neural Network Databases Before Getting their Full Info With our DetailCrawler
							matrix.crawl(item)
							#End of Neural Functionality
							#End of Neural Functionality
							#End of Neural Functionality

							product_info = DetailCrawler(item, product_name, product_color, product_seller, product_current_price, product_old_price, product_categories, product_sizes, product_percentage_off, product_images, product_description, "")
							product_info.product_detail()


							for items in product_info.items:
								data['product'].append(items)
								faker['product'].append(items)
								#time.sleep(5)

						the_url = os.path.join('products/' + crawler.project+' - '+str(datetime.date.today())+'/'+category_name +'/'+category_name+'_products_'+category_name+'_'+str(datetime.date.today())+'.txt')
						if not os.path.isfile(the_url):
							print('Category Completely Crawled :',  crawler.project+' - '+str(datetime.date.today())+'/'+category_name+'/'+category_name+'_products_'+category_name+'_'+str(datetime.date.today())+'.txt')
							write_file(the_url, '')

						with open(the_url, 'w' ) as outfile:
							json.dump(faker, outfile)
						
						#We call the news function to work on the newly created product object file and add it to Mysql Product and News Database
						#And also add any product that has altered in attributes(i.e Price) to the News Table
						#The News Function Handles all these for us
						news(arg, argz)

						#The Set is Cleared after each Category is crawled and saved to file
						crawl_each_category.items.clear()

						#The Set is Cleared after each Full Product Information is crawled and saved to file
						try:
							product_info.items.clear()
						except:
							pass

						faker = {}  
						faker['product'] = []  
						

				else:
					print('Sorry File :', urls, 'Already Exists')

			else:
				path = 'products/' +crawler.project+' - '+str(datetime.date.today())+'/'+category_name
				text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
				print("Nos of txt files are: ", len(text_files))

				nosOfFiles = len(text_files)
				last = text_files[-1]
				print("Last File is: ", last)

				if nosOfFiles == 1 :
					os.remove(path+'/'+last)
					os.rmdir(path)
					print("We removed file and directory...")
				print('Sorry Category Folder :', crawler.project+' - '+str(datetime.date.today())+'/'+category_name, 'Already Exists')
				

		ans = get_full_domain_name(website_name)

		if ans == "ng.fashpa.com":
			each_project = "ng.fashpa.com"
		else:
			each_project = get_domain_name(website_name)

		

		randomStr = randint(123456, 989121)
		final_url = os.path.join('media/products_all_categories_objects_for_' + str(each_project) +'_'+ str(randomStr) +'_'+ str(datetime.date.today())+'.txt')
		if not os.path.isfile(final_url):
			print('Completed Crawling of this Store :',  'media/products_all_categories_objects_for_' + str(datetime.date.today())+'.txt' ) 
			write_file(final_url, '')
		with open(final_url, 'w') as outfile:
			json.dump(data, outfile)

	else:
		print("request is not post ")
	return render(request, 'products/news.html')

