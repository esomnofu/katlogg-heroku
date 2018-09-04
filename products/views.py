
#Dango Modules
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
import json
import os
from django.conf import settings

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









# Create your views here.




# Create your views here.

def index(request):

	#Initialization of the Refresh our Crawler Calculation Index to Reflect Current Status of Ratings on Website Loaded
	try:
		neural_ntwk = searchnet('nn.db')
		neural_ntwk.maketables()
	except:
		pass

	page_rank = NeuralCrawler('searchindex.db')
	#page_rank.createindextables()

	#Calling the Refresh Method
	#page_rank.calculatepagerank()

	#Start Process to get Products From Text File
	#Start Process to get Products From Text File
	#Start Process to get Products From Text File

	"""
	path = '/Users/DIAMONDSCRIPTS/Desktop/django/media'

	text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
	last = text_files[-1]

	new_data = []
	with open(os.path.join(settings.STATIC_ROOT, last)) as json_file:
		data = json.load(json_file)
		for p in data['product']:
			each_item = {'name':p['name'], 'seller':p['seller'], 'current_price':p['current_price'], 'old_price':p['old_price'], 'url':p['url'], 'categories':p['categories'].split(','), 'valid_sizes':p['valid_sizes'].split(), 'off':p['off'], 'valid_images':p['valid_images'].split(), 'color':p['color'] }
			new_data.append(each_item)

		desc_new_data = new_data[::-1]

	"""
	
	#End Process to get Products From Text Files
	#End Process to get Products From Text Files
	#End Process to get Products From Text Files

	#Get Products From Products Table in Database

	all_products = Product.objects.all().order_by('-date')


	paginator = Paginator(all_products, 20)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		datum = paginator.page(page)

	except(EmptyPage, InvalidPage):
		datum = paginator.page(paginator.num_pages)


	return render(request, 'products/product.html', {'datum' : datum})

def crawl(request):

	
	if request.method == 'POST':
		website_name = request.POST['website_name']
		website_name.strip()
		major_url = request.POST['major_url']
		major_url.strip()
		relay_links = request.POST['relay_links']
		relay_links.strip()
		start_page_number = request.POST['start_page_number']
		start_page_number.strip()
		end_page_number = request.POST['end_page_number']
		end_page_number.strip()
		concatenation_pattern = request.POST['pagination_index']
		concatenation_pattern.strip()
		product_url = request.POST['product_url']
		product_url.strip()
		product_name = request.POST['product_name']
		product_name.strip()
		product_seller = request.POST['product_seller']
		product_seller.strip()
		product_color = request.POST['product_color']
		product_color.strip()
		product_current_price = request.POST['product_current_price']
		product_current_price.strip()
		product_old_price = request.POST['product_old_price']
		product_old_price.strip()
		product_categories = request.POST['product_categories']
		product_categories.strip()
		product_sizes = request.POST['product_sizes']
		product_sizes.strip()
		product_percentage_off = request.POST['product_percentage_off']
		product_percentage_off.strip()
		product_images = request.POST['product_images']
		product_images.strip()
		product_description = request.POST['product_description']
		product_description.strip()
		product_filters = request.POST['product_filters']
		product_filters.strip()
		product_filters_texts = request.POST['product_filters_texts']
		product_filters_texts.strip()

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
				arg = os.path.join('/Users/DIAMONDSCRIPTS/Desktop/katlogg/products/' + crawler.project+' - '+str(datetime.date.today())+'/'+category_name+'/')
				
				#Argument Two to Feed The News Function in General.py
				argz = os.path.join('/' + crawler.project+' - '+str(datetime.date.today())+'/'+category_name+'/')

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
	return render(request, 'products/news.html')


def search(request):
	
	neural_network = searcher('searchindex.db')

	if request.method == 'POST':

		search = request.POST['search']
		
		query = neural_network.query(search)

		if query:

			results = query[0]

			wordids = query[1]

			urlids = query[2]

			scores = query[3]

			return render(request, 'products/search.html', {'results':results, 'search':search, 'wordids':wordids, 'urlids':urlids, 'scores':scores})
		else:
			return render(request, 'products/search.html', {'results':'Search Not Available', 'search':search, 'query':query})

