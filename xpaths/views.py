#For Initial API FXns
#For Initial API FXns
#For Initial API FXns
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

from .models import XpathList




#For Crawler Class
#For Crawler Class
#For Crawler Class
#Paginator Module
from django.core.paginator import Paginator, EmptyPage, InvalidPage

#Modules For Crawler
from lxml import html
import requests
import datetime
from products.get_all_major_category_links import HomeCrawler
from products.get_all_item_links_by_sub_category import CategoryCrawler
from products.detailed_view import DetailCrawler
from products.general import *
from products.domain import *
from products.detect_changes import *
import time

#Module for Neural Network
from products.searchengine import *
#from products.nn import *



#Import Models Here

from products.models import *

#Get Object or 404
from django.shortcuts import get_object_or_404
import json
import os
from django.conf import settings




class Xpath(View):
    def get(self, request):
        xpath_list = list(XpathList.objects.values())
        return JsonResponse(xpath_list, safe=False) 

    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Xpath, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.body.decode('utf8')
        data = json.loads(data)
        try:
            new_xpath = XpathList(website_name=data["website_name"], major_url=data["major_url"], relay_links=data["relay_links"], start_page_number=data["start_page_number"],  end_page_number=data["end_page_number"], pagination_index=data["pagination_index"], product_url=data["product_url"], product_name=data["product_name"], product_seller=data["product_seller"], product_color=data["product_color"], product_current_price=data["product_current_price"], product_old_price=data["product_old_price"], product_categories=data["product_categories"], product_sizes=data["product_sizes"], product_percentage_off=data["product_percentage_off"], product_images=data["product_images"], product_description=data["product_description"])
            new_xpath.save()
            return JsonResponse({"New Xpath Successfully Added": data}, safe=False)
        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)



class XpathDetail(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(XpathDetail, self).dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        xpath_list = {"xpath": list(XpathList.objects.filter(pk=pk).values())}
        return JsonResponse(xpath_list, safe=False)

    def put(self, request, pk):
        data = request.body.decode('utf8')
        data = json.loads(data)
        try:
            new_xpath = XpathList.objects.get(pk=pk)

            data_key = list(data.keys())

            for key in data_key:

                if key == "website_name":
                    new_xpath.website_name = data[key]
                
                if key == "major_url":
                    new_xpath.major_url = data[key]

                if key == "relay_links":
                    new_xpath.relay_links = data[key]
                
                if key == "start_page_number":
                    new_xpath.start_page_number = data[key]

                if key == "end_page_number":
                    new_xpath.end_page_number = data[key]
                
                if key == "pagination_index":
                    new_xpath.pagination_index = data[key]

                if key == "product_name":
                    new_xpath.product_name = data[key]
                
                if key == "product_seller":
                    new_xpath.product_seller = data[key]

                if key == "product_color":
                    new_xpath.product_color = data[key]
                
                if key == "product_current_price":
                    new_xpath.product_current_price = data[key]

                if key == "product_old_price":
                    new_xpath.product_old_price = data[key]
                
                if key == "product_categories":
                    new_xpath.product_categories = data[key]

                if key == "product_sizes":
                    new_xpath.product_sizes = data[key]
                
                if key == "product_percentage_off":
                    new_xpath.product_percentage_off = data[key]

                if key == "product_images":
                    new_xpath.product_images = data[key]
                
                if key == "product_description":
                    new_xpath.product_description = data[key]
        
            new_xpath.save()
            return JsonResponse({"updated xpath": data}, safe=False)
        except XpathList.DoesNotExist:
            return JsonResponse({"error": "The xpath you provided primary key does not exist"}, safe=False)
        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)

    def delete(self, request, pk):
        try:
            new_xpath = XpathList.objects.get(pk=pk)
            new_xpath.delete()
            return JsonResponse({"deleted xpath": True}, safe=False)
        except:
            return JsonResponse({"error": "not a valid primary key"}, safe=False)