def train(request):

	#neural_network = searcher('searchindex.db')

	#mynet = neural_network.mynet


	if request.method == 'POST':

		
		wordids = request.POST['wordids']

		arr_wordids = []

		for word in wordids.split(','):
			arr_wordids.append(int(word.strip()))

		urlids = request.POST['urlids']

		arr_urlids = [int(url.strip()) for url in urlids.split(',')]
		
		theselectedurlid = int(request.POST['theselectedurlid'])
		
		neural = searchnet('nn.db')
		
		neural.trainquery(arr_wordids, arr_urlids, theselectedurlid)
		
		print(neural.getresult(arr_wordids, arr_urlids))

		#return render(request, 'products/training.html', {'trainings':trainings})
		return redirect('index')

def form(request):
	names_xpaths = XpathList.objects.values_list('website_name', flat=True)    
	return render(request, 'products/form.html', {"xpaths":names_xpaths})

def newsfeed(request):

	all_entries = News.objects.all().order_by('-date')

	paginator = Paginator(all_entries, 20)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		datum = paginator.page(page)

	except(EmptyPage, InvalidPage):
		datum = paginator.page(paginator.num_pages)
	return render(request, 'products/news.html', {'datum' : datum})


def reduce(request):

	all_entries = News.objects.filter(product_price_change_type='down').order_by('-date')

	paginator = Paginator(all_entries, 10)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		datum = paginator.page(page)

	except(EmptyPage, InvalidPage):
		datum = paginator.page(paginator.num_pages)


	return render(request, 'products/news.html', {'datum' : datum})

def increase(request):

	all_entries = News.objects.filter(product_price_change_type='up').order_by('-date')

	paginator = Paginator(all_entries, 10)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		datum = paginator.page(page)

	except(EmptyPage, InvalidPage):
		datum = paginator.page(paginator.num_pages)


	return render(request, 'products/news.html', {'datum' : datum})

def color(request):

	all_entries = News.objects.filter(product_color_change='Yes').order_by('-date')

	paginator = Paginator(all_entries, 10)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		datum = paginator.page(page)

	except(EmptyPage, InvalidPage):
		datum = paginator.page(paginator.num_pages)


	return render(request, 'products/news.html', {'datum' : datum})

def size(request):

	all_entries = News.objects.filter(product_size_change='Yes').order_by('-date')

	paginator = Paginator(all_entries, 10)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		datum = paginator.page(page)

	except(EmptyPage, InvalidPage):
		datum = paginator.page(paginator.num_pages)


	return render(request, 'products/news.html', {'datum' : datum})


#ITEM BASED RECOMMENDATIONS VIEWS
#ITEM BASED RECOMMENDATIONS VIEWS
#ITEM BASED RECOMMENDATIONS VIEWS
def signup(request):

	form = MyUserRegisterForm()

	if request.method == "POST":
		#Instantiate received request into a new form

		received_req = MyUserRegisterForm(request.POST)

		if received_req.is_valid():
			user = received_req.save()
			#Log the User In
			login(request, user)
			return redirect('index')
			#return render(request, 'myapp/index.html', {'success':'Successfully Registered'})



	return render(request, 'products/signup.html', {'form':form} )

def signin(request):

	form = AuthenticationForm()

	if request.method == "POST":
		#Instantiate received request into a new form

		received_req = AuthenticationForm(data=request.POST)

		if received_req.is_valid():
			#Log the User In

			user = received_req.get_user()
			login(request, user)

			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			return redirect('index')
			


	return render(request, 'products/login.html', {'form':form} )

def loggedout(request):
	if request.method == "POST":
		logout(request)
		return redirect('index')

@login_required(login_url="signin")
def newsroom(request):
	form = AddRating()
	return render(request, 'products/newsroom.html', {'form':form})



def create(request):
	if request.method == "POST":


		#print('Item name', item_name)
		#received_req = AddRating(request.POST)
		#print("Received Request is ", received_req)

		
		item_name = request.POST['item_name']

		item_rating = request.POST['item_rating']

		requested_user_id = request.user.id

		if item_name != '':

			#Count is 1 if Movie Has been Rated by this user before
			exist_count = Ratings.objects.filter(item_name=item_name, rater_id=request.user.id).count()

			#print("Existence Count", exist_count)
			if exist_count > 0:
				return redirect('index')
			else:	
				each_table_row = Ratings( item_name=item_name, item_rating=item_rating, rater_id=requested_user_id )
				each_table_row.save()
				return render(request, 'products/product.html')

		else:

			received_req = AddRating(request.POST)
			
			#Parameters Needed To Check if the Rater has rated this product before
			this_rater_item_name = request.POST['item_name']
			this_rater_id = request.user.id
			
			if received_req.is_valid():
				#Count is 1 if Movie Has been Rated by this user before
				exist_count = Ratings.objects.filter(item_name=this_rater_item_name, rater_id=this_rater_id).count()
				
				#print("Existence Count", exist_count)
				if exist_count > 0:
					return redirect('index')
				else:	
					instance = received_req.save(commit=False)
					instance.rater = request.user
					this_rater_id = instance.rater.id
					instance.save()
					return redirect('index')

#For Recommendations
@login_required(login_url="signin")
def recommend(request):

	#The Critics Dictionary
	critics = {}

	#Grabbing All Users By IDs
	userids = User.objects.values_list('id', flat=True)


	#print("Authenticated User Is", request.user)

	#iterate all users
	for userid in userids:
		userid = str(userid)

		#if user has at least one rating
		#We add to our pool for recommendation
		user_count = Ratings.objects.filter(rater_id=userid).count()
		#print("The User", userid, "has", user_count, "ratings available")

		if user_count > 0:
			#If user have a Rating

			#get_object_or_404 gets the product or return 404
			#We use this so as to get the username and use it in the Critics Dictionary
			#Instead of Using IDs
			user_name = get_object_or_404(User, id=userid)


			#we grab all this current iterating user ratings
			user_ratings = Ratings.objects.filter(rater_id=userid)

			
			for rate in user_ratings:
				#print('this rating', rate.user_rated())
				product_and_rate = rate.user_rated()
				#print(user_name, 'has', product_and_rate, 'ratings')
				try:
					critics[str(user_name)][str(product_and_rate[0])] = float(product_and_rate[1])
				except KeyError:
					critics[str(user_name)] = {str(product_and_rate[0]) : float(product_and_rate[1]) }


	#START OUTPUTTING
	#START OUTPUTTING
	#START OUTPUTTING

	#critics = critics['LisaRose']['Lady in the Water']
	#critics = critics['Toby']['Snakes on a Plane']
	#critics = critics['Toby']
	#critics = sim_distance(critics, 'LisaRose', 'GeneSeymour')
	#critics = sim_pearson(critics, 'LisaRose', 'GeneSeymour')
	#critics = topMatches(critics, 'Toby', n=3)
	#critics = getRecommendations(critics, 'Toby')
	#critics = getRecommendations(critics, 'Toby', similarity=sim_distance)
	
	#Transform Critics Dictionary From User Based to Item Based
	item_based_products = transformPrefs(critics)

	#Top Matches of an Item
	#critics = topMatches(item_based_products, 'Superman Returns')

	#Recommend A Movie To Some Users Based on their Current Rating
	#and How the Movie Scale Up Others
	#critics = getRecommendations(item_based_products, 'Just My Luck')

	#This Can be Done Once in A week to Refresh Similarities Not Too Often
	#Cos this takes a very long time to execute especially when Dataset is large
	#itemsim refers to item similarities
	itemsim=calculateSimilarItems(critics)

	authenticated_user = str(request.user)

	#Final Items Recommendations
	critics = getRecommendedItems(critics,itemsim,authenticated_user)

	#Return critics to show item and alongside Rating
	#Otherwise user_unique_news to show only item

	user_unique_news = [ critic[1] for critic in critics ]

	personalized_news = []

	for url in user_unique_news:
		each_object = get_object_or_404(Product, product_url=url)
		personalized_news.append(each_object)
		#print("Each Object Is:", each_object)



	paginator = Paginator(personalized_news, 5)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		datum = paginator.page(page)

	except(EmptyPage, InvalidPage):
		datum = paginator.page(paginator.num_pages)

	
	if len(datum) == 0:
		datum = ''

	#print("Datum is", datum)
	

	return render(request, 'products/recommend.html', {'datum' : datum})