class XpathStores(View):
    def get(self, request):
        xpath_list = list(XpathList.objects.values())
        stores = {}
        #print("Product Names", xpath_list)
        for loop_index, each in enumerate(xpath_list):
            stores[loop_index] = each['website_name']
            print(loop_index, each['website_name'])
        #[print(product_name) for product in xpath_list]
        #print("Product Name", xpath_list[0]['product_name'])
        return JsonResponse(stores, safe=False) 

    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(XpathStores, self).dispatch(request, *args, **kwargs)




class XpathCrawl(View):
    def get(self, request):
        xpath_list = list(Product.objects.values())
        return JsonResponse(xpath_list, safe=False) 

    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(XpathCrawl, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.body.decode('utf8')
        data = json.loads(data)

        try:
            website_name = data["website_name"]
            website_name.strip()
            major_url = data['major_url']
            major_url.strip()
            relay_links = data['relay_links']
            relay_links.strip()
            start_page_number = data['start_page_number']
            start_page_number.strip()
            end_page_number = data['end_page_number']
            end_page_number.strip()
            concatenation_pattern = data['pagination_index']
            concatenation_pattern.strip()
            product_url = data['product_url']
            product_url.strip()
            product_name = data['product_name']
            product_name.strip()
            product_seller = data['product_seller']
            product_seller.strip()
            product_color = data['product_color']
            product_color.strip()
            product_current_price = data['product_current_price']
            product_current_price.strip()
            product_old_price = data['product_old_price']
            product_old_price.strip()
            product_categories = data['product_categories']
            product_categories.strip()
            product_sizes = data['product_sizes']
            product_sizes.strip()
            product_percentage_off = data['product_percentage_off']
            product_percentage_off.strip()
            product_images = data['product_images']
            product_images.strip()
            product_description = data['product_description']
            product_description.strip()

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

                #print('Category is', category)

                cat_num = category.split('/')
                #print('Category List', cat_num)

                category_name = cat_num[-1]
                #print("Category name", category_name)

                #Replace Question marks with nothing as it impedes folder/file creation
                category_name = category_name.replace('?', '')

            #Creating A Folder for every Category Under the Project Name which already bears the Timestamp of the Day
                if not os.path.exists( os.path.join('products/' +crawler.project+' - '+str(datetime.date.today())+'/'+category_name) ):
                    print('Created Category Folder For :',  crawler.project+' - '+str(datetime.date.today())+'/'+category_name)


            #Creating a Folder For Each Category
                    os.makedirs(os.path.join('products/' +crawler.project+' - '+str(datetime.date.today())+'/'+category_name) )


            #Creating a File for All Links Found in a Category      
                    urls = os.path.join('products/' + crawler.project+' - '+str(datetime.date.today())+'/'+category_name +'/'+category_name+'.txt')
                    

                    #Argument One to Feed The News Function in General.py
                    arg = os.path.join('/Users/DIAMONDSCRIPTS/Desktop/django/rest/products/' + crawler.project+' - '+str(datetime.date.today())+'/'+category_name+'/')
                    
                    #Argument Two to Feed The News Function in General.py
                    argz = os.path.join('/' + crawler.project+' - '+str(datetime.date.today())+'/'+category_name+'/')

                    if not os.path.isfile(urls):
                        print('Created File :',  crawler.project+' - '+str(datetime.date.today())+'/'+category_name+'/'+category_name+'.txt')
                        write_file(urls, '')


                        #Crawl Each Category Gotten From HomeCrawler With CategoryCrawler
                        print('Now crawling and Writing all products URL in:', category_name, 'category to', category_name, 'text file, please be patient this might take some few minutes...')
                        crawl_each_category = CategoryCrawler(category, start_page_number, end_page_number, concatenation_pattern, product_url)
                        crawl_each_category.crawl()

                        #All the Links Stored in the Set Per Category Are Written to the File bearing the Category Name
                        #set_to_file(list(crawl_each_category.items)[:40], urls)
                        set_to_file(crawl_each_category.items, urls)


                        print('Now Crawling Each URL for Full Product Information to text file...')
                        #After Adding Each Links Per Category to File, Its time to get their Full Detail and Add to File Too
                        
                        matrix = NeuralCrawler('searchindex.db')

                        #for item in list(crawl_each_category.items)[:40]:
                        for item in crawl_each_category.items:

                            #Let Us Index and Add Each Info From All Products Category to our Neural Network Databases Before Getting their Full Info With our DetailCrawler
                            #Let Us Index and Add Each Info From All Products Category to our Neural Network Databases Before Getting their Full Info With our DetailCrawler
                            #Let Us Index and Add Each Info From All Products Category to our Neural Network Databases Before Getting their Full Info With our DetailCrawler
                            matrix.crawl(item)
                            #End of Neural Functionality
                            #End of Neural Functionality
                            #End of Neural Functionality

                            product_info = DetailCrawler(item, product_name, product_color, product_seller, product_current_price, product_old_price, product_categories, product_sizes, product_percentage_off, product_images, product_description)
                            product_info.product_detail()


                            for items in product_info.items:
                                data['product'].append(items)
                                faker['product'].append(items)
                                #time.sleep(5)

                        the_url = os.path.join('products/' + crawler.project+' - '+str(datetime.date.today())+'/'+category_name +'/'+category_name+'_products_'+str(datetime.date.today())+'.txt')
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
                    print('Sorry Category Folder :', crawler.project+' - '+str(datetime.date.today())+'/'+category_name, 'Already Exists')
                    
                    


            print('Now Writing All Full Products Information to text file...')

            each_project = get_domain_name(website_name)

            final_url = os.path.join('media/products_all_categories_objects_for_' + str(each_project) +'_'+ str(datetime.date.today())+'.txt')
            if not os.path.isfile(final_url):
                print('Created Comprehensive and Final Dictionary Object For All Products Information File :',  'media/products_all_categories_objects_for_' + str(datetime.date.today())+'.txt' ) 
                write_file(final_url, '')
            with open(final_url, 'w') as outfile:
                json.dump(data, outfile)

            return JsonResponse({"Crawling Completed For Store - ": each_project}, safe=False)

        except:
            
            return JsonResponse({"error": "An Error Occurred while crawling the store"}, safe=False)






class XpathCrawlDetail(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(XpathCrawlDetail, self).dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        #print("Primary key is", pk)
        #xpath_list = {"xpath": list(Product.objects.filter(pk=pk).values())}
        xpath_list = list(XpathList.objects.filter(pk=pk).values())


        #print("Product Name", xpath_list[0]['product_name'])
        return JsonResponse(xpath_list, safe=False)

    def put(self, request, pk):
        data = request.body.decode('utf8')
        data = json.loads(data)
        try:
            new_xpath = Product.objects.get(pk=pk)

            data_key = list(data.keys())

            for key in data_key:

                if key == "website_name":
                    new_xpath.website_name = data[key]
                
                if key == "major_url":
                    new_xpath.major_url = data[key]

                if key == "relay_links":
                    new_xpath.relay_links = data[key]
                
                if key == "start_page_number":
                    new_xpath.start_page_number = data[key]

                if key == "end_page_number":
                    new_xpath.end_page_number = data[key]
                
                if key == "pagination_index":
                    new_xpath.pagination_index = data[key]

                if key == "product_name":
                    new_xpath.product_name = data[key]
                
                if key == "product_seller":
                    new_xpath.product_seller = data[key]

                if key == "product_color":
                    new_xpath.product_color = data[key]
                
                if key == "product_current_price":
                    new_xpath.product_current_price = data[key]

                if key == "product_old_price":
                    new_xpath.product_old_price = data[key]
                
                if key == "product_categories":
                    new_xpath.product_categories = data[key]

                if key == "product_sizes":
                    new_xpath.product_sizes = data[key]
                
                if key == "product_percentage_off":
                    new_xpath.product_percentage_off = data[key]

                if key == "product_images":
                    new_xpath.product_images = data[key]
                
                if key == "product_description":
                    new_xpath.product_description = data[key]
        
            new_xpath.save()
            return JsonResponse({"updated xpath": data}, safe=False)
        except Product.DoesNotExist:
            return JsonResponse({"error": "The xpath you provided primary key does not exist"}, safe=False)
        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)

    def delete(self, request, pk):
        try:
            new_xpath = Product.objects.get(pk=pk)
            new_xpath.delete()
            return JsonResponse({"deleted xpath": True}, safe=False)
        except:
            return JsonResponse({"error": "not a valid primary key"}, safe=False)