#ENDITEM BASED RECOMMENDATIONS VIEWS
#ENDITEM BASED RECOMMENDATIONS VIEWS
#ENDITEM BASED RECOMMENDATIONS VIEWS



#XPATHS REQ
#XPATH REQS
def getXpaths(request):
	
	if request.method == 'POST':
		print("The Request is POST...")
		name = request.POST['website_name'].strip()
		correspondingData = XpathList.objects.filter(website_name=name).values_list()
		#data = get_object_or_404(XpathList, website_name=name).values_list()
		return JsonResponse({"output": list(correspondingData)})
	else :
		print("No Response")
		return render('products/form.html', locals())



def addstore(request):

	if request.method == "POST":

		website_name = request.POST['website_name']
		website_name.strip()
		major_url = request.POST['major_url']
		major_url.strip()
		relay_links = request.POST['relay_links']
		relay_links.strip()
		pagination_index = request.POST['pagination_index']
		pagination_index.strip()
		product_url = request.POST['product_url']
		product_url.strip()
		product_name = request.POST['product_name']
		product_name.strip()
		product_seller = request.POST['product_seller']
		product_seller.strip()
		product_color = request.POST['product_color']
		product_color.strip()
		product_current_price = request.POST['product_current_price']
		product_current_price.strip()
		product_old_price = request.POST['product_old_price']
		product_old_price.strip()
		product_categories = request.POST['product_categories']
		product_categories.strip()
		product_sizes = request.POST['product_sizes']
		product_sizes.strip()
		product_percentage_off = request.POST['product_percentage_off']
		product_percentage_off.strip()
		product_images = request.POST['product_images']
		product_images.strip()
		product_description = request.POST['product_description']
		product_description.strip()		
		product_filters = request.POST['product_filters']
		product_filters.strip()		
		product_filters_texts = request.POST['product_filters_texts']
		product_filters_texts.strip()

		xpath = XpathList(website_name=website_name, major_url=major_url, relay_links=relay_links, pagination_index=pagination_index, product_url=product_url, product_name=product_name,product_seller=product_seller, product_color=product_color, product_current_price=product_current_price, product_old_price=product_old_price, product_categories=product_categories, product_sizes=product_sizes, product_percentage_off=product_percentage_off, product_images=product_images, product_description=product_description, product_filters=product_filters, product_filters_texts=product_filters_texts)
		xpath.save()
		return HttpResponse("success")

	return render(request, 'products/addstore.html')



def dstesting(request):

	all_products = Product.objects.all().order_by('-date')


	paginator = Paginator(all_products, 20)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		datum = paginator.page(page)

	except(EmptyPage, InvalidPage):
		datum = paginator.page(paginator.num_pages)

	return render(request, 'products/dstesting.html', {'datum' : datum})


def unidentified(request):

	all_products = Unidentified.objects.all().order_by('-date')


	paginator = Paginator(all_products, 20)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		datum = paginator.page(page)

	except(EmptyPage, InvalidPage):
		datum = paginator.page(paginator.num_pages)

	return render(request, 'products/unidentified.html', {'datum' : datum})




#START CLASS BASED VIEW FOR API CALLS
#START CLASS BASED VIEW FOR API CALLS
#START CLASS BASED VIEW FOR API CALLS
#START CLASS BASED VIEW FOR API CALLS

class ProductList(APIView):

	def get(self, request):
		all_existing_products = Product.objects.all()
		serializer = ProductSerializer(all_existing_products, many=True)
		return Response(serializer.data)


	def post(self):
		pass


class ProductView(viewsets.ModelViewSet):

	queryset = Product.objects.all()

	serializer_class = ProductSerializer
